from flask import Flask, request, Response ,jsonify, send_file
from dependency_injector.wiring import inject, Provide
from FileService import FileService
from containers import Container
import os

#@app.route('/')
def hello():
    return 'flask app is working'

#@app.route('/picture', methods=['POST'])
@inject
def uploadPicture(file_service: FileService = Provide[Container.fileService]):

    # check file is exist
    if 'file' in request.files:
        pic = request.files['file']
    else:
        Response = jsonify(dict(msg='file is not found in POST request'))
        Response.status_code = 400    
        return Response

    # check file is valid    
    if file_service.isValidFile(pic.filename,'P'):
        return jsonify(file_service.savePicture(pic))
    else :
        Response = jsonify(dict(msg='file is not a picture'))
        Response.status_code = 400 
        return Response

#@app.route('/zip', methods=['POST'])
@inject
def uploadZip(file_service: FileService = Provide[Container.fileService]):

    zip = None

    # check file is exist
    if 'file' in request.files:
        pic = request.files['file']
    else:    
        Response = jsonify(dict(msg='file is not found in POST request'))
        Response.status_code = 400    
        return Response

    # check file is valid    
    if file_service.isValidFile(pic.filename,'Z'):
        return jsonify(file_service.handleZipPicture(pic))
    else :
        Response = jsonify(dict(msg='file is not a zip'))
        Response.status_code = 400 
        return Response


#@app.route('/thumbnail', methods=['POST'])
def uploadThumbnail(file_service: FileService = Provide[Container.fileService]):

    # check file is exist
    if 'file' in request.files:
        pic = request.files['file']
    else:    
        Response = jsonify(dict(msg='file is not found in POST request'))
        Response.status_code = 400    
        return Response

    # check file is valid    
    if file_service.isValidFile(pic.filename,'P'):
        return jsonify(file_service.saveThumbnails(pic))
    else :
        Response = jsonify(dict(msg='file is not a picture'))
        Response.status_code = 400 
        return Response

def getPicture():
    pictureName = request.args.get("picture_name")
    if pictureName :
        if os.path.isfile('img/'+pictureName):     
            return send_file('img/'+pictureName)
        else :
            Response = jsonify(dict(msg='picture is not found'))
            Response.status_code = 404
            return Response    
    else :
        Response = jsonify(dict(msg='picture_name parameter is empty'))
        Response.status_code = 400
        return Response 

        


