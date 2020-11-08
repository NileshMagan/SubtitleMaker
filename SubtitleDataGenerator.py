import datetime
import math
import string
import random
# import Subtitle from Subtitle
from Subtitle import Subtitle

def createSubtitleData(amplitudes, sampleRate):
    threshold = 0.25
    minSecondsApart = datetime.timedelta(seconds=2)

    numberOfPoints = len(amplitudes)
    totalTime = datetime.timedelta(seconds=(numberOfPoints / sampleRate))
    timeIncrement = datetime.timedelta(seconds=(1 / sampleRate))
    iteratingTime = datetime.timedelta(seconds=0)
    prevTime = datetime.timedelta(seconds=0)
    timestamp = sampleRate

    itr = 1
    # finalTimes = [Subtitle(itr, iteratingTime, generateRandomChar())]
    finalTimes = [Subtitle(0, "00:00:00,000", generateRandomChar())]
    print('--------- STARTING PROCESSING ---------')
    lengthOfData = len(amplitudes)
    for index, amp in enumerate(amplitudes):
        if (index > 0):
            if detectRisingEdgeThreshold(amplitudes[index -1], amp, threshold) and checkIfTimeIsDistant(prevTime, iteratingTime, minSecondsApart):
                finalTimes.append(Subtitle(itr, formatTimeStamp(iteratingTime), generateRandomChar()))
                itr += 1
                prevTime = iteratingTime
        iteratingTime += timeIncrement
        # else:
        #     index = 200000
        print('Processed (' + str(index) + '/' + str(lengthOfData) + ')')
        # if (index > 200000):
        #     break

    # for index, sub in enumerate(finalTimes):

    #     # if (index > 0)

    #     # print(iteratingTime)
    #     # print(str(math.floor(iteratingTime.seconds)))
    #     # print(iteratingTime.seconds)
    #     # print(iteratingTime.total_seconds())
    #     hours = '00'
    #     try:
    #         hours = '{:02d}'.format(math.floor(iteratingTime.seconds/(60 * 60)))
    #     except:
    #         pass
    #     minutes = '00'
    #     try:
    #         minutes = '{:02d}'.format(math.floor(iteratingTime.seconds/60) % 60)
    #     except:
    #         pass
    #     seconds = '{:02d}'.format(iteratingTime.seconds % 60)
    #     milli = '000'
    #     if (len(str(iteratingTime.microseconds)) > 1):
    #         milli = str(iteratingTime.microseconds/1000)[0:3]
    #     print(str(index) + ': ' + hours + ':' + minutes + ':' + seconds + ',' + milli)
    #     currentTimstamp = (hours + ':' + minutes + ':' + seconds + ',' + milli)
    #     iteratingTime += timeIncrement
    return finalTimes

def formatTimeStamp(time):
    hours = '00'
    try:
        hours = '{:02d}'.format(math.floor(time.seconds/(60 * 60)))
    except:
        pass
    minutes = '00'
    try:
        minutes = '{:02d}'.format(math.floor(time.seconds/60) % 60)
    except:
        pass
    seconds = '{:02d}'.format(time.seconds % 60)
    milli = '000'
    if (len(str(time.microseconds)) > 1):
        milli = str(time.microseconds/1000)[0:3]
    # print(str(index) + ': ' + hours + ':' + minutes + ':' + seconds + ',' + milli)
    currentTimstamp = (hours + ':' + minutes + ':' + seconds + ',' + milli)
    return currentTimstamp
    # iteratingTime += timeIncrement

def generateRandomChar():
    chars = string.ascii_uppercase + string.digits
    return random.choice(chars)


def detectRisingEdgeThreshold(p1, p2, thresh):
    if ((p2 - p1) > 0 and (p2 >= thresh) and (p1 < thresh)):
        return True
    return False

def detectRisingEdgeSR(p1, p2, thresh):
    if ((p2 - p1) > thresh):
        return True
    return False

def checkIfTimeIsDistant(t1, t2, minTimeApart):
    if ((t2 - t1) >= minTimeApart):
        return True
    return False



# def detectRisingEdge(p1, p2, thresh):
#     if ((p2 - p1) > thresh) {
#         return true
#     }
#     return false




amplitudes = [1,2,3,4,5,6,7,8,9,10]
sr = 3
createSubtitleData(amplitudes, sr)