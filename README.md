# 3D face reconstruction from low-resolution images
#### Angelo Garangau Menezes - N°USP: 11413492

### Abstract:

Since the introduction of models that could reconstruct the dense 3D geometry of a face from a single image, there has been a trend in academia for models that could enhance this capability in high-resolution scenarios. However, the reconstruction event is also important for situations where images in low-resolution are the majority, such as in general surveillance.  
This project aims at the development of a 3D face reconstruction model from a single low-resolution image using advances in volumetric convolutional neural networks regression and generative models. 

The development of this project was divided into two steps:

### 1) Super-Resolution

Super-resolution techniques are going to be applied to the images in order to have enhanced version which may have enough details for the following reconstruction step. For the former, different iterative and learning based techniques (e.g., bicubic interpolation, pixel-CNN, SRGAN) are going to be compared based on their peak-signal noise ratio (PSNR) and structural similarity (SSIM).

### 2) 3D Face Reconstruction

The reconstruction phase is going to be applied using models based on volumetric convolutional neural networks for regression of feature points in the mesh.

### Dataset: A low-resolution version of the 300 W-LP dataset (http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm).

The 300 W-LP dataset has been produced by fitting a 3D morphable model to unconstrained images of the 300W large pose dataset using a multi-feature fitting approach.

- [300W-3D-all](https://drive.google.com/open?id=18W2a-LtUHty0C7jbTOArQV2eY73oicoa)
- [AFLW-2000-3D](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/Database/AFLW2000-3D.zip)

### References

### Acknowledgement 
