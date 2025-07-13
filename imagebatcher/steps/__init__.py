from .resize import process as resize
from .grayscale import process as grayscale


available_steps = {
    "resize": resize,
    "grayscale": grayscale
}