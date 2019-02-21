# imports
import Parser, ParserType, Crawler, Logger
from somewhere import GiveDM, GiveSN, GiveMJD, GiveJName
from somewhereelse import MyFilReader
# definition
Parser myParser
Crawler myCrawler
Logger myLogger
#############################
import toy_my_parsers.py
'''
While thinking more about it, I realized that we don't have to explicitly call 
AddParserType methods of myParser, we can use 
globals()
method to iterate over all the objects in the global scope and marry them ourselves.

This way the user neednot bother with ensuring the parser object have the same name. 
'''
#############################
# let's make some friends
myCrawler.__RulesToCrawler( myParser.__RulesToCrawler() )
myLogger.__ReceiveSchema( myParser.__SchemaToLogger()  )

# enough talk, let's crawl
myCrawler.DoYourThing()
