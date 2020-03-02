import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

# One pixel perturbation



# read the image
image=io.imread("E:/Newcastle/Advanced Computer Science/Research Method/Task/Image/First.jpg")

image1=io.imread("E:/Newcastle/Advanced Computer Science/Research Method/Task/Image/Speed.jpg")

# Change the pixel
def Pertubation(pixel,imag):

    # This is to batch images
    # tile=[1]*4
    # imags=np.tile(imag,tile)
    # for c,image in zip(pixel,imags):
    #
    # # x is row
    # # y is column
    # # rgb is value of one pixel
    #     x,y,*rgb=c
    #     image[x,y]=rgb


    # This is to process one image
    # x is row
    # y is column
    # rgb is value of one pixel
    x, y, *rgb = pixel
    imag[x, y] = rgb

    return imag

if __name__=="__main__":

    # For batch
    # pixs=[]
    # pixel = [20, 20, 225, 255, 0]
    # pixs=pixs.append(pixel)
    # after_per=Pertubation(pixel,image)


    # For one image
    pixel = [20, 20, 0, 0, 0]
    after_per=Pertubation(pixel,image)
    io.imshow(after_per)
    plt.show()
    # save the image after perturbation, the format need to be png
    io.imsave('E:/Newcastle/Advanced Computer Science/Research Method/Task/Image/new5.png', after_per)
