from p2p_correspondence.src.main import get_correspondence
from easydict import EasyDict
import json

mesh1_path = "/home/shahar/cardio_corr/outputs/magix/synthetic_dataset100/01/orig/meshes/smooth_mesh.off"
mesh2_path = "/home/shahar/cardio_corr/outputs/magix/synthetic_dataset100/28/orig/meshes/smooth_mesh.off"
with open("/home/shahar/cardio_corr/my_packages/p2p_correspondence_project/p2p_correspondence/p2p_correspondence/src/default_config.json") as f:
    config = EasyDict(json.load(f))

inference_path = get_correspondence(mesh1_path, mesh2_path, config)
print(inference_path)