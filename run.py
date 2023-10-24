from easydict import EasyDict

import p2p_correspondence

mesh1_path = "/home/shahar/cardio_corr/outputs/magix/synthetic_dataset100/01/orig/meshes/smooth_mesh.off"
mesh2_path = "/home/shahar/cardio_corr/outputs/magix/synthetic_dataset100/28/orig/meshes/smooth_mesh.off"
config = p2p_correspondence.get_default_config()

inference_path = p2p_correspondence.get_correspondence(mesh1_path, mesh2_path, EasyDict(config))
print(inference_path)