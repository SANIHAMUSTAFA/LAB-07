from astropy.io import fits
import matplotlib.pyplot as plt
from skimage import exposure

# Open a FITS file
hdulist = fits.open(r'E:\Saniha\Image Processing\M51\green.fits')

# Access the data in the primary HDU (Header Data Unit)
data = hdulist[0].data
header = hdulist[0].header

# Close the FITS file
hdulist.close()

# Perform histogram equalization to enhance image contrast
data_equalized = exposure.equalize_hist(data)

# Display the equalized image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(data, cmap='Greens')
plt.title('Original Image')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(data_equalized, cmap='Greens')
plt.title('Equalized Image')
plt.colorbar()

plt.tight_layout()
plt.show()
