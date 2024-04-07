from easydict import EasyDict

import p2p_correspondence

mesh1_path = "/home/shahar/cardio_corr/my_packages/p2p_correspondence_project/default_output_dir/tmp_data/1014_00/smooth_mesh_1014_00_1.off"
mesh2_path = "/home/shahar/cardio_corr/my_packages/p2p_correspondence_project/default_output_dir/tmp_data/1014_00/smooth_mesh_1014_00_28.off"
config = p2p_correspondence.get_default_config()
config["plots"] = True
config["zoomout_refine_params"]["nit"] = 100
config["main_output_dir"] = "exps_120923_wks1010II"
config["process_params"]["n_ev"] = [10,10]
config["validation"]["mean_l1_flow_th"] = 10

inference_path, flow_is_valid = p2p_correspondence.get_correspondence(mesh1_path, mesh2_path, EasyDict(config))
print(inference_path, flow_is_valid)