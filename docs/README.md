---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e15-4yp-nearIR-spectroscopy
title: NearIR Spectroscopy
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Project Title

#### Team

- E/15/383, Keshara Weerasinghe, [email](mailto:keshara2032@gmail.com)
- E/15/349, Shamal Tennakoon, [email](mailto:shamal.ten@gmail.com)
- E/15/188, Nithya Kularatne, [email](mailto:e15188@eng.pdn.ac.lk)

#### Supervisors

- Dr. Isuru Nawinne, [email](mailto:isurunawinne@eng.pdn.ac.lk)
- Prof. Roshan Ragel, [email](mailto:roshanr@eng.pdn.ac.lk)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

---

## Abstract
Near-Infrared spectroscopy is used for better vein visualization to make the venipuncture
process more efficient. While there exist a few models which use the said mechanism,
these models are costly, have accuracy issues, and are limited only to certain types of
skin tones. Some of the available devices use image-guided venipuncture technique and
the others use projection . We propose a low-cost mechanism of obtaining near-infrared
spectroscopy by using the image-guided technique after assessing both the available
techniques, optimizing the image processing algorithms and adjusting the illumination
method. The algorithms are still being tested and are in the process of getting optimized.
We use near-infrared LEDs as the source of illumination, and a CMOS camera for
image acquisition. Images are processed using OpenCV, and Histogram equalization and
CLAHE algorithms are used in preprocessing. We are still in the process of optimizing
further. We display the vein map on a 7 inch IPS LCD screen. We are continuing to test
and improve the model to output highly accurate results in a more efficient manner.


## Related works

## Methodology

### 3.1 Conceptual design
Our task is to design and develop a device capable of detecting veins belonging to a
particular region and display them on a portable screen accurately. The entire process –
detection and display occur in real-time. The overall architecture of the system can be
divided into a few basic sub-components.

#### 3.1.1 Identifying the optimum wave length for lighting and obtain the appropriate light sources
We obtained a variety of different sources of the near IR region. Here, we determine
parameters such as the optimum wavelength, intensity, and lighting conditions such as
the environment where image capturing should occur and the placement of the object.
This step is a prerequisite for image capturing.

#### 3.1.2 Image capturing
Once the light sources were selected, we proceeded with the capturing of images. For this purpose, we use a modified CMOS camera and, with the help of the light source, illuminate the object of interest and capture it. Later on, we progress to capturing a live stream instead of a still image.

#### 3.1.3 Preprocessing of the images
Once an image is acquired, preprocessing steps are applied. These steps utilize image
processing techniques to enhance the region of interest in a captured image (for example, the vein pattern in hand). The main objective is to create a visible contrast between
the Region of Interest and its surroundings. The same preprocessing procedures are implemented for video capturing as well.

#### 3.1.4 Applying a formulated algorithm to clearly visualize and extract the vein patterns
After preprocessing, we focus on extracting the region of interest from the image. Here, we isolate only the vein pattern from the body part captured in the image and that will be used as the image that is displayed on the screen. This task is a bit complex as we need to develop an algorithm that is capable of performing this task both efficiently and accurately. The algorithm contains several fundamental steps that are discussed under the methodological approach and extensively under the Implementation section.

#### 3.1.5 Designing a interface to display the live stream obtained from the camera
A user interface is created in order to display the live video stream captured from the image sensor. It is capable of showing the video footage that has gone through image processing to clearly portray the veins real time. More details regarding this is stated under the implementation segment.

### 3.2 Methodological approach
We were able to assemble pieces of hardware to form a fully functioning hardware setup which captures the image and feeds it to a microprocessor where all the image processing
in handled, and is displayed on the screen in real-time. Analyzing the results and further improvements based on the results are yet to be completed.

