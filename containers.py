from dependency_injector import containers, providers
from FileService import FileService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    fileService = providers.Factory(FileService)