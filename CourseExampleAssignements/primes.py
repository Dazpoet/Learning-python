#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for n in range (2,25):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)