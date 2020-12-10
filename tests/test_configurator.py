import unittest2
import os
from configurator import get_attributes

class TestMain(unittest2.TestCase):

    def setUp(self):
        self.temporary_file = '/tmp/emptyfile.csv'
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        df = get_attributes("/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(df)

    def test_empty_datafie(self):
        df = get_attributes(self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = get_attributes(self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
        os.remove(self.temporary_file)

if __name__ == "__main__":
    unittest2.main()
