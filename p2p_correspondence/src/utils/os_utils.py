import os

def create_output_dir(config):
    exp_dir = f'_n_ev_{config.process_params.n_ev}_n_descr_{config.process_params.n_descr}_descr_type_{config.process_params.descr_type}_nit_{config.zoomout_refine_params.nit}_step_{config.zoomout_refine_params.step}'
    output_dir = os.path.join(config.main_output_dir, config.output_subdir, exp_dir)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir