# -*- coding: utf-8 -*-

''' What is Kudelas Middle Name- guess here on line 3-Steven
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img)
ax[0].set_xlim(20,30)
ax[0].set_ylim(30,20)
ax[1].set_xlim(30,40)
ax[1].set_ylim(40,30)
ax[2].set_xlim(50,40)
ax[2].set_ylim(40,50)
# Show the figure on the screen
fig.show()




