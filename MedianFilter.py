import scipy.misc
import scipy.ndimage
from PIL import Image

src = Image.open('images/noisy.png')
out = scipy.ndimage.filters.median_filter(src, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
out = Image.fromarray(out)
out.save('out/median.png')
