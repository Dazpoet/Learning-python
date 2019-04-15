#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

def generate_questions():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "\indata.csv"
    
    with open(file_path, newline='') as csvfile:
        indata_lista = [row for row in csv.reader(csvfile)]

    questions = {}

    for i in range(len(indata_lista)):
        questions[i] = tuple(indata_lista[i])
    
    return questions

def main():
    questions = generate_questions()
    print(questions)

if __name__ == "__main__":
    main()