import numpy as np
from google.colab import files
from keras.preprocessing import image

uploaded = files.upload()
IMAGE_SIZE = 224
for fn in uploaded.keys():
 
  # predicting images
  path = '/content/' + fn
  img = image.load_img(path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)

  image_tensor = np.vstack([x])

  interpreter.set_tensor(input_index, image_tensor)
  interpreter.invoke()
  predictions = interpreter.get_tensor(output_index)
  classes = np.argmax(predictions)
  print(classes)
  if classes==1:
    print(fn + " is a dog")
  else:
    print(fn + " is a cat")
