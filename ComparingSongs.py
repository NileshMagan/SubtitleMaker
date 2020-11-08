#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/GD')


# In[ ]:


get_ipython().system('pip install librosa')


# In[ ]:


# Load imports
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt


# In[ ]:


ipd.Audio('/GD/My Drive/.../audio/numb.m4a')


# In[ ]:


ipd.Audio('/GD/My Drive/.../audio/Michael Jackson Dangerous.m4a')


# In[ ]:


ipd.Audio('/GD/My Drive/.../audio/BlueOneLove.m4a')


# In[ ]:


# Numb - Linkin Park 

filename1 = '/GD/My Drive/../audio/numb.m4a'
plt.figure(figsize=(15,4))
data1,sample_rate1 = librosa.load(filename1, sr=22050, mono=True, offset=0.0, duration=50, res_type='kaiser_best')
librosa.display.waveplot(data1,sr=sample_rate1, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)


# In[ ]:


print(data1)
print(len(data1))
print(sample_rate1)


# In[ ]:


# Dangerous - Michael Jackson

filename2 = '/GD/My Drive/.../audio/Michael Jackson Dangerous.m4a'
plt.figure(figsize=(15,4))
data2,sample_rate2 = librosa.load(filename2, sr=22050, mono=True, offset=0.0, duration=180, res_type='kaiser_best')
librosa.display.waveplot(data2,sr=sample_rate2, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)


# In[ ]:


print(data2)
print(len(data2))
print(sample_rate2)


# In[ ]:


# One Love - Blue

filename3 = '/GD/My Drive/.../audio/BlueOneLove.m4a'
plt.figure(figsize=(15,4))
data3,sample_rate3 = librosa.load(filename3, mono=True, offset=0.0, duration=180, res_type='kaiser_best')
librosa.display.waveplot(data3,sr=sample_rate3, max_points=50000.0, x_axis='time', offset=0.0, max_sr=1000)


# In[ ]:


print(data3)
print(len(data3))
print(sample_rate3)

