import os
import uuid


class FileSaver:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def save_file(self, text):
        file_id = str(uuid.uuid4())
        file_path = os.path.join(self.storage_path, f"{file_id}.txt")
        with open(file_path, "w") as f:
            f.write(text)
        return file_id
