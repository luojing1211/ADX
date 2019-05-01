"""test tables 
"""
import unittest2 as unittest

from adx.table.jsontable import JsonTable
from adx.filter import ExtFilter
import os

dataDir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'fs', 'lofasm1')

class TestLofasmJsonTable(unittest.TestCase):
    def test_newdir(self):
        """load a new data directory
        """
        jt = JsonTable('lofasm', fp=dataDir)
        self.assertEqual(os.path.basename(jt.tablepath), "lofasm.adx.json")
        self.assertEqual(jt.tablepath, os.path.join(dataDir,'.adx','lofasm.adx.json'))
        # purge file / directory
        if os.path.isfile(jt.tablepath):
            os.remove(jt.tablepath)
        if os.path.isdir(os.path.dirname(jt.tablepath)):
            os.rmdir(os.path.dirname(jt.tablepath))


    def test_create_basic_table(self):
        """create a basic table and store minimal values
        """
        jt = JsonTable('lofasm', fp=dataDir)
        sampleData = {'mtime': 12345678.8765422}
        jt.data = sampleData
        tbl_path = jt.tablepath
        jt.save()

        jt2 = JsonTable('lofasm', fp=os.path.join(dataDir,'.adx','lofasm.adx.json'))
        self.assertEqual(sampleData, jt2.data)

        # purge file / directory
        if os.path.isfile(jt.tablepath):
            os.remove(jt.tablepath)
        if os.path.isdir(os.path.dirname(jt.tablepath)):
            os.rmdir(os.path.dirname(jt.tablepath))

        


if __name__ == "__main__":
    unittest.main()
