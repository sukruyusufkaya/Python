"""from openpyxl import Workbook,load_workbook

P_yuk = [0.580416667, 0.539066667, 0.390116667, 0.232033333, 0.204533333, 0.194716667, 0.194633333, 0.209233333, 0.247266668, 0.407916668, 0.537349998, 0.576983332, 0.580216667, 0.520566667, 0.485200003, 0.4197, 0.424300002, 0.448333332, 0.546983333, 0.840733333, 1.0, 0.856422014, 0.921716667, 0.720283335]
pv_uretilen = [0, 0, 0, 0, 0.846573268, 6.670823882, 0.2234096457, 0.4840323145, 0.9510129002, 1.617686087, 2.369894473, 2.939150696, 3.053854497, 2.946843366, 2.517269744, 1.822991627,1.23210826, 7.311869927, 3.355642336, 0.9910144956, 0.1621109317, 0.008980831, 0, 0]
P_sebeke_satis = list()
P_sebeke_alis = list()
for i in range(0, 24):
    if pv_uretilen[i] < P_yuk[i]:
        P_sebeke_alis.append((P_yuk[i] - pv_uretilen[i]))
        P_sebeke_satis.append(0)

    elif pv_uretilen[i] > P_yuk[i]:
        P_sebeke_satis.append((pv_uretilen[i] - P_yuk[i]))
        P_sebeke_alis.append(0)

Guc_sebekedenalinan = 0
for i in range(0, 24):
    print(i,".00 Saatinde şebekeden alınan yük", P_sebeke_alis)
    #Guc_sebekedenalinan = Guc_sebekedenalinan + int(P_sebeke_alis[i])

Guc_sebekeyeverilen = 0
for i in range(0, 24):
    print(i,".00 Saatinde şebekeye satilan yük", P_sebeke_satis)
    #Guc_sebekeyeverilen = Guc_sebekeyeverilen + int(P_sebeke_satis[i])"""
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock"
            "")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()
#Execution of the window.clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
clock.mainloop()
#Execution of the window.
