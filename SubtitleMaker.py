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

# ipd.Audio('/GD/My Drive/.../audio/numb.m4a')
# ipd.Audio('/GD/My Drive/.../audio/Michael Jackson Dangerous.m4a')
# ipd.Audio('/GD/My Drive/.../audio/BlueOneLove.m4a')
ipd.Audio('./Test Podcarst.wav')


# writeToCSV('output.CSV', [Subtitle(0, "00:00:00,000", 'H'), Subtitle(1, "00:00:01,000", '9'), Subtitle(2, "00:00:02,000", 'X'), Subtitle(3, "00:00:03,000", 'S')])



# Numb - Linkin Park 

# filename1 = '/GD/My Drive/../audio/numb.m4a'
# plt.figure(figsize=(15,4))
# data1,sample_rate1 = librosa.load(filename1, sr=22050, mono=True, offset=0.0, duration=50, res_type='kaiser_best')
# librosa.display.waveplot(data1,sr=sample_rate1, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)

# print(data1)
# print(len(data1))
# print(sample_rate1)

# Dangerous - Michael Jackson

# filename2 = '/GD/My Drive/.../audio/Michael Jackson Dangerous.m4a'
# plt.figure(figsize=(15,4))
# data2,sample_rate2 = librosa.load(filename2, sr=22050, mono=True, offset=0.0, duration=180, res_type='kaiser_best')
# librosa.display.waveplot(data2,sr=sample_rate2, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)

# print(data2)
# print(len(data2))
# print(sample_rate2)


# One Love - Blue
# createSubtitleData('hi')
# filename3 = '/GD/My Drive/.../audio/BlueOneLove.m4a'
filename3 = './Test Podcarst.wav'
plt.figure(figsize=(15,4))
data3,sample_rate3 = librosa.load(filename3, mono=True, offset=0.0, duration=180, res_type='kaiser_best')
librosa.display.waveplot(data3,sr=sample_rate3, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)
plt.show()

subTitles = createSubtitleData(data3, sample_rate3)

# lengthOfData = len(subTitles)
# # print('len: ' + str(lengthOfData))
# for index, sub in enumerate(subTitles):
#     # print('here: ' + str(index))
#     if (index > 0):
#         # print (str(sub.index))
#         # print (subTitles[index - 1].timeStamp + ' --> ' + sub.timeStamp)
#         # print (sub.randomDigit)
#         # print ()
#         file_writer.writerow(str(sub.index))
#         file_writer.writerow([subtitleData[index - 1].timeStamp + ' --> ' + sub.timeStamp])
#         file_writer.writerow(sub.randomDigit)
# print('lol')

writeToCSV('output.CSV', subTitles)
# print(max(data3))
# print(data3)
# print(len(data3))
# print(sample_rate3)
# print(max(data3))
# for i in data3:
#     i.



input()


