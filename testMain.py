import sys

sys.path.insert(0 , sys.path[0] + '/exercises')

from videoProcessing import *
from exercises.sample1 import ArmStretch

vc = VideoProcessing()
vc.exercise = ArmStretch()
vc.capture()




