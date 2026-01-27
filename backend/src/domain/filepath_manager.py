from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RESULTS_PATH = BASE_DIR / "out"

class FilepathManager:
    @staticmethod
    def get_out_path(raw_filepath:str, suffix: str):
        filename = Path(raw_filepath).name.split(".")[0]
        extension = '.'.join(Path(raw_filepath).name.split(".")[1:])
        outname = f'{filename}_{suffix}.{extension}'
        out_path = RESULTS_PATH / outname
        #print(BASE_DIR)
        abs_out_path = out_path.resolve()
        return str(abs_out_path)

#r = FilepathManager.get_out_path("C:\\Users\\rmena\\Desktop\\dev\\MRI-prototype-medical-apps\\backend\\workspace\\default\\brain-lesion_T1w.nii.gz", "out")
#r = FilepathManager.get_out_path("/app/workspace/default/brain-lesion_T1w.nii.gz", "out")
#print(r)