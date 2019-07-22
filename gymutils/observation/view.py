import cv2
import numpy as np
from PIL import Image


def _preprocess(observation):
    observation = observation.copy()
    if type(observation) != np.uint8:
        observation = np.uint8(observation)
    if observation.max() <= 1:
        observation *= 255
    return observation


def look(observation):
    Image.fromarray(_preprocess(observation)).show()


def save(observation, path, name, prefix='', suffix='', ext='png'):
    path = "{}/{}{}{}.{}".format(path, prefix, name, suffix, ext)
    Image.fromarray(_preprocess(observation)).save(path)


class Recorder:
    def __init__(self, fps=15, size=(210, 160), path='.', out='out', video_format='mp4v'):
        video_ext = None
        if video_format == 'mp4v':
            video_ext = 'mov'
        elif video_format in ['MP4V', 'H264']:
            video_ext = 'mp4'

        size = (size[1], size[0])
        out = "{}/{}.{}".format(path, out, video_ext)
        fourcc = cv2.VideoWriter_fourcc(*video_format)
        self.recorder = cv2.VideoWriter(out, fourcc, fps, size)

    def record(self, observation, cvt_color=True):
        frame = cv2.cvtColor(observation, cv2.COLOR_RGB2BGR) if cvt_color else observation
        self.recorder.write(frame)

    def stop(self):
        self.recorder.release()
    
    def __del__(self):
        self.stop()
