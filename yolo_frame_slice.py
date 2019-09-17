#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
from timeit import time
import warnings
import cv2
from PIL import Image
from yolo import YOLO


import json
from collections import OrderedDict
warnings.filterwarnings('ignore')


def main(yolo):

    writeVideo_flag = True

    # video_capture = cv2.VideoCapture(0 )
    filename = '/database/fall video/Office/video (9).avi'
    video_capture = cv2.VideoCapture(filename)
    origin_fps = video_capture.get(cv2.CAP_PROP_FPS)
    print("original FPS : {0}".format(origin_fps))
    # json file init
    json_data = OrderedDict()
    json_data["detection"] = []
    if writeVideo_flag:

        json_file = open('detections.json','w',encoding="utf-8")
        frame_index = -1

    fps = 0.0
    while True:
        ret, frame = video_capture.read()  # frame shape 640*480*3
        if ret != True:
            break
        t1 = time.time()

        # image = Image.fromarray(frame)
        image = Image.fromarray(frame[..., ::-1])  # bgr to rgb
        boxs = yolo.detect_image(image)
        frame_index = frame_index + 1
        if not boxs:
            continue

        if writeVideo_flag:


            json_data["detection"].append({"frame": frame_index, "bbox[x,y,w,h]": boxs[0]})



        fps = (fps + (1. / (time.time() - t1))) / 2
        print("fps= %f" % (fps))

        # Press Q to stop!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    if writeVideo_flag:
        json.dump(json_data, json_file, ensure_ascii=False, indent='\t')
        json_file.close()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main(YOLO())
