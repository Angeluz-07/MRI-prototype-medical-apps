import ants
print(f'AntsPy version = {ants.__version__}')
from antspynet.utilities import brain_extraction

def run(raw_img_path):
    raw_img_ants = ants.image_read(raw_img_path, reorient='IAL')
    print("img read...")
    prob_brain_mask = brain_extraction(raw_img_ants,modality="t1",verbose=True)
    print("prob brain mask extracted...")
    brain_mask = ants.get_mask(prob_brain_mask, low_thresh=0.5)
    print("brain mask got...")
    brain_mask.to_file(f"out/test.nii")
    print("brain mask saved...")
