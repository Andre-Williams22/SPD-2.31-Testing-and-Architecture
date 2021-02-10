# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
circle_x = 4
circle_y = 4.25

circle2_x = 53
circle2_y = -5.35

def circle_distances(circle_x, circle_y, circle2_x, circle2_y):
    # Calculate the distance between the two circle
    distance = math.sqrt((circle_x-circle2_x)**2 + (circle_y - circle2_y)**2)
    print('distance', distance)
    

# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91

def vector_lengths(xa, ya, xb, yb):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    print('length', length)


print(vector_lengths(xa, ya, xb, yb))
print(circle_distances(circle_x, circle_y, circle2_x, circle2_y))