#### 3.2.1 Hardware setup, modifications and assembly
NIR light source – These light sources fall under 760 – 940 nm waveband and the emitted light is absorbed by deoxygenated hemoglobin that circulates within the peripheral veins.
Attention is given to the arrangement of the NIR LEDs, the number of LEDs used, their positioning and distance. In our setup they are fixed in concentric circles with the camera
located at the center of the circle. The wavelength of a NIR source can be precisely measured with the use of a spectrometer which we were able to build and calibrate. 
Image sensor – This part of the setup captures the image that is illuminated by the light source. The image sensor that we are using currently is a NOIR image sensor that has no IR filter attached to it. The sensor captures an image of the object that is illuminated by the NIR sources and the resulting image displays highlighted (mildly) vein patterns. A high-pass filter is used to cutoff the radiation below 750 nm.
Microprocessor – This is where the processing of the acquired image takes place. A raspberry pi 3 is used, and all the hardware components are interfaced with it. The image processing is executed by the microprocessor and the result is sent to be streamed live that will be displayed on the screen.
Image display – The Image that is acquired and processed, is displayed on a 7 inch IPS LCD panel so that the phlebotomist can be guided by showing the positions of the veins accurately.

#### 3.2.2 Image processing
Image processing is performing operations on an image/set of images to get an enhanced image or to extract some useful information from it. Our objective is to use image processing techniques to identify the vein patterns of an image and its extraction. The Open CV python package along with some basic applications of machine learning (classification and clustering algorithms) are used for vein detection and extraction. The entire process comprises of 3 important phases.
• Background removal : This is the initial phase. For our application, we need only the region of the hand (or some specific body part) where veins are located, and the rest can be considered as noise and therefore eliminated. More details on how this is implemented is discussed under implementation section.
• Preprocessing : This is the initial phase where the raw image is enhanced to show the vein patterns clearly with comparison to the tissue. More details on how this is implemented is discussed under implementation section.
• Algorithm Development and Optimization : This is the most crucial phase of the entire process. It involves developing an algorithm to distinguish and derive the vein pattern from the image with a good accuracy. The general functionality of the algorithm can be expressed by following elementary steps.
1. Eliminate the background of the image and isolate only the region of interest
2. Increase the contrast of the image with the use of histogram equalization and CLAHE algorithm
3. Use morphological transformations on the resulting image to tone down lines and edges.
4. Smoothen and noise reduction using techniques such as median blur, bilateral filters.
5. Segregate the pixels of the image into clusters based on the color of each pixel. Colors are assigned to each cluster to help identify and distinguish the components of the image from one another.
6. Use Edge detection to separate the vein patterns - canny edge detection, Laplacian gradients, Sobel combined.
7. Use adaptive thresholding to get the processed image.
8. Separate the vein from the processed image, color them, and overlay the pattern onto the original image to see a clear and contrasting vein pattern.


### 3.3 Assumptions and constraints
Some problems arose when trying to find/verify the wavelength of the IR sources with
the spectrometer and we were not able buy a variety of sources with different wave
lengths due to the prevailing situation of the country. Therefore, we assumed that the
wavelength of the sources that we currently have are accurate.
Since the NOIR image sensor has no IR filter, it acquires all bands of light instead
of just IR which affects the contrast of the image that is due to undergo processing.
Therefore, we use a high-pass filter so that only the radiation above 750 nm is allowed to
pass through.
When trying to remove the background of an image, the current implementation relies
on the color of each pixel to identify possible edges from the changes in the hsv values
(hue, saturation, value). This approach might result in part of the region of interest being
removed along with the background. Also it is quite difficult to automate this process
where the program implicitly detects the region of interest and detaches the remaining
part.
During the pre-processing stage of an image CLAHE contrasting algorithm is used to
increase the contrast. This results in spots or color marks on the image which are not
veins, to be enhanced as well. Therefore, we are trying to increase the contrast of only
the vein pattern while the rest of the image remains as it is.

## Experiment Setup and Implementation

## Results and Analysis

## Conclusion and Future Work
As of now, we have managed to create a prototype for image capturing, perform preprocessing on the image, and finally construct an algorithm to obtain an output that shows
the vein patterns. Shortly, we expect to improve the algorithm to provide a clearer and more accurate depiction of the vein map. Considering the hardware implementation, we
have developed a prototype by embedding the camera module, near-infrared light sources, single-board computer, and the display screen. The device is ready for testing and we
will start the evaluation shortly. Further improving the algorithms and fine-tuning the device will also be done during the project.

## Publications
1. [Semester 7 report](./)
2. [Semester 7 slides](./)
3. [Semester 8 report](./)
4. [Semester 8 slides](./)
5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./).


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e15-4yp-nearIR-spectroscopy)
- [Project Page](https://cepdnaclk.github.io/e15-4yp-nearIR-spectroscopy/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
