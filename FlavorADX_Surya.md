# This is mere flavor of ADX


  Assuming our data directory is conveniently mounted on root like `/data`. 
  
## Crawler

  Crawler can either run from your favorite shell as a standalone program or run in the background as daemon patiently waiting and checking for new files for indexing and analyzing. 
  
To run the daemon on our data directory:
  
  adxd /data --parser=Parse_Filterbank.py
  
  adxd /data --frequency * * * 59
  
  adxd /data --db=localhost 34001
  
  `parser` argument is nothing but a class definition which will be defined below
  
  `frequency` argument is just like arguments of crontabs which decides the frequency at which the daemon should check for new files. 
  
  `db` argument provides the IP and port number to host a database. It will be ignored if user seeks astropy tables argument.
  
  To run the crawler from your shell:
  `$ adx /data --parser=Parse_Filterbank.py`
  
  As mentioned above, `parser` will be discussed here.
 
 
## Parser
  There will be a main parser class which user doesn't touch. All the info will be added to the parser class by Adx `ParserType` instance. For instance, consider this example:
  
    ParserType fil
Creation of `ParserType` class
    
    fil.AddExtenstionRule('fil')
Method of `ParserType` which adds an rule for extension.
    
    fil.AddFilenameRegexRule('[JB]+[0-9]{4}[+-][0-9]{2,4}_[0-9]{5}_')
Method to add a regex rule to test for files for further processing. This regex is source JName or Bname followed by MJD.

    fil.AddFilenameRule('!kur')   
Method which adds filename rule. 
The rule starting with ! implies logical NOT.

    fil.AddFilenameRule('kur')
Method which adds filename rule, which means, that it will only accept kurtosis files.

    fil.AddSignature('^BBX')
Method which checks for signature in the file. N.B. there is no way around to NOT open the file. 
`^` means the beginning of the file. `$` means the end of the file. This is similar to regex matching. 
    
    fil.Reader(MyFilReader)
Binds class interface to Filterbank files with the parser. If this option is provided and there are metrics in *this* `ParserType` instance which take the class interface as argument, a single instantiation of the reader class (interface class) is instantiated and passed as argument to one (or more) such metrics. *This is will further elucidated in an example*
    
    fil.AddFloat('mean')
Adds a data field (which is to be tabulated) with column name 'mean' and since it is a fairly common statistics, `Parser` use it's own definition of mean computation. User doesn't have to provide this implementation of mean computation.
    
    fil.AddFloat('smean', GiveSMean)
Similar to above, but column name is 'smean' which stands for special mean and `GiveSMean` is a callable class or function 
    which is user provided. If the user has provided an interface class using `Reader` method, `GiveSMean` should take that class as an argument.
    
    fil.AddString('polarisation', GivePol)
This method adds a string data field with name 'polarisation' and similar to above `GivePol` is a callable class or function which can take either filename or `Reader` class as argument. The exact function matching falls on the mantle of users.
    
    fil.AddDateTime('ctime')
There will be some fields which are captured by ADX by default. One of them is the `ctime, atime, mtime` of files which proves to be helpful in keeping track of files.
    ....
    
There will/can be many more options which for brevity sake are left out. Now, here comes first act of magic:
    
    Parser.AddParserType(fil)
This method takes the necessary stuff (all the required things it would need) and merges it with `Parser` class. 
    `ParserType` class can be one heavy and over-engineered to the extent of over-engineering but ONLY those which are actually are relevant (decided by `Add*` methods as called by the user gets added) are injected into the `Parser` class. 
    You can add multiple parsertypes in the same `Parser` class and `Parser` class knows what to do with each of them. 
    
This approach not only gives set of tools for the user but only constraints the structure of the code and thereby increases regularity which helps us developers in writing smooth code. Instead of telling the user "look, this method `def __call__(self)` define it to your liking and then make it return dictionary with key value pairs" we are telling user to "you know what you want? OK, add methods which we provided in `ParserType` to get whatever you want. We made sure that anything you want, our methods in `ParserType` class can get you. Once, you're done, pass that class to main `Parser` and chill"

This approach also ensures that every file is only opened once since every metric is computed from same `File Handle`. 

### ParserType example

Let us crawl through a directory containing Pulsar integrated profiles which have .prof extension and first line (and only the first line) is a header with 
  
  `# MJD, Fraction-of-day, Number of periods in integration, period, DM, num-bins, polarisation, observatory-code`
 
 followed by num-bins number which correspond to actual data. 
 This is how it would look.
 
    ParserType prof
    prof.AddExtensionRule('prof')
    prof.Reader(MyProfReader)
    prof.AddFloat('SN',GiveSN)
    prof.AddFloat('DM',GiveDM)
    prof.AddFloat('MJD',GiveMJD)
    prof.AddString('PSR', 10, GiveJName)
    Parser.AddParserType(prof)
  
The functions used above are defined in the same place where `ParserType` is defined and they all have the following signature:
    
    class MyProfReader(object):
        def __init__(self, filepath):
            # initalization
            self.dm = ...
            self.data = ...
            
    def GiveDM(x):
        return x.sn
    
    def GiveSN(x):
        # SN computation using x.data
 
## Crawler

Coming back to crawler with our `Parser` class loaded with all the rules while still hidden by the user, can safely interact with `Crawler` class in a pre-determined fashion and just the way we developers seek.

    Parser.GetExtensions()
This method would return the extensions which were added to `Parser` class. 

Second act of magic:
`Parser` class where all the `ParserType` are injected creates regex rules for each of the `ParserType` classes. This regex rule is generated from filename, pathname, extension and is pretty robust. And, it is this rule which is passed onto to `Crawler` at the start of crawling which is used to figure out what to do. On successful match, `Parser` internally calls and computes all the metrics as asked by the user (the user is not calling an function, s/he is merely specifying what s/he wants).

## Logger
Third and final act of magic:

`Parser` class again comes to rescue here and tells us the schema of each of the table. `Crawler` and `Logger` can internally talk among themselves.

## Final comments

We can really brainstorm and add contrived `ParserType` methods such as `AddOnFile` which computes a statistics (not recorded by Logger) and performs logic based on the statistics.
    
    ParserType prof
    prof.AddOnFile(AlertIfNoDetection)
    
In the running example, `AddOnFile` binds function or callable class `AlertIfNoDetection` which takes `MyProfReader` as argument and runs some statistical test to check for detection and if it finds that there's no detection, it shouts. 

Not just it, this approach hides `Crawler` and `Logger` class from the user with the exception of `Parser` in which only one method is exposed, the `AddParserType` method. The definition of `Parser` will happen in the main body and `adx --parser=MyParser.py` uses it without defining it.  

The true power (according to me) comes from creating the tools which the user can just call and use to his/her liking and rest is taken care by ADX. 