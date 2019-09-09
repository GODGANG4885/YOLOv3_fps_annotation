## Quick Start
Download YOLOv3 or tiny_yolov3 weights from YOLO website.Then convert the Darknet YOLO model to a Keras model. Or use what i had converted https://drive.google.com/file/d/1uvXFacPnrSMw6ldWTyLLjGLETlEsUvcE/view?usp=sharing (yolo.h5 model file with tf-1.4.0) , put it into model_data folder

Run YOLO_DEEP_SORT with cmd :

```python yolo_frame_slice.py```  
(Optional) Convert the Darknet YOLO model to a Keras model by yourself:

 please download the weights at first from yolo website. 
 ```python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5```  
Dependencies
The code is compatible with Python 2.7 and 3. The following dependencies are needed to run the tracker:

```NumPy
sklean
OpenCV
Pillow```
Additionally, feature generation requires TensorFlow-1.4.0.
