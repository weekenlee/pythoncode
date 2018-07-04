# coding: utf-8
import os
import shutil
import sys

if __name__=="__main__":
    day = sys.argv[1]
    srcdir=".//files"
    desdir=".//files_"+ day
    for f in os.listdir(srcdir):
        name = f.split(".")[0] + "_" + day +".xlsx"
        if not os.path.exists(desdir):
            os.makedirs(desdir)
        shutil.copyfile(srcdir+"\\"+f, desdir + "\\" + name)
