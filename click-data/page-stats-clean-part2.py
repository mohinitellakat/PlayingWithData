# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:37:36 2016

@author: mt34546
"""
import pandas as pd

file_path = raw_input('Enter your filepath here:')

df1 = pd.read_csv(file_path)

class_status_types=("in class", "before class", "after class", "in benchmark", "out of class")
in_class_list = []
out_of_class_list = []
before_class_list = []
after_class_list = []
in_benchmark_list = []

## Put in a boolean value and create an associated column if the class status falls into a class status bucket
for class_status in df1['In Class Status']:
    if class_status == "in class":
        in_class_list.append(1)
        out_of_class_list.append(0)
        before_class_list.append(0)
        after_class_list.append(0)
        in_benchmark_list.append(0)
    elif class_status == "out of class":
        in_class_list.append(0)
        out_of_class_list.append(1)
        before_class_list.append(0)
        after_class_list.append(0)
        in_benchmark_list.append(0)
    elif class_status == "before class":
        in_class_list.append(0)
        out_of_class_list.append(0)
        before_class_list.append(1)
        after_class_list.append(0)
        in_benchmark_list.append(0)
    elif class_status == "after class":
        in_class_list.append(0)
        out_of_class_list.append(0)
        before_class_list.append(0)
        after_class_list.append(1)
        in_benchmark_list.append(0)
    elif class_status == "in benchmark":
        in_class_list.append(0)
        out_of_class_list.append(0)
        before_class_list.append(1)
        after_class_list.append(0)
        in_benchmark_list.append(0)
    else:
        in_class_list.append(0)
        out_of_class_list.append(0)
        before_class_list.append(0)
        after_class_list.append(0)
        in_benchmark_list.append(0)


df1["Class Status: in class"] = in_class_list
df1["Class Status: out of class"] = out_of_class_list
df1["Class Status: before class"] = before_class_list
df1["Class Status: after class"] = after_class_list
df1["Class Status: in benchmark"] = in_benchmark_list

print "done class status indicators"

df1.to_csv('ps-data-clean/ps_data_Fall2015_clean.csv' , index=False)