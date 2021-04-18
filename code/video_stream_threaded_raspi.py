from tkinter import *
from PIL import ImageTk
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter.ttk as ttk
from skimage import io, exposure, data, filters, morphology
from skimage.color import rgb2gray as cvtGrayImage
from skimage.util import img_as_ubyte
from threading import Thread
import time
import os


def splitFrame(frame):
    frameSegments = []
    dimensions = frame.shape

    height = dimensions[0]

    segmentHeight = int(height / 3)

    for x in range(0, 3):
        if(x < 2):
            frameSegment = frame[x * segmentHeight:(x + 1) * segmentHeight, :]
        else:
            frameSegment = frame[x * segmentHeight:height, :]

        frameSegments.append(frameSegment)

    return frameSegments


def joinFrames(frame1, frame2, frame3):
    tempFrame = np.concatenate((frame2, frame3), axis=0)

    joinedFrame = np.concatenate((frame1, tempFrame), axis=0)

    return joinedFrame


def mapToScale(val):
    scaledVal = val / 100
    return scaledVal


def showResult(frame):
    breakFlag = False

    cv2.imshow('result', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        breakFlag = True

    return breakFlag


def saveFrame():
    global saveCount
    global capturedFrame

    saveCount += 1

    filePath = "Saved Images/save" + str(saveCount) + ".jpg"

    cv2.imwrite(filePath, capturedFrame)

    timestamp = os.path.getctime(filePath)

    timestamp_str = time.ctime(timestamp)

    timestamp_obj = time.strptime(timestamp_str)

    timeFormat = time.strftime("%Y-%m-%d %H:%M:%S", timestamp_obj)
    timeFormat = timeFormat.replace(":", "꞉")

    os.rename(filePath, os.path.split(filePath)[0] + '/' + timeFormat + os.path.splitext(filePath)[1])


def changeColor(frame):
    dimensions = frame.shape

    temp_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):

            [b, g, r] = temp_frame[i, j]

            if(b == 0 and g == 0 and r == 0):
                temp_frame[i, j] = (113, 179, 60)
            else:
                temp_frame[i, j] = (255, 255, 255)

    return temp_frame


def defaultVideoStream(threadName, threadID):
    frameSegment = splitFrames[threadID]

    splitFrames[threadID] = frameSegment


def createEqualizedStream(threadName, threadID):
    global contrastLimit

    scaledVal = mapToScale(contrastLimit[0])

    frameSegment = splitFrames[threadID]

    frameSegment = cv2.cvtColor(frameSegment, cv2.COLOR_BGR2RGB)

    grayScale = cvtGrayImage(frameSegment)

    # equalized_frame = exposure.equalize_hist(grayScale)

    equalized_frame_adapt = exposure.equalize_adapthist(grayScale, clip_limit=scaledVal)

    equalized_frame_adapt = img_as_ubyte(equalized_frame_adapt)

    splitFrames[threadID] = equalized_frame_adapt


def createConstrastedStream(threadName, threadID):
    global contrastLimit

    frameSegment = splitFrames[threadID]

    grayScale = cv2.cvtColor(frameSegment, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=contrastLimit[0], tileGridSize=(16, 16))
    clahe_frame = clahe.apply(grayScale)

    splitFrames[threadID] = clahe_frame


def createProcessedStream(threadName, threadID):
    global contrastLimit

    frameSegment = splitFrames[threadID]

    grayScale = cv2.cvtColor(frameSegment, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=contrastLimit[0], tileGridSize=(16, 16))
    clahe_frame = clahe.apply(grayScale)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(clahe_frame, kernel, iterations=1)

    adaptive_threshold = cv2.adaptiveThreshold(dilation, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)

    kernel_Morph = np.ones((3, 3), np.uint8)
    closing_thresh = cv2.morphologyEx(adaptive_threshold, cv2.MORPH_CLOSE, kernel_Morph)

    processed_frame = closing_thresh

    splitFrames[threadID] = processed_frame


def createColoredStream(threadName, threadID):
    global contrastLimit

    frameSegment = splitFrames[threadID]

    grayScale = cv2.cvtColor(frameSegment, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=contrastLimit[0], tileGridSize=(16, 16))
    clahe_frame = clahe.apply(grayScale)

    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(clahe_frame, kernel, iterations=1)

    adaptive_threshold = cv2.adaptiveThreshold(dilation, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 7)

    kernel_Morph = np.ones((3, 3), np.uint8)
    closing_thresh = cv2.morphologyEx(adaptive_threshold, cv2.MORPH_CLOSE, kernel_Morph)

    processed_frame = closing_thresh

    colored_frame = changeColor(processed_frame)

    splitFrames[threadID] = colored_frame


