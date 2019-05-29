# 3D face reconstruction from low-resolution images
#### Angelo Garangau Menezes - N°USP: 11413492

### Abstract:

Since the introduction of models that could reconstruct the dense 3D geometry of a face from a single image, there has been a trend in academia for models that could enhance this capability in high-resolution scenarios. However, the reconstruction event is also important for situations where images in low-resolution are the majority, such as in general surveillance.  
This project aims at the development of a 3D face reconstruction model from a single low-resolution image using advances in volumetric convolutional neural networks regression and generative models. 

The project can be divided in two steps:

### 1) Super-Resolution

Super-resolution techniques are going to be applied to the images in order to have enhanced version which could have enough details for the reconstruction step. For this part, different iterative and learning based techniques (e.g., bicubic interpolation, pixel-CNN, SRGAN) are going to be compared based on their peak-signal noise ratio (PSNR) and structural similarity (SSIM)

### 2) 3D Face Reconstruction

Reconstruction phase is going to be applied using models based on volumetric convolutional neural networks for regression of points in the mesh.

### Dataset: A low-resolution version of the 300 W-LP dataset (http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm).

The 300 W-LP dataset has been produced by fitting a 3D morphable model to unconstrained images of the 300W large pose dataset using a multi-feature fitting approach. Face profiling was then used to render each image to 10-15 different poses resulting in over 60,000 2D facial images to 3D mesh. In order to provide a mapping from 2D low-resolution images to these 3D models, the original 2D images are going to be resized and then up-scaled using bilinear interpolation.



