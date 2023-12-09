from pyFM.mesh import TriMesh

from .utils.fm_utils import fit_basic_model, fit_zoomout, get_fm_norm, predict
from .utils.visualization_utils import double_mesh_plot, plot_cmap, plot_fm
from .utils.os_utils import create_output_dir

def get_correspondence(mesh1_path, mesh2_path, config):
    mesh1_norm = TriMesh(mesh1_path, area_normalize=config.preprocess.normalize_meshes_area)
    mesh2_norm = TriMesh(mesh2_path, area_normalize=config.preprocess.normalize_meshes_area)

    mesh1_no_norm = TriMesh(mesh1_path, area_normalize=False)
    mesh2_no_norm = TriMesh(mesh2_path, area_normalize=False)

    output_dir = create_output_dir(config)

    model, p2p_21 = fit_basic_model(config, mesh1_norm, mesh2_norm)

    if config.plots:
        double_mesh_plot(mesh1_no_norm, mesh2_no_norm, prefix="clean", output_dir=output_dir)

        plot_cmap(mesh1_no_norm, mesh2_no_norm, output_dir, p2p_21, method="FM")
        fms_norm = get_fm_norm(model)
        plot_fm(output_dir, model, fms_norm, "FM")

    model, p2p_21_zo = fit_zoomout(config, mesh1_norm, mesh2_norm, output_dir, model)
    mean_l1_flow = predict(mesh1_no_norm, mesh2_no_norm, output_dir, p2p_21_zo, config["validation"]["check_flow"])
    flow_validation = False if mean_l1_flow > config["validation"]["mean_l1_flow_th"] else True
    
    if config.plots:
        plot_cmap(mesh1_no_norm, mesh2_no_norm, output_dir, p2p_21_zo, method="zoomout")
        fms_norm = get_fm_norm(model)
        plot_fm(output_dir, model, fms_norm, "zoomout")
    
    return output_dir, flow_validation