def slide(value):
    mode = slider.get()
    global label

    if(mode == 0):
        guiMode[0] = 0

    elif(mode == 1):
        guiMode[0] = 1

    elif (mode == 2):
        guiMode[0] = 2

    else:
        guiMode[0] = 3


def changeContrast(value):
    global contrastLimit

    tempVal = trackBar.get()

    if int(tempVal) != tempVal:
        tempVal = round(tempVal)
        tempVal = 5 * round(tempVal / 5)
        trackBar.set(tempVal)

    contrastLimit[0] = tempVal


def kmeans_clustering(frame, no_clusters):
    temp_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    pixel_vals = temp_frame.reshape((-1, 3))
    pixel_vals = np.float32(pixel_vals)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 15, 1.0)

    ret_vals, labels, centers = cv2.kmeans(pixel_vals, no_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    clustered_frame = segmented_data.reshape(temp_frame.shape)
    clustered_frame = cv2.cvtColor(clustered_frame, cv2.COLOR_RGB2GRAY)

    return clustered_frame


def isGrayScale(img):
    temp_img = img.copy()

    dimensions = temp_img.shape

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):

            values = temp_img[i, j]

            if values.size != 1:
                return False

    return True


def plotHistogram(img):

    if(not isGrayScale(img)):
        values = img.mean(axis=2).flatten()

        counts, bins = np.histogram(values, range(257))

        plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
        plt.xlim([-0.5, 255.5])
        # plt.savefig('hist_6.png', dpi=300, bbox_inches='tight')
        plt.show()

    else:
        temp_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        values = temp_img.mean(axis=2).flatten()

        counts, bins = np.histogram(values, range(257))

        plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
        plt.xlim([-0.5, 255.5])
        # plt.savefig('hist_clust_5.png', dpi=300, bbox_inches='tight')
        plt.show()


class myThread(Thread):

    def __init__(self, thread_id, name):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        print(self.name + " created!")

    def run(self):
        print("Starting " + self.name)

        if(guiMode[0] == 0):
            defaultVideoStream(self.name, self.thread_id)
        elif(guiMode[0] == 1):
            createConstrastedStream(self.name, self.thread_id)
        elif (guiMode[0] == 2):
            createProcessedStream(self.name, self.thread_id)
        else:
            createColoredStream(self.name, self.thread_id)

        print("Exiting " + self.name)


root = Tk()

root.title("Equalizer")
root.geometry("500x70")
root.resizable(False, False)
root.attributes('-fullscreen', False)

stream = cv2.VideoCapture(0)

splitFrames = []

guiMode = [0]

# label = Label(root)
# label.grid(row=1, column=0, columnspan=3)
# label.pack()

slider = Scale(root, from_=0, to=3, orient=HORIZONTAL, command=slide)
slider.grid(row=0, column=1, padx=40)
# slider.pack()

trackBar = ttk.Scale(root, from_=0, to=40, orient=HORIZONTAL, variable=IntVar(), length=150)
trackBar.grid(row=0, column=2, padx=40)
trackBar.set(15)
trackBar.bind("<ButtonRelease-1>", changeContrast)

contrastLimit = [trackBar.get()]

saveCount = 0

icon_capture_image = PhotoImage(file=r'Icons/camera.png')
icon_capture_image = icon_capture_image.subsample(22, 22)

btn_capture = Button(root, image=icon_capture_image, command=saveFrame)
btn_capture.grid(row=0, column=0, padx=20, pady=10)

while True:
    root.update_idletasks()
    root.update()

    thread1 = myThread(0, "Thread-1")
    thread2 = myThread(1, "Thread-2")
    thread3 = myThread(2, "Thread-3")

    _, frame = stream.read()

    splitFrames = splitFrame(frame)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    joinedFrame = joinFrames(splitFrames[0], splitFrames[1], splitFrames[2])
    
    capturedFrame = joinedFrame
    
    cv2.imshow('frame', joinedFrame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    
    # joinedFrame = Image.fromarray(joinedFrame)

    # joinedFrameObject = ImageTk.PhotoImage(image=joinedFrame)

    # label.frameObject = joinedFrameObject
    # label.configure(image=joinedFrameObject)

print("Exiting Main Thread")







