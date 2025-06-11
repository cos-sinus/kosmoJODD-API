from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


class RequestFileStorage:
    def upload_file(self, file: FileStorage) -> str:
        file.filename = secure_filename(file.filename)
        path = f"files/{file.filename}"
        file.save(path)
        return path