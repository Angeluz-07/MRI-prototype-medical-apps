from src.repository.algorithm import InMemoryAlgorithmRepository
from src.repository.file import FileRepository

def get_algorithms():
    return InMemoryAlgorithmRepository().get_all()

def img_process_run(filename):
    img_full_path = FileRepository().get_full_path(filename)
    print(img_full_path)
    _img_process_run(img_full_path)

from src.service.filepath_manager import FilepathManager
import ants
from antspynet.utilities import brain_extraction
def _img_process_run(raw_img_path):
    print(f'AntsPy version = {ants.__version__}')
    print("processing...", raw_img_path)
    raw_img_ants = ants.image_read(raw_img_path, reorient='IAL')
    print("img read...")
    prob_brain_mask = brain_extraction(raw_img_ants,modality="t1",verbose=True) # todo:fix issue of weights being retrieved on running time.
    print("prob brain mask extracted...")
    brain_mask = ants.get_mask(prob_brain_mask, low_thresh=0.5)
    print("brain mask got...")
    out_path =  raw_img_path.split('.')[0] +'_brainMask.nii.gz'
    brain_mask.to_file(out_path)
    print("brain mask saved...")

    print("saving brain masked...")
    masked = ants.mask_image(raw_img_ants, brain_mask)
    out_path= FilepathManager.get_out_path(raw_img_path,'brainMasked')
    print(out_path)
    masked.to_file(out_path)
    print("saved brain masked...")