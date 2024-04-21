#!/usr/bin/env python

import os
path=os.chdir("C:\\Users\\Desktop\\New folder (2)")#put your working directory
path_str="C:\\Users\\Harshit\\Desktop\\New folder (2)"#same path as above
for folder in os.listdir(path):
    print(folder)#all names of files in the directory    
    
#unzip data, if not unzipped the code will delete the zipped data.
import zipfile
for folder in os.listdir(path):
    if folder[-4:]=='.zip':
        try:
            with zipfile.ZipFile(path_str+"\\"+folder, 'r') as zip_ref:
                zip_ref.extractall(path_str)
        except:
            print("Error in "+folder)
            try:
                os.remove(path_str+"\\"+folder[:-3]+"SAFE")
            except:
                print("Error Deleting "+folder[:-3]+"SAFE")





