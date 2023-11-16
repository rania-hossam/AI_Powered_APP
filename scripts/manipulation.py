import pickle
from basic_pitch.inference import predict
import numpy as np
import warnings
from skimage import io, transform, color, filters
from skimage.filters import roberts, scharr, prewitt, sobel

dims = (140, 90)

def image_manipulation(imname, imview=False):
    dims = (140, 90)
    warnings.filterwarnings('ignore')
    print(imname)
    img_raw = io.imread(imname)

    # Convert RGBA to RGB
    if img_raw.shape[2] == 4:
        img_raw = color.rgba2rgb(img_raw)

    downscaled = transform.resize(img_raw, (dims[0], dims[1]))  # Downscale image
    gray = filters.sobel(color.rgb2gray(downscaled))
    edge_roberts = roberts(gray)
    edge_scharr = scharr(gray)
    edge_prewitt = prewitt(gray)
    edge_sobel = sobel(gray)
    diff_scharr_sobel = edge_roberts - edge_sobel

    if imview:
        io.imshow(diff_scharr_sobel)
        io.show()

    warnings.filterwarnings('always')
    return diff_scharr_sobel



