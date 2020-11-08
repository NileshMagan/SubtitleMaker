#!/usr/bin/env python
# coding: utf-8

# from google.colab import drive
# drive.mount('/GD')

# get_ipython().system('pip install librosa')

# Load imports
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
from SubtitleDataGenerator import createSubtitleData 
from Subtitle import Subtitle
from CSV import writeToCSV

# Variables
audioFile = './Test Podcarst.wav'
outputFile = 'output.srt'
showGraphAtBeginning = True
amplitudeThreshold = 0.25
minimumSecondsBetweenEachSubtitle = 2

# Grab audio from file and get amplitudes
data3,sample_rate3 = librosa.load(audioFile, mono=True, offset=0.0, duration=180, res_type='kaiser_best')
librosa.display.waveplot(data3,sr=sample_rate3, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)

# Graph data
plt.figure(figsize=(15,4))
if showGraphAtBeginning:
    plt.show()

# Go through audio data, check amplitudes and generate digits
subTitles = createSubtitleData(data3, sample_rate3, amplitudeThreshold, minimumSecondsBetweenEachSubtitle)

# Write subtitles to file
writeToCSV(outputFile, subTitles)

# Wait on users input before exiting
input()


