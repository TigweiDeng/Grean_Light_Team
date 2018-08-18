
from Const import *

class unitClass:

    coefficient = 1

    def __init__(self, parameterUnitIndex = 0, resultUnitIndex = 0):
        self.coefficient = Coefficient**parameterUnitIndex/Coefficient**resultUnitIndex

