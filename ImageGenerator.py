from PIL import Image
import numpy as np

data = np.random.randint(255,size=(500,500,3))
image = Image.fromarray(data,mode='RGB')
image.show()
image.save('made.jpg')

