#!/usr/bin/env python

'''
Lucas-Kanade tracker
====================
Lucas-Kanade sparse optical flow demo. Uses goodFeaturesToTrack
for track initialization and back-tracking for match verification
between frames.
Usage
-----
lk_track.py [<video_source>]
Keys
----
ESC - exit
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
import video
from common import anorm2, draw_str
from time import clock

lk_params = dict( winSize  = (15, 15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.3,
                       minDistance = 400,
                       blockSize = 7 )

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class App:
    def __init__(self, video_src):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = video.create_capture(video_src)
        self.frame_idx = 0
        self.x_coords = []
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def run(self):
        while True:
            _ret, frame = self.cam.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = frame.copy()
            time = self.cam.get(cv2.CAP_PROP_POS_MSEC)*0.001
            face = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
            # print ("Face: ")
            # print (face)

            if len(self.tracks) > 0:
                img0, img1 = self.prev_gray, frame_gray
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                p1, _st, _err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                p0r, _st, _err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                d = abs(p0-p0r).reshape(-1, 2).max(-1)
                good = d < 1
                new_tracks = []
                old_x = 0
                old_time = 0
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    cv2.circle(vis, (x, y), 2, (0, 255, 0), -1)
                    #record tuples of x coords and corresponding time
                    self.x_coords.insert(0,((x,time)))
                    if abs(self.x_coords[0][0]- old_x) < 500 and abs(self.x_coords[0][1] - old_time) > 10:
                        self.x_coords.append((x,time))
                        old_time = time
                        old_x = x
                    else:
                        self.x_coords.pop(0)

                self.tracks = new_tracks
                cv2.polylines(vis, [np.int32(tr) for tr in self.tracks], False, (0, 255, 0))
                draw_str(vis, (20, 20), 'track count: %d' % len(self.tracks))
                # write time
                cv2.putText(vis,"Time: "+ str(time)[:5],(20,60), self.font, 0.5, (0,0,255), 1, cv2.LINE_AA)

            if self.frame_idx < 1:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x, y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)
                print ("frame goodFeaturesToTrack: ")
                print (p)
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        # cv2.putText(vis,"YOOOO: ",(x,y), self.font, 0.5, (255,0,0), 1, cv2.LINE_AA)
                        print ("x, and y: ")
                        print (str(x) + " "+ str(y))
                        self.tracks.append([(x, y)])


            self.frame_idx += 1
            self.prev_gray = frame_gray
            cv2.imshow('lk_track', vis)
            # print(self.x_coords)

            ch = cv2.waitKey(1)
            if ch == 27:
                break

def main():
    import sys
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    print(__doc__)
    App(video_src).run()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()