# SubtitleMaker

## Basic Info
This solution creates a subtitle (.srt) file by generating a random digit (alphabet + numbers) each time the music goes past a certain amplitude. A digit will only be generated if another digit has not been generated within the last time period (e.g. say the time period is 2 seconds, another digit won't be generated if another one has been generated within the last 2 seconds). The amplitude and time period are adjustable as described below

## How to run
Clone this solution and just be weary you may have to install some libraries (use google if you get any errors to make sure all the packages are installed). 

Running it out of the box probably won't be suitable for your application so please see the "Configuration" section below on how to tailor it to your project

In terms of running the project, once you have the solution downloaded, go to that directory and open a command prompt. Type the command below to run the project:
```
python SubtitleMaker.py
```

## Configuration
Open the file 'SubtitleMaker.py'

In there you should see some important variables at the top of the file:
```
audioFile = './Test Podcarst.wav'
outputFile = 'output.srt'
showGraphAtBeginning = True
amplitudeThreshold = 0.25
minimumSecondsBetweenEachSubtitle = 2
```
The first two variables are self explanatory, 'audioFile' is just the input music file you are trying to create the .srt for and the 'outputFile' is just the .srt file that will be generated - both of which must/will be in the same directory as the code. 

Now for the important parts. The parameters 'amplitudeThreshold' and 'minimumSecondsBetweenEachSubtitle' are the variables that will need twweaking. How to know what they should be? The parameter 'showGraphAtBeginning' is a switch, which when true, shows a waveform of the song with the amplitude of each part of the song vs time. It is recommended that you leave this on initially so you can see what kind of amplitudes your song has. Look at the amplitudes of the spikes that your song has and use that to determine what amplitude you think would be a good amplitude that when past, a new digit is generated. If the song is beat heavy and has lots of big spikes, adjusting the 'minimumSecondsBetweenEachSubtitle' variable can help avoid a new digit being generated every single spike as it will only generate a new digit no more than once every 'minimumSecondsBetweenEachSubtitle' period.

Good luck!
