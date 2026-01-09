from pathlib import Path
import ants
print(f'AntsPy version = {ants.__version__}')
from antspynet.utilities import brain_extraction

def add_suffix_before_extension(file_path_str: str, suffix: str) -> str:
    """
    Adds a suffix before the file extension of a given path.

    Args:
        file_path_str: The original file path as a string.
        suffix: The suffix to be added (e.g., "_new", "-copy").

    Returns:
        The new file path as a string with the suffix added before the extension.
    """
    path_obj = Path(file_path_str)
    # Reconstruct the path with the suffix inserted before the extension
    new_stem = path_obj.stem + suffix
    new_path_obj = path_obj.parent / (new_stem + path_obj.suffix)
    return str(new_path_obj)

def run(raw_img_path):
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
