from PIL import Image
import numpy as np
import os
np_array = np.array([])
for f in os.listdir('.'):
    if f.endswith('png'):
        np_array = np.append(np_array,f)
print(np_array)
for i in range(len(np_array)):
    pic1 = Image.open(np_array[i])
    pic1 = pic1.resize((500,500))
    pic1.show()