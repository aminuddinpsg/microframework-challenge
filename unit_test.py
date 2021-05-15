import unittest

from FileService import FileService


class TestFileService(unittest.TestCase):

    def test_createFileNameNotNone(self):
        self.assertIsNotNone(FileService.createFileName(self,fileName='abc.png'))

    def test_createFileNameNone(self):
        self.assertEqual(FileService.createFileName(self,fileName=None), 'fileName is None or Empty')

    def test_createFileNameEmpty(self):
        self.assertEqual(FileService.createFileName(self,fileName=""), 'fileName is None or Empty')

    def test_isValidFileTrue(self):
        self.assertTrue(FileService.isValidFile(self,file='sample.png',type='p'))

    def test_isValidFileFalse(self):
        self.assertFalse(FileService.isValidFile(self,file='sample.pdf',type='P'))

    def test_isValidFileTrueZip(self):
        self.assertTrue(FileService.isValidFile(self,file='sample.zip',type='z'))

    def test_isValidFileFalseZip(self):
        self.assertFalse(FileService.isValidFile(self,file='sample.pdf',type='Z'))        
  
if __name__ == '__main__':
    unittest.main()
    