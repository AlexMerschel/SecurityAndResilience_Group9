import math
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import skimage
from PIL import Image, ImageFilter
import cv2
import numpy as nm
from skimage.util import random_noise
import matplotlib.pyplot as plot

# For creating window GUI
window = tkinter.Tk()
window.title("CSC8208- Processing")
window.geometry("300x300+0+0")
window.resizable(0, 0)
window.eval('tk::PlaceWindow . center')
# ---- End Window----
# First layout frame --------


# Heading label and other select file buttons and location label
Label1 = Label(window, text="Welcome to Image Perturbation ", pady=20, justify=LEFT)
Label1.config(font=("Helvetica", 13))
Label1.place(x=30, y=10)
LctnLbl = Label(window, wraplength=300, fg="red")


def browse():
    clear(LctnLbl)
    browseLctn = filedialog.askdirectory(title="Choose Input Folder")
    LctnLbl.configure(text="Source is : " + browseLctn, justify=LEFT)
    LctnLbl.place(x=5, y=220)
    return browseLctn


def clear(type):
    type.configure(text="")


label2 = Label(window, text="Select Operation")
label2.configure(font="Arial 10 underline")
label2.place(x=10, y=80)
Gschkvar = IntVar()
Rtchkvar = IntVar()
Blrchkvar = IntVar()
Dschkvar = IntVar()
Rplchkvar = IntVar()
Gauchkvar = IntVar()
Opxchkvar = IntVar()
GsChkbk = Checkbutton(window, text="Grayscale", variable=Gschkvar, onvalue=1).place(x=20, y=120)
RtChkbk = Checkbutton(window, text="Rotate", variable=Rtchkvar, onvalue=1).place(x=100, y=120)
BlrChkbk = Checkbutton(window, text="Blur", variable=Blrchkvar, onvalue=1).place(x=160, y=120)
DsChkbk = Checkbutton(window, text="Distort", variable=Dschkvar, onvalue=1).place(x=220, y=120)  # crop and blur
RplChkbk = Checkbutton(window, text="Wave", variable=Rplchkvar, onvalue=1).place(x=20, y=150)
GauChkbk = Checkbutton(window, text="S & P", variable=Gauchkvar, onvalue=1).place(x=100, y=150)
OpxChkbk = Checkbutton(window, text="One Pixel", variable=Opxchkvar, onvalue=1).place(x=160, y=150)


def grscl(img):
    grSclimg = img.convert('L')
    return grSclimg


def rotn(img):
    rotated = img.rotate(24)
    return rotated


def blurImg(img):
    blurImage = img.filter(ImageFilter.GaussianBlur(radius=2))
    return blurImage


def CropNblur(img):
    cropImage = img.crop((13, 17, 26, 21))
    cropImage2 = img.crop((31, 1, 35, 15))
    cropNdBlur = cropImage.filter(ImageFilter.GaussianBlur(radius=10))
    cropNdBlur2 = cropImage2.filter(ImageFilter.GaussianBlur(radius=5))
    img.paste(cropNdBlur, (13, 17, 26, 21))
    img.paste(cropNdBlur2, (31, 1, 35, 15))
    return img


def saltNpepper(img, imgNm):
    noisyImgInpt = cv2.imread(img)
    noisyImg = random_noise(noisyImgInpt, mode='s&p', amount=0.5)
    noisyImg = nm.array(255 * noisyImg, dtype='uint8')
    # cv2.imshow('blur', noisyImg)
    cv2.imwrite("Transformed/saltNppr/" + imgNm, noisyImg)
    cv2.waitKey(0)


def wave(img, imgNm):
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape
    WavImg = nm.zeros(img.shape, dtype=img.dtype)

    for i in range(rows):
        for j in range(cols):
            offset_x = int(25.0 * math.sin(2 * 3.14 * i / 260))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i + offset_y < rows and j + offset_x < cols:
                WavImg[i, j] = img[(i + offset_y) % rows, (j + offset_x) % cols]
            else:
                WavImg[i, j] = 0

    cv2.imwrite("Transformed/Ripple/" + imgNm, WavImg)
    cv2.waitKey(0)


def process():
    try:
        BrwsLctn = browse()
        arr = os.listdir(BrwsLctn)
        for i in arr:
            EchImgLctn = BrwsLctn + "/" + i
            img = Image.open(EchImgLctn)
            if Gschkvar.get() == 1:
                img = grscl(img)
            if Rtchkvar.get() == 1:
                img = rotn(img)
            if Blrchkvar.get() == 1:
                img = blurImg(img)
            if Dschkvar.get() == 1:
                img = CropNblur(img)
            if Gauchkvar.get() == 1:
                saltNpepper(EchImgLctn, i)
            if Rplchkvar.get() == 1:
                wave(EchImgLctn, i)
            # img.show()
            if Rplchkvar.get() == 1 or Gauchkvar.get() == 1 or Rplchkvar.get() == 1:
                print("Image stored in directory")
            elif Gschkvar.get() == 1 or Rtchkvar.get() == 1 or Blrchkvar.get() == 1 or Dschkvar.get() == 1:
                img.save("Transformed/Output/" + i)

        DstLbl = Label(window, text="Destination is : Transformed/..", fg="green").place(x=5, y=260)

    except:
        mb.showwarning("Warning", "Please select input folder!!! Try again")


executeBtn = Button(window, text="Process", bg="red", command=process).place(x=200, y=190)

window.mainloop()
