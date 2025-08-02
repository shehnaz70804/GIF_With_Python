import imageio.v3 as iio

filenames = ['pic2.jpg', 'pic3.jpg']
images = [ ]

for filename in filenames:
  path = 'input/'+filename
  images.append(iio.imread(path))

iio.imwrite('output/group.gif', images, duration = 250, loop = 0)