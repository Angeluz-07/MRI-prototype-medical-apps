

from src.domain.filepath_manager import FilepathManager

import ants
from antspynet.utilities import brain_extraction
from src.config import CACHE_DIR

def _mask_brain(raw_img_path):
    print(f'AntsPy version = {ants.__version__}')
    print("processing...", raw_img_path)
    raw_img_ants = ants.image_read(raw_img_path, reorient='IAL')
    print("img read...")
    prob_brain_mask = brain_extraction(raw_img_ants,modality="t1",verbose=False, antsxnet_cache_directory=CACHE_DIR) # todo:fix issue of weights being retrieved on running time.
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



def get_implementation(alg_name):
    IMPLEMENTATIONS = {
        "mask_brain" : _mask_brain
    }
    return IMPLEMENTATIONS.get(alg_name)
