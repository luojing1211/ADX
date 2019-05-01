"""test ADX file filters

"""
import unittest2 as unittest

from adx.table.jsontable import JsonTable
from adx.filter import ExtFilter
import os

dataDir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'fs', 'lofasm1')

class TestExtFilter(unittest.TestCase):
    def test_filterTargets(self):
        """Test: Filter Targets by extension
        """
        flist = os.listdir(dataDir)
        flist_no_lofasm = [f for f in flist if not f.endswith('.lofasm')]
        flist_no_lofasm_or_lofasmgz = [f for f in flist if \
                not f.endswith('.lofasm') and \
                not f.endswith('.lofasm.gz')]
        flist_no_bbx_or_bbxgz = [f for f in flist if \
                not f.endswith('.bbx') and \
                not f.endswith('.bbx.gz')]
        flist_no_exe = os.listdir(dataDir)

        # define filters
        lofasmFilter = ExtFilter('.lofasm')
        lofasmFilter2 = ExtFilter(['.lofasm', '.lofasm.gz'])
        bbxFilter = ExtFilter(['.bbx', '.bbx.gz'])
        exeFilter = ExtFilter('.exe') # should not match any files!

        result = lofasmFilter(flist)
        self.assertEqual(result[1], flist_no_lofasm)

        flist = os.listdir(dataDir)
        result = lofasmFilter2(flist)
        self.assertEqual(result[1], flist_no_lofasm_or_lofasmgz)

        flist = os.listdir(dataDir)
        result = bbxFilter(flist)
        self.assertEqual(result[1], flist_no_bbx_or_bbxgz)

        flist = os.listdir(dataDir)
        result = exeFilter(flist)
        self.assertEqual(result[1], flist_no_exe)




