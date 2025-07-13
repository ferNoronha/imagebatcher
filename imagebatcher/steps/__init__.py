from .resize import process as resize
from .grayscale import process as grayscale
from .autocontrast import process as autocontrast
from .invert import process as invert
from .blur import process as blur
from .threshold import process as threshold
from .erode import process as erode
from .dilate import process as dilate


available_steps = {
    "resize": resize,
    "grayscale": grayscale,
    "autocontrast": autocontrast,
    "invert": invert,
    "blur": blur,
    "threshold": threshold,
    "erode": erode,
    "dilate": dilate
}