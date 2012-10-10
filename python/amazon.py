#!/usr/bin/python

import os
import re

def find_html(folder):
    x_files = []
    for file in os.listdir(os.path.abspath(folder)):
        with open(file, 'r') as f:
            if re.findall(regex, f.read()):
                x_files.append(file)
    return x_files

