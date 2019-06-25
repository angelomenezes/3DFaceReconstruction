# 3D face reconstruction from low-resolution images
#### Angelo Garangau Menezes - N°USP: 11413492

### Abstract:

Since the introduction of models that could reconstruct the dense 3D geometry of a face from a single image, there has been a trend in academia for models that could enhance this capability in high-resolution scenarios. However, the reconstruction event is also important for situations where images in low-resolution are the majority, such as in general surveillance.
Most of the software that present features related to 3D face reconstruction usually include 3D morphable model fitting which may be computationally expensive and often do not bring enough details, mainly when the image to be used in the first place is a low-resolution one.

This project evaluated different resolution scenarios and explored a deep volumetric regression network to infer 3D depth maps directly of images of faces.

The work performed in this repository can be divided basically into two phases:

### 1) Super-Resolution

Super-resolution techniques were applied to a set of low-resolution images in order to have enhanced versions that could provide enough details for the following reconstruction step.
For the former stage, different neighboorhood and learning based techniques were compared based on their peak-signal noise ratio (PSNR) and structural similarity (SSIM).

### 2) 3D Face Reconstruction

The reconstruction phase was performed by a learning model based on volumetric convolutional neural networks for regression of feature points in the mesh.

### Dataset: 
A low-resolution version of the [300 W-LP dataset](http://www.cbsr.ia.ac.cn/users/xiangyuzhu/projects/3DDFA/main.htm).

### Final Results
[Final_Report.ipynb](https://github.com/angelomenezes/3DFaceReconstruction/blob/master/Final_Report.ipynb)

### References

- Jackson, Aaron S., et al. "Large pose 3D face reconstruction from a single image via direct volumetric CNN regression." Proceedings of the IEEE International Conference on Computer Vision. 2017.
- Shi, Wenzhe, et al. "Real-time single image and video super-resolution using an efficient sub-pixel convolutional neural network." Proceedings of the IEEE conference on computer vision and pattern recognition. 2016.

### Acknowledgements

This repository was highly influenced by the code, ideas and implementations presented in [Alexandru Dino](https://github.com/alexandru-dinu/3D-face-reconstruction), [Aaron Jackson](https://github.com/AaronJackson/vrn), and [Pytorch](https://github.com/pytorch/examples/tree/master/super_resolution) repositories.
