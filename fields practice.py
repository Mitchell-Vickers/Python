#inputs: 
#Length in Yards
#Width in Yards

#Outputs:
# Length in meters
# width in meters
# Area in m^2
#perimeter
#diagonal 

import math
from math import sqrt

length = float(input("what is the length of the field in yards: "))
width = float(input("what is the width of the field in yards: "))

METER_CONVERSION_FACTOR = 0.9144 # 1 Yard * 0.9144 meters/yards = 0.9144 meters

length = length * METER_CONVERSION_FACTOR
width = width * METER_CONVERSION_FACTOR

area = length * width
perimeter = (2 * length) + (2 * width)
diagonal = sqrt(length**2 + width**2)

print("the width is %s meters" % round(width,2))
print("the length is %s meters\n" % round(length,2))
print("the area is %s meters squared" % round(area,2))
print("the peremiter is %s meteres" % round(perimeter,2))
print("the diagonal is %s meters" % round(diagonal,2))
