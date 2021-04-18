---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e15-4yp-nearIR-spectroscopy
title: NearIR Spectroscopy
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Near-IR Spectroscopy

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
Near-Infrared spectroscopy is used for better vein visualization to make the venipuncture process more efficient. While there exist a few models which use the said mechanism, these models are costly, have accuracy issues, and are limited only to certain types of skin tones. Some of the available devices use image-guided venipuncture technique and the others use projection.
We propose a low-cost mechanism of obtaining near-infrared spectroscopy by using the image-guided technique. We decided on using this technique after assessing both the available techniques. The low-cost is achieved by optimizing the image processing algorithms and adjusting the illumination method. We have tested and optimized the algorithms accordingly.
We use near-infrared LEDs as the source of illumination, and a CMOS camera for image acquisition. Images are processed using OpenCV, and Histogram equalization and CLAHE algorithms are used in preprocessing. Initially, we processed the still images and later on developed the model to process the live video stream and display the processed video footage that visualizes the veins in real-time. We display the vein map on a 7 inch IPS LCD screen. 

We have tested the prototype using different combinations of light sources with different intensities and have analyzed the results. We have also analyzed how the results vary based on body fat. In order to quantitatively analyze, we have obtained a count of the number of visible veins and depicted the comparison in a graph. We have concluded that a higher intensity does not always increase the visibility of veins. Our plan is to conduct a clinical trial and test the device on human subjects and get the feedback from both the patients and phlebotomists and improve the model so that those final users are satisfied. 

## Methodology

### 3.1 Conceptual design
Our task is to design and develop a device capable of detecting veins belonging to a particular region and display them on a portable screen accurately. The entire process – detection and display occur in real-time. The overall procedure can be divided into a few basic sub-components. 

#### 3.1.1 Identifying the optimum wave length for lighting and obtain the appropriate light sources
We obtained a variety of different sources of the near IR region. Here, we determined parameters such as the optimum wavelength, intensity, 
and lighting conditions, thereby the environment where image capturing should occur and the placement of the object. This step is a prerequisite for image capturing.


#### 3.1.2 Image capturing
Once the light sources were selected, we proceeded with the capturing of images. For this purpose, we use a modified CMOS camera and, with the help of the light source, illuminate the object of interest and capture it.  Later on, we progress to capturing a live stream instead of a still image.

#### 3.1.3 Preprocessing of the images
Once an image is acquired, preprocessing steps are applied. These steps utilize image processing techniques to enhance the region of interest in a captured image (for example, the vein pattern in hand).  The main objective is to create a visible contrast between the Region of Interest and its surroundings. The same preprocessing procedures are implemented for video capturing as well. 

#### 3.1.4 Applying a formulated algorithm to clearly visualize and extract the vein patterns
After preprocessing, we focus on extracting the region of interest from the image. Here, we isolate only the vein pattern from the body part captured in the image and that will be used as the image that is displayed on the screen. This task is a bit complex as we need to develop an algorithm that is capable of performing this task both efficiently and accurately. The algorithm contains several fundamental steps that are discussed under the methodological approach and extensively under the Implementation section.

#### 3.1.5 Designing a interface to display the live stream obtained from the camera
A user interface is created in order to display the live video stream captured from the image sensor. It is capable of showing the video footage that has gone through image processing to clearly portray the veins real time. More details regarding this is stated under the implementation segment.

### 3.2 Methodological approach
We were able to assemble pieces of hardware to form a fully functioning hardware setup which captures the image and feeds it to a microprocessor where all the image processing is handled, and is displayed on the screen in real-time. As a final step we planned to do a clinical trial and get the feedback from the actual final users.

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

## Experimental Setup and Implementation

This section is covered under three main parts: hardware design and implementation, Image processing, and interface design.


### Hardware design and implementation

#### Near-Infrared Spectroscopy to identify veins and display on a screen.

Veins contain oxygenated hemoglobin-rich blood that almost completely absorbs light at near-infrared wavelengths (750 nm–950 nm) up to several millimeters. Using this phenomenon, we can illuminate the skin using infrared-emitting light sources within the specified spectrum and capture the images using an infrared-sensitive image sensor. By further processing of such acquired images, we can extract the vein pattern. We also display the live stream obtained from the camera in order to guide the phlebotomist. He will be shown the detected vein map of the puncture site. He will also be guided by the live stream and will not lose the normal vision on the puncture site by this mechanism. This can resolve many issues faced by venipuncture.

However, depending on the region, skin color, weight the effectiveness of the selected wavelength can vary. Therefore, our study is about coming up with the best wavelength combination and effective image processing algorithm to identify the vein map irrespective of the above conditions. 

Initially, we got 3 light sources emitting at 3 different wavelengths. Namely 750nm, 850nm, and 950nm. Controlling the intensity of these light sources is not a concern at this stage. To verify the light sources that they emit such wavelengths we needed an infrared light spectrometer.
However, such a device was not available to us at that moment. So we planned to build a spectrometer to do our study.

Optical spectrometer is an instrument used to measure properties of light over a specific portion of the electromagnetic spectrum, typically used in spectroscopic analysis to identify materials. The independent variable is usually the wavelength of the light or a unit directly proportional to the photon energy, such as reciprocal centimeters or electron volts, which has a reciprocal relationship to wavelength.
 
A monochromatic light beam that is incident on a grating gives rise to a transmitted beam and various diffracted beams, at angles that depend on the ratio between the distance between the lines of the grating and the wavelength of the light. So, if the light beam is composed of multiple wavelengths, the decomposition of the beam into its components is obtained.
 
