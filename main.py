import sys

sys.path.insert(0 , sys.path[0] + '/exercises')

from videoProcessing import *
from exercises.bicepCurl import BicepCurls
from exercises.lateralRaises2 import LateralRaises


vc = VideoProcessing()
vc.exercise = LateralRaises(5)
# vc.exercise = BicepCurls(5)
vc.capture()
