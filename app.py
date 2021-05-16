from flask import Flask

from containers import Container
import controller
from init import initApp

# Initialize app
initApp()

def create_app() -> Flask:
    container = Container()
    container.wire(modules=[controller])
    app = Flask(__name__)
    app.container = container
    app.add_url_rule('/', 'hello', controller.hello)
    app.add_url_rule('/api/picture','picture',controller.uploadPicture,methods=['POST'])
    app.add_url_rule('/api/zip','zip',controller.uploadZip,methods=['POST'])
    app.add_url_rule('/api/thumbnail','thumbnail',controller.uploadThumbnail,methods=['POST'])
      
    return app  