The light with a longer wavelength is deflected to a larger angle with respect to the incident direction (angle of diffraction ) . For each wavelength more rows can be observed. The number of rows that are counted from the middle line, which is not skewed with respect to the incident beam and is taken as a reference , it is said “order” and is often denoted by the letter m.

The goals of the build were as follows:
 
* item Having at least 5 nm spectral resolution.
* item Covering the entire visible spectral region and the near-infrared spectral region.
* item Low cost and convenience to calibrate.

The initial prototype for the spectrometer was designed using CAD software with the required dimensions and built by using 3D printed parts and was designed using CAD software.
Below are images that show the design of the spectrometer prototype

********8**********************************************************************************

#### Initial prototype for the spectrometer

The key optical principle in a spectrometer is diffraction. The slit was constructed with thin sheets of aluminum with sharpened edges. This allows a very limited amount of light to the sensor as a large amount can overwhelm the sensor and lead to inaccurate readings. To collimate the light, a biconvex lens was kept at its focal length away from the slit. This will ensure the light will enter the diffraction grating in a parallel manner. The diffraction grating is really important in this setup. Initially, we were not able to get ahold of quality diffraction grating. So we carefully removed the diffraction material in the DVD disk and used it in our first attempt.

However, our first attempt was not successful because the DVD did not serve well as a true diffraction grating inside the first prototype. Moreover, a collimating biconvex lens was not included in the first prototype.

We were able to find high quality 1000 lines per mm grating from the Faculty of Science and rebuilt the spectrometer. Therefore, we redesigned the spectrometer with the true diffraction grating and a collimating lens fixed at its proper focal length. The second prototype proved to be much more accurate.

To analyze the light, we used a Logitech C270 image sensor (Web Camera) with its inbuilt IR Filter removed (In order to let the IR light enter the sensor). The software was an open-source software and to calibrate we used a Mercury Lamp which emits specific peak wavelengths at 4 different points and used 2 points to calibrate. The two points used for calibration were Mercury 2: 436 nm and Mercury 3: 546 nm.
 
After calibrating the spectrometer, we analyzed our two IR sources in a controlled environment to avoid unnecessary light entering the spectrometer. The first source used was had a wavelength of 950 nm. The analyzed result gave us a reading of 945 nm and it was satisfactory.
The second source had a nominal wavelength of 850 nm and it was read as 840 nm. This was also acceptable since these light sources were not high-quality ones.

##### Initial prototype to capture images

The prototype was designed to be composed of the following components.

* Light source setup
* IR Sensitive Camera
* Single-Board computer

 
We designed the prototype to be able to hold 3 light sources at a time where each light source can be turned on and off. The light sources were powered with a 12V power supply which provides 5Amps on load. The single-board computer is a Raspberry Pi Model 3. Raspberry Pi is running a Lightweight version of Raspberry Pi OS which is a Debian-based operating system for Raspberry Pi. OpenCV was compiled and setup on the computer, in order to handle the image processing part of the study. The IR sensitive camera is a product from the same manufacturers of the Raspberry Pi, named NoIR camera which uses a Sony IMX219 image sensor with no inbuilt IR Filters. This is a CMOS sensor. However, CCD works best with Infrared imaging, but, at this point, we could not get ahold of a CCD Sensor.

The prototype is designed so as the height of the camera and light sources are manually adjustable so that we are able to adjust the focus and determine the best distance for proper illumination and capturing images. The camera comes with a fixed focal distance. However, it sits within the region we require.

The light sources can be turned on either individually or as a combination during the image acquiring procedure. Following figure displays the actual prototype with 2 IR light sources namely 940 nm and 850 nm. The images were taken using an IR sensitive camera to see the observe the functionality of IR sources.


********************************************1st prototype photo *************************************8

#### Second prototype to detect and display veins

The second prototype consists of the following components. 

* Light source setup
* IR Sensitive Camera
* Single-Board computer
* Display screen


As the light source, we used 48 LEDs emitting at wavelength of 940nm. We arranged IR LEDs in a circular array. This illumination setup uses a total power of 18W. The intensity of the LEDs is controlled by Pulse Width Modulation (PWM).
We use the same camera we used in the initial prototype with an IR sensitive image sensor - SONY IMX219. A high-pass filter is used so that the radiation above 750 nm is let to pass through and those below that are cut off.
image processing is done on a single board computer raspberry pi 3b which has a Quad Core 1.2GHz Broadcom BCM2837 64bit CPU with a 1GB ram.
We use a 7 inch IPS LCD panel with a resolution of 1024x600 for the display of veins. It is powered by a set of li-ion cells with a capacity of 37Wh.
Following figures give few different views of the second prototype.

#### Final prototype

The final prototype was implemented with suggestions from the medical personnel and considering ease of use and accessibility. The image capturing module was separated from the previous inbuilt design to make it easier for accessing difficult and sensitive venipuncture locations.

Following figure shows an overall view of the final prototype including the image capturing module and display module.

**************************8final prototype photo ***************************************************************

The final prototype consists of the following components and an updated IR source with higher intensity. 

* IR light source
* IR Sensitive Camera
* Optical High Pass filter
* Battery System
* Single-Board computer
* Display screen

The IR source consists of 96 LEDs emitting infrared light at 850 nm with a total power of 18 Watts. If we compare it with the second prototype, it consists of 48 LEDs of 940 nm. After analyzing the intensity and determining the wavelength we decided to go with 96 LEDs of 850 nm.

A closeup view of the final prototype can be seen in below.

8888888888888888888888888888888888 final prototype 88888888888888888888888888888

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
