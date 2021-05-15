from flask import Flask, request, Response ,jsonify
from dependency_injector.wiring import inject, Provide
from FileService import FileService
from containers import Container


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

