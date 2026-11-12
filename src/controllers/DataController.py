
from .BaseController import BaseController
from fastapi import  UploadFile
from models import Responsesignal
class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1048576
    def validate_file(self, file: UploadFile):
            if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
                return False, Responsesignal.BAD_REQUEST.value
            if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
                return False, Responsesignal.BAD_REQUEST.value
            return True, Responsesignal.SUCCESS.value
    pass