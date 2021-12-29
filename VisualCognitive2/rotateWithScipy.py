import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

# img = scipy.misc.lena()
img = scipy.misc.face()  # lena is not included in scipy 0.19.1
plt.figure(figsize=(12, 2))

for degree in range(5):
    plt.subplot(151+degree)
    rotated_img = ndimage.rotate(img, degree*60, cval=255)
    print(rotated_img.shape)
    plt.imshow(rotated_img, cmap=plt.cm.gray)
    plt.axis('off')

plt.show()