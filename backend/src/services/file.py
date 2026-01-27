from src.repository.file import FileRepository
from src.domain.filepath_manager import WORKSPACE_DEFAULT_FOLDER, FilepathManager, RESULTS_FOLDER

def get_input_files():
    folder_path = WORKSPACE_DEFAULT_FOLDER
    return FileRepository(folder_path).get_all()

def get_input_file_as_base64(file_id):
    folder_path = WORKSPACE_DEFAULT_FOLDER
    file_repository = FileRepository(folder_path)
    file = file_repository.get_by_id(file_id)
    full_path = file_repository.get_full_path(file.name)
    base64_str = FilepathManager.get_base64_str_from_path(full_path)
    return base64_str

def save_input_file(filename, file):
    folder_path = WORKSPACE_DEFAULT_FOLDER
    file_repository = FileRepository(folder_path)
    return file_repository.add_raw(filename, file)

def get_output_files():
    folder_path = RESULTS_FOLDER
    print(folder_path)
    return FileRepository(folder_path).get_all()

def get_output_file_as_base64(file_id):
    folder_path = RESULTS_FOLDER
    file_repository = FileRepository(folder_path)
    file = file_repository.get_by_id(file_id)
    full_path = file_repository.get_full_path(file.name)
    base64_str = FilepathManager.get_base64_str_from_path(full_path)
    return base64_str
