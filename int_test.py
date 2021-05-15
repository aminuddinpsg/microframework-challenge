from os import close
import unittest
import requests

from FileService import FileService

class TestInterFileService(unittest.TestCase):

    """def test_hello_world(self):
        response = requests.get('http://localhost:8080')
        self.assertEqual(response.text, 'flask app is working')"""

    def test_savePictureWrongFile(self):
        file = open('requirements.txt','rb')
        files = {'file': file}
        response = requests.post('http://localhost:8080/api/picture', files=files)
        self.assertEqual(response.json()['msg'],'file is not a picture')
        file.close()

    def test_savePictureEmpty(self):
        #files = {'file': open('requirements.txt','rb')}
        response = requests.post('http://localhost:8080/api/picture', files=None)
        self.assertEqual(response.json()['msg'],'file is not found in POST request')

    def test_savePicture(self):
        file = open('./test-data/sample.png','rb')
        files = {'file': file}
        response = requests.post('http://localhost:8080/api/picture', files=files)
        self.assertIsNotNone(response.json()['url'])
        file.close()

    def test_saveZip(self):
        file = open('./test-data/multiple.zip','rb')
        files = {'file': file}
        response = requests.post('http://localhost:8080/api/zip', files=files)
        self.assertIsNotNone(response.json()[0]['url'])
        self.assertIsNotNone(response.json()[1]['url'])
        file.close()

    def test_saveThumbnailSmall(self):
        file = open('./test-data/small-sample.png','rb')
        files = {'file': file}
        response = requests.post('http://localhost:8080/api/thumbnail', files=files)
        self.assertIsNotNone(response.json()['url'])
        file.close()

    def test_saveThumbnailBig(self):
        file = open('./test-data/sample.png','rb')
        files = {'file': file}
        response = requests.post('http://localhost:8080/api/thumbnail', files=files)
        self.assertIsNotNone(response.json()[0]['url'])
        self.assertIsNotNone(response.json()[1]['url'])
        file.close()              


if __name__ == '__main__':
    unittest.main()
    