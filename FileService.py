import uuid
import os
import zipfile

from werkzeug.utils import secure_filename
from os import path
from PIL import Image
from flask import request

from init import PIC_DIR

class FileService:

    def __init__(self):
        print ("__instance created")

    def createFileName(self,fileName):
        if str(fileName) and fileName:
            unique =str(uuid.uuid4())
            split = fileName.lower().split(".")
            return split[0]+"-"+unique+"."+split[1]
        else:
            return 'fileName is None or Empty'    


    def isValidFile(self,file,type):
        if ((type.lower() =='P'.lower() and file.lower().
            endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))) or 
            (type.lower() =='Z'.lower() and file.lower().
            endswith(('.zip'))) ):
            return True
        else:
            return False 

    def savePicture(self,pic):
        filename = self.createFileName(secure_filename(pic.filename))
        fullPath = os.path.join(PIC_DIR, filename)
        pic.save(fullPath)
        return dict(url=request.url_root+"api/pic?picture_name="+filename)

    def handleZipPicture(self,file):
        
        # get zipFile
        zip = zipfile.ZipFile(file, 'r')
        fileNameList = zip.namelist()

        # extract zip file
        zip.extractall(PIC_DIR)

        # create respond msg with multiple files
        respond = []
        for filename in fileNameList:
            if self.isValidFile(filename,'P') :
                tempFilePath = os.path.join(PIC_DIR, filename);  
                filename = self.createFileName(secure_filename(filename))
                fullPath = os.path.join(PIC_DIR, filename)
                os.rename(tempFilePath,fullPath)  
                respond.append(dict(url=request.url_root+"api/pic?picture_name="+filename))
            else :
                respond.append(dict(msg=filename+" is not a picture"))
                os.remove(os.path.join(PIC_DIR, filename))    

        return respond

    def saveThumbnails(self,pic):
        image = Image.open(pic)
        width, height = image.size
        
        if(width >= 128 and height >= 128):

            filename = secure_filename(pic.filename)
            firstThumbnail = image.copy()
            secondThumbnail = image.copy()

            # generate unique fileName
            firstFileName = self.createFileName(filename)
            secondFileName = self.createFileName(filename)
            firstFullPath =  os.path.join(PIC_DIR, firstFileName)
            secondFullPath =  os.path.join(PIC_DIR, secondFileName)

            # determine the size
            firstSize = 32, (height/(width/32))
            secondSize = 64, (height/(width/64))

            # create the thumbnails
            firstThumbnail.thumbnail(firstSize,Image.ANTIALIAS)
            secondThumbnail.thumbnail(secondSize,Image.ANTIALIAS)

            #save the thumbnails
            firstThumbnail.save(firstFullPath)
            secondThumbnail.save(secondFullPath)

            # append the urls
            respond = []
            respond.append(dict(url=request.url_root+"api/pic?picture_name="+firstFileName))
            respond.append(dict(url=request.url_root+"api/pic?picture_name="+secondFileName))
            return respond

        else :    
            filename = self.createFileName(secure_filename(pic.filename))
            fullPath = os.path.join(PIC_DIR, filename)
            image.save(fullPath)
            return dict(url=request.url_root+"api/pic?picture_name="+filename)            