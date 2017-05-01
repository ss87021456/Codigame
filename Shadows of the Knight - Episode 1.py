import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def contain_(target, words):
    for word in words:
        if word == target:
            return True
    #print "no target", target ,"!"
    return False


# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]

map_x0, map_y0, map_x1, map_y1 = 0, 0, w, h

# game loop
while True:
    bomb_dir = list(raw_input())  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if contain_('U', bomb_dir):
        map_y1 = y0
    elif contain_('D', bomb_dir):
        map_y0 = y0

    if contain_('L', bomb_dir):
        map_x1 = x0
    elif contain_('R', bomb_dir):
        map_x0 = x0

    x0 = map_x0 + (map_x1 - map_x0)/2
    y0 = map_y0 + (map_y1 - map_y0)/2
    print x0, y0
    #print map_x0, map_y0, map_x1, map_y1
        # Write an action using print
        # To debug: print >> sys.stderr, "Debug messages..."


        # the location of the next window Batman should jump to.

