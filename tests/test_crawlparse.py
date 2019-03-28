from adx.parser import Parser
from adx.parser import ParserType
from adx.adx import Adx # I don't like this way of importing
###############################
path = "/home/shining/study/MS/vLITE/mkerr/fil"
pars = Parser()
###
filpt = ParserType('fil')
rgrule = "^\d{8}_\d{6}_muos_ea\d{2}_kur.fil$"
filpt.AddFilenameRegexRule(rgrule)
filpt.AddString('filename', 30, lambda x : x)
###
pars.AddParserType(filpt)
###############################
myadx = Adx(path, pars)
