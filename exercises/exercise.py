
import sys

sys.path.insert(1,sys.path[0]+r"/..")

from landmarkInfo import *


class Exercise:
    '''
    Exercise Class that is used to create new exercises by creating the subclasses of this class.
    '''
    def __init__(self) -> None:
        print("Creating Exercise.")
        self.landmarkInfo = LandmarkInfo()

    def evaluate(self) : 
        print("This evaluate method of template exercise.")
        return True

if __name__ == "__main__" :
    exe = Exercise()
    exe.evaluate()