import os
import numpy as np
import h5py
from pyFM.functional import FunctionalMapping


def get_cmap(vertices):
    min_coord,max_coord = np.min(vertices,axis=0,keepdims=True),np.max(vertices,axis=0,keepdims=True)
    cmap = (vertices-min_coord)/(max_coord-min_coord)
    return cmap

def fit_basic_model(config, mesh1, mesh2):
    model = FunctionalMapping(mesh1, mesh2)
    model.preprocess(**config.process_params, verbose=True)
    model.fit(**config.fm_fit_params, verbose=True)
    p2p_21 = model.get_p2p(n_jobs=1)
    return model, p2p_21

def fit_and_pred_zoomout(config, mesh1, mesh2, output_dir, model):
    model.zoomout_refine(**config.zoomout_refine_params)
    p2p_21_zo = model.get_p2p()
    p = np.zeros((mesh2.n_vertices, mesh1.n_vertices))
    p[np.arange(mesh2.n_vertices),p2p_21_zo] = 1.
    pred = {'P_normalized':p, 'source':mesh2.vertices, 'target':mesh1.vertices}
    inference_filepath = save_inference(output_dir, pred)
    
    return model, p2p_21_zo, inference_filepath

def get_fm_norm(model):
    fms = model.FM.copy()
    max_=fms.max()
    min_=fms.min()
    fms_norm=(fms-min_)/(max_-min_)
    return (fms_norm*255).astype(int)

def save_inference(output_inference_dir, pred): #TODO add saving of downsampling indices
    os.makedirs(output_inference_dir, exist_ok=True)

    key="18_28" # TEMP TODO
    keys_np = np.array([int(k) for k in key.split("_")])
    filepath = os.path.join(output_inference_dir, "model_inference.hdf5")
    f =  h5py.File(filepath, 'a')

    f.create_dataset(name=f"p_{key}",      data=(pred["P_normalized"]), compression="gzip")
    f.create_dataset(name=f"source_{key}", data=(pred["source"]),       compression="gzip")
    f.create_dataset(name=f"target_{key}", data=(pred["target"]),       compression="gzip")
    f.create_dataset(name=f"key",          data=keys_np,                compression="gzip")

    f.close()

    return filepath