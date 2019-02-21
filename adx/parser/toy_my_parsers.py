'''
So this is the only file which user will have to provide 
'''
from somewhere import GiveDM, GiveSN, GiveMJD, GiveJName
from somewhereelse import MyFilReader
# defining my parsertype
ParserType prof
prof.AddExtensionRule('prof')
prof.Reader(MyProfReader)
prof.AddFloat('SN',GiveSN)
prof.AddFloat('DM',GiveDM)
prof.AddFloat('MJD',GiveMJD)
prof.AddString('PSR', 10, GiveJName)
# marrying parsertype with Parser
# read globals 
myParser.AddParserType(prof)

# defining another parsertype
ParserType fil
fil.AddExtenstionRule('fil')
fil.AddFilenameRule('kur')
fil.Reader(MyFilReader)
fil.AddFloat('smean', GiveSMean)
# marrying parsertype with Parser
# read globals 
myParser.AddParserType(fil)

