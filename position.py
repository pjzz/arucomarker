# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:00:17 2018

@author: ZZ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

pos=pd.read_csv("d:/position.csv")
plt.xlim(0,3840)  
plt.ylim(0,2160)  
plt.scatter(pos["X"],2160-pos["Y"])
plt.show
plt.savefig("d:/position.jpg")
myfile="d:/position.csv"
#os.remove(myfile)