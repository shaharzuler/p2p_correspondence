import os
import json
from typing import Dict
import pkg_resources

def _get_config(json_path:str) -> Dict:
    package_name = __name__.split('.')[0]
    file_path = pkg_resources.resource_filename(package_name, json_path)
    with open(file_path) as file:
        args = json.load(file)
    return args

def get_default_config() -> Dict:
    json_path = os.path.join('src','default_config.json')
    args = _get_config(json_path)
    return args

def create_output_dir(config):
    exp_dir = f'_n_ev_{config.process_params.n_ev}_n_descr_{config.process_params.n_descr}_descr_type_{config.process_params.descr_type}_nit_{config.zoomout_refine_params.nit}_step_{config.zoomout_refine_params.step}'
    output_dir = os.path.join(config.main_output_dir, config.output_subdir, exp_dir)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir