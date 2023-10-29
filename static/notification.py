import time
import os
from plyer import notification

birthdayFile = 'birthdays.txt'
def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
            # line[1] contains Name and line[2] contains Surname
            notification.notify(
                title = "Birthday Notification",
                message = str(line[1]) + " " + str(line[2]) + " BIRTHDAY",
                timeout = 10
            )
            # os.system('notify-send "Birthdays Today: ' + line[1]
            # + ' ' + line[2] + '"')
    # if flag == 0:
    #         os.system('notify-send "No Birthdays Today!"')
  
if __name__ == '__main__':
    checkTodaysBirthdays() 
