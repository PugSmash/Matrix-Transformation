from PIL import ImageDraw, Image # python image libray which allows the creation of and drawing on images
import numpy as np # numpy stores each of the matricies as arrays
from math import cos, sin # math allows the use of the sine and cosine function
from alive_progress import alive_bar # alive_bar creates a nice progress bar when images are being generated




def matrix_multiplication(matrixA, matrixB):
    """
    - this function does matrix multiplication
    - it is built to multiply 2x2 with a 2x4 matrix
    - incorrect shapes will yield an error
    - it returns a 2x4 matrix
    """
    a = (matrixA[0, 0] * matrixB[0, 0]) + (matrixA[0, 1] * matrixB[1, 0])
    b = (matrixA[0, 0] * matrixB[0, 1]) + (matrixA[0, 1] * matrixB[1, 1])
    c = (matrixA[0, 0] * matrixB[0, 2]) + (matrixA[0, 1] * matrixB[1, 2])
    d = (matrixA[0, 0] * matrixB[0, 3]) + (matrixA[0, 1] * matrixB[1, 3])
    e = (matrixA[1, 0] * matrixB[0, 0]) + (matrixA[1, 1] * matrixB[1, 0])
    f = (matrixA[1, 0] * matrixB[0, 1]) + (matrixA[1, 1] * matrixB[1, 1])
    g = (matrixA[1, 0] * matrixB[0, 2]) + (matrixA[1, 1] * matrixB[1, 2])
    h = (matrixA[1, 0] * matrixB[0, 3]) + (matrixA[1, 1] * matrixB[1, 3])
    return np.array([[a, b, c, d], [e, f, g, h]]).reshape(2, 4)

def matrix_addition(matrixA, matrixB):
    """
    - this function performs matrix addition
    - it takes in 2 parameters - matrixA and matrixB
    - both must be 2x2 matricies
    - it returns a 2x2 matrix
    """
    a = matrixA[0, 0] + matrixB[0, 0]
    b = matrixA[0, 1] + matrixB[0, 1]
    c = matrixA[0, 2] + matrixB[0, 1]
    d = matrixA[0, 3] + matrixB[0, 1]
    e = matrixA[1, 0] + matrixB[1, 0]
    f = matrixA[1, 1] + matrixB[1, 1]
    g = matrixA[1, 2] + matrixB[1, 2]
    h = matrixA[1, 3] + matrixB[1, 3]
    return np.array([[a, b, c, d], [e, f, g, h]]).reshape(2, 4)

# this creates a nes 500x500 blank image
img = Image.new("RGB", (500, 500), "white")
# this creates a draw object that can draw on the image just created
draw = ImageDraw.Draw(img)
# shape is the original shape and its coordinates are (0, 0), (100, 0), (100, 100), (0, 100)
# it is reshaped to 2x4 to allow foir both matrix addition and multiplication
# it is initialised around the origin to make the rotaion work (see mathematics section in documentation)
shape = np.array([[0, 100, 100, 0], [0, 0, 100, 100]]).reshape(2, 4)
# the translation matix translates the square to the centre of the screen
translation_matrix = np.array([[250, 250, 250, 250], [250, 250, 250, 250]])
# this is the list that will contain each individual image
images = []

def set_up_img():
    """
    - this function resets the image by drawing a white rectange over it
    - the axis are also drawn with both lines 
    """
    draw.rectangle(((0,0),(500, 500)), fill="white")
    draw.line(((250, 0), (250, 500)), fill="black")
    draw.line(((0, 250), (500, 250)), fill="black")

def draw_shape(A_img, B_img, C_img, D_img):
    """
    - this function draws the sqaure every time based on the 4 points provided to it
    - the outline of the square is blue
    """
    draw.polygon([A_img, B_img, C_img, D_img], outline="blue")

set_up_img()

def rotate_shape(theta, shape):
    """
    - this function rotates the square useing the transformation matrix for anti-clockwise rotation (see mathematics section on the docs)
    """
    transformation_matrix = np.array([[(cos(theta)), (sin(theta))], [(-1*sin(theta)), (cos(theta))]])
    return matrix_multiplication(transformation_matrix, shape)

with alive_bar(3600, bar = 'smooth', spinner = 'waves') as bar:
    for i in range(3600):
        shape = rotate_shape(1/10, shape)
        shape_translated = matrix_addition(shape, translation_matrix)
        draw_shape((shape_translated[0, 0], shape_translated[1, 0]), (shape_translated[0, 1], shape_translated[1, 1]), (shape_translated[0, 2], shape_translated[1, 2]), (shape_translated[0, 3], shape_translated[1, 3]))
        images.append(img.convert("HSV"))
        set_up_img()
        bar()

images[0].save("Square_Rotation1.gif", append_images=images, save_all=True, duration=0.1, loop=0, optimize=True)


