# GIF_With_Python
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats. It is cross-platform, runs on Python 3.9+, and is easy to install.

First install the required dependencies(imageio package using pip3 install).
Command: pip3 install imageio

Have the same sized images(same width and height) in the input folder and create output folder for storing the gif.

Now create a file for writing the script "create_gif.py".

imageio.v3.imread() and imageio.v3.imwrite() functions are used. Use imageio.v3 as iio to make the task easier.

iio.imread() is used to read the image

Store the images in a list.

iio.write() is used to make the gif. First argument is where the output should be rendered. Second argument is the list of images. Then the duration is mentioned in milliseconds. loop=0 makes sure the gif runs infinitely.

Run the created script "create_gif.py" using the command: python create_gif.py

The gif is created.