"""
Created on June 9th, 2021
@author:    Alireza(Ali) Shamsoshoara
@Project:   Coding Challenge for ResMed
@Northern Arizona University
This project is developed and tested with Python 3.6 using pycharm on Ubuntu 18.04 System
"""

#################################
# Main File
#################################

# ############# import libraries
# General Modules
import numpy as np
from datetime import datetime


def main():
    file_input = open('sample-input-1.txt', 'r')
    all_lines = file_input.readlines()
    for line in all_lines:
        # print(line)
        print(line.strip())
        parts = line.rstrip().split('|')
        date = parts[0]
        value_float = np.float16(parts[1])
        parser_year, parser_month, parser_day = datetime.strptime(date, "%Y-%m-%d").year,\
                                                datetime.strptime(date, "%Y-%m-%d").month,\
                                                datetime.strptime(date, "%Y-%m-%d").day

    pass


if __name__ == "__main__":
    main()
