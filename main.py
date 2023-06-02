import sys

sys.path.insert(0 , sys.path[0] + '/exercises')

from videoProcessing import *
from exercises.sample1 import ArmStretch
from exercises.lateralRaises2 import LateralRaises
# from exercises.sample3 import legStretch

vc = VideoProcessing()
vc.exercise = LateralRaises()
vc.capture()
