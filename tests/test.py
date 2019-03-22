from adx import Adx
from adx.parser import parser
from adx.crawler import crawler
from adx.logger import logger

myCrawl = crawler(pdir, batchsize=100)

log = logger('localhost:84001',writeDB='./save.db', numtables=1)

profpar = parser('^\d{8}_\d{6}_[BJ]\d{4}[+-]\d{4}.prof$')
profpar.AddFloat('SN', getSN)
profpar.AddString('Source', getSource)
#
myparse = parser()
myparse.AddParserType(profpar)

myAdx = Adx(crawler=myCrawl, logger=log, parser=myparse)
