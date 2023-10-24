import os

import numpy as np
import cv2
from matplotlib import pyplot as plt
import trimesh

from .fm_utils import get_cmap

def plot_mesh(mesh, cmap=None, prefix="",suffix="0",output_dir=''):
    pcd = trimesh.points.PointCloud(mesh.vertices)
    pcd.colors = cmap
    pcd.export(os.path.join(output_dir,f'{prefix}_pcd_{suffix}.obj'))
 
def double_mesh_plot(mesh1, mesh2, cmap1=None, cmap2=None, prefix="", output_dir=''):
    plot_mesh(mesh1, cmap1, prefix, "1",output_dir=output_dir)
    plot_mesh(mesh2, cmap2, prefix, "2",output_dir=output_dir)

def plot_cmap(mesh1, mesh2, output_dir, p2p_21, method=""):
    cmap1 = get_cmap(mesh1.vertlist); 
    cmap2 = cmap1[p2p_21]
    double_mesh_plot(mesh1, mesh2, cmap1, cmap2, prefix=f"after_{method}", output_dir=output_dir)

def plot_fm(output_dir, model, fms_norm, method=""):
    cv2.imwrite(os.path.join(output_dir,f"after_{method}.jpg"), fms_norm)
    plt.imshow(model.FM)
    plt.savefig(os.path.join(output_dir,f"after_{method}_plt.jpg"))
    np.save(os.path.join(output_dir,f"after_{method}.npy"), model.FM)

