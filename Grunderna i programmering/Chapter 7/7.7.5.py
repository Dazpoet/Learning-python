#!/usr/bin/env python3

#Make a program that prints a list of volumes for cubes with lenghts equal to range(1,15)

base = width = depth = 0

def calculate_volume(base, width, depth):
    volume = base*width*depth
    return volume

def main():
    print("These are the volumes for cubes with given sides")
    for i in range(1,15):
        v = calculate_volume(i,i,i)
        print("When the sides are all %d m the volume is %d cubic metres" %(i, v))

main()