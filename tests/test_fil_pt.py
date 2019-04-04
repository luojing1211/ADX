from adx.parser import ParserType
path = "/home/shining/study/MS/vLITE/mkerr/fil"
filpt = ParserType('fil')
rgrule = "^\d{8}_\d{6}_muos_ea\d{2}_.fil$"
filpt.AddFilenameRegexRule(rgrule)
filpt.AddString('filename', 30, lambda x : x)

