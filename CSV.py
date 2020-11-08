import csv

def writeToCSV(filename, subtitleData):
    # with open('output.csv', mode='w', newline='') as output_file:
    with open(filename, mode='w', newline='') as output_file:
        print('--------- STARTING WRITING ---------')
        file_writer = csv.writer(output_file, delimiter='|', quoting=csv.QUOTE_NONE)
        code = ''
        lengthOfData = len(subtitleData)
        for index, sub in enumerate(subtitleData):
            if (index > 0):
                # print (str(sub.index))
                # print (subtitleData[index - 1].timeStamp + ' --> ' + sub.timeStamp)
                # print (sub.randomDigit)
                # print ()
                file_writer.writerow([str(sub.index)])
                file_writer.writerow([subtitleData[index - 1].timeStamp + ' --> ' + sub.timeStamp])
                file_writer.writerow(sub.randomDigit)
                file_writer.writerow('')
                code += sub.randomDigit
                print('Written (' + str(index) + '/' + str(lengthOfData) + ')')
        print('-------------- FINISHED --------------')
        print('Code is as follows: ' + code)
        print('...Press key to exit')