
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
from astropy.utils.data import download_file
from skimage import filters

# Load FITS image
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
hdulist = fits.open(image_file)
image = hdulist[0].data

# Save FITS image as PNG
plt.imsave('/output/original.png', image, cmap='gray')

# Apply filters
gaussian_image = filters.gaussian(image, sigma=2)
sobel_image = filters.sobel(image)

# Save filtered images as PNGs
plt.imsave('/output/gaussian.png', gaussian_image, cmap='gray')
plt.imsave('/output/sobel.png', sobel_image, cmap='gray')

# Display original and filtered images
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 1].imshow(gaussian_image, cmap='gray')
axs[0, 1].set_title('Gaussian')
axs[1, 0].imshow(sobel_image, cmap='gray')
axs[1, 0].set_title('Sobel')
axs[1, 1].axis('off')

# Save figure as PNG
fig.savefig('/output/filtered.png')
