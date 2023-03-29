import os
import shutil
from os import path
def main():
        if path.exists("file1.txt"):
                src = path.realpath("file1.txt")     #get the path

                head, tail = path.split(src)         #separate the path from the filter
                print("path :"+head)
                print("file :"+tail)

                dst = src+".bak"                     #make a backup copy
                shutil.copy(src,dst)                 # make a copy 
                shutil.copystat(src,dst)             #copy permissions, modification