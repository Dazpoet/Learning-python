#!/usr/bin/env python3

my_string = "hejsan"

index = len(my_string) - 1 #we start our index at the lenght of my_string

while not index == -1: #as long as our index is 0 or greater we continue running, this could've been not index < 0
    print(my_string[index])
    index -= 1 #This is the same as index = index - 1 but shorter