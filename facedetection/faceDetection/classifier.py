import numpy as np
from PIL import Image
import os

def train_classifier(nitesh_dir):
    path = [os.path.join(nitesh_dir, f) for f in os.listdir(nitesh_dir)]
    faces= []
    ids =[] 