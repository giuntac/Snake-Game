import unittest2
import os
from configurator import get_attributes


class TestConfigurator(unittest2.TestCase):
    """A testcase is created by subclassing unittest2.TestCase."""

    def setUp(self):
        """Create and access a valid temporary file."""
        self.temporary_file = '/tmp/emptyfile.csv'
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        """Test for a non-existent file."""
        df = get_attributes("/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(df)

    def test_empty_datafile(self):
        """Test for an empty csv file."""
        df = get_attributes(self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        """Test for a file with a wrong format."""
        df = get_attributes(self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
        """Delete the temporary file created in the setUp function."""
        os.remove(self.temporary_file)


if __name__ == "__main__":
    unittest2.main()
