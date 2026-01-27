from pathlib import Path
from base64 import b64encode
import os

# todo: check for better pattern
BASE_DIR = Path(__file__).resolve().parent.parent.parent
WORKSPACE_DEFAULT_FOLDER = BASE_DIR / "workspace" / "default"
RESULTS_FOLDER = BASE_DIR / "out"

class FilepathManager:
    @staticmethod
    def get_out_path(raw_filepath:str, suffix: str):
        filename = Path(raw_filepath).name.split(".")[0]
        extension = '.'.join(Path(raw_filepath).name.split(".")[1:])
        outname = f'{filename}_{suffix}.{extension}'
        out_path = RESULTS_FOLDER / outname
        #print(BASE_DIR)
        abs_out_path = out_path.resolve()
        return str(abs_out_path)
    
    @staticmethod
    def get_base64_str_from_path(file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()                
        # 2. Encode the binary content to Base64
        encoded_content = b64encode(file_content)                
        # 3. Decode the Base64 bytes to a string for JSON serialization
        base64_string = encoded_content.decode('utf-8')     
        return base64_string

 
#r = FilepathManager.get_out_path("C:\\Users\\rmena\\Desktop\\dev\\MRI-prototype-medical-apps\\backend\\workspace\\default\\brain-lesion_T1w.nii.gz", "out")
#r = FilepathManager.get_out_path("/app/workspace/default/brain-lesion_T1w.nii.gz", "out")
#print(r)