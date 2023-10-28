from pyFM.mesh import TriMesh

from .utils.fm_utils import fit_basic_model, fit_and_pred_zoomout, get_fm_norm
from .utils.visualization_utils import double_mesh_plot, plot_cmap, plot_fm
from .utils.os_utils import create_output_dir

def get_correspondence(mesh1_path, mesh2_path, config):
    mesh1 = TriMesh(mesh1_path, area_normalize=config.preprocess.normalize_meshes_area)
    mesh2 = TriMesh(mesh2_path, area_normalize=config.preprocess.normalize_meshes_area)

    output_dir = create_output_dir(config)

    model, p2p_21 = fit_basic_model(config, mesh1, mesh2)

    if config.plots:
        double_mesh_plot(mesh1, mesh2, prefix="clean", output_dir=output_dir)

        plot_cmap(mesh1, mesh2, output_dir, p2p_21, method="FM")
        fms_norm = get_fm_norm(model)
        plot_fm(output_dir, model, fms_norm, "FM")

    model, p2p_21_zo = fit_and_pred_zoomout(config, mesh1, mesh2, output_dir, model)

    if config.plots:
        plot_cmap(mesh1, mesh2, output_dir, p2p_21_zo, method="zoomout")
        fms_norm = get_fm_norm(model)
        plot_fm(output_dir, model, fms_norm, "zoomout")
    
    return output_dir