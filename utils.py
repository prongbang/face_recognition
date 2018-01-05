from PIL import Image
import os, os.path
import numpy

def load_image_from_dir(path):
    """
    Load image path from directory
    """
    index = 0
    imgs_path = []
    valid_images = [".jpg",".gif",".png",".tga"]
    for f in os.listdir(path):
        name = str(os.path.splitext(f)[0])
        ext = str(os.path.splitext(f)[1])
        if ext.lower() not in valid_images:
            continue
        imgs_path.append({
            "index": int(index),
            "name": name,
            "path": os.path.join(path, f)
        })
        index += 1
    return imgs_path

def find_index_from_match(match):
    result = numpy.where(match)[0]
    return result