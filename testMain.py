import sys

sys.path.insert(0 , sys.path[0] + '/exercises')

from videoProcessing import *
from exercises.sample1 import ArmStretch
from exercises.lateralRaises import LateralRaises

vc = VideoProcessing()
vc.exercise = LateralRaises()
vc.capture()

