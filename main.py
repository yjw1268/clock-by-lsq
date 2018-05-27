# -*- coding: UTF-8 -*-
import time,sys,math,_thread
from tkinter import *
from turtle import *

def runnian(a):
    p=""
    if((a%4==0 and a%100!=0) or a%400==0):
        p="闰年 "
    else:
        p = "平年"
    return p

def shuxiang(y):
    p=""
    if(y%12==0):
        p="猴"
    if (y % 12 == 1):
        p = "鸡"
    if (y % 12 == 2):
        p = "狗"
    if (y % 12 == 3):
        p = "猪"
    if (y % 12 == 4):
        p = "鼠"
    if (y % 12 == 5):
        p = "牛"
    if (y % 12 == 6):
        p = "虎"
    if (y % 12 == 7):
        p = "兔"
    if (y % 12 == 8):
        p = "龙"
    if (y % 12 == 9):
        p = "蛇"
    if (y % 12 == 10):
        p = "马"
    if (y % 12 == 11):
        p = "羊"
    return p

def tgdz(year):   #天干地支
    n1=year%10
    n2=year%12
    p=""

    if(n1<=3):
        n1+=7
    else:
        n1-=3
    if(n2<=3):
        n2+=9
    else:
        n2-=3

    if (n1 == 1):
        p="甲"
    if (n1 == 2):
        p="乙"
    if (n1 == 3):
        p="丙"
    if (n1 == 4):
        p="丁"
    if (n1 == 5):
        p="戊"
    if (n1 == 6):
        p="己"
    if (n1 == 7):
        p="庚"
    if (n1 == 8):
        p="辛"
    if (n1 == 9):
        p="壬"
    if (n1 == 10):
        p="癸"

    if (n2 == 1):
        p+="子"
    if (n2 == 2):
        p+="丑"
    if (n2 == 3):
        p+="寅"
    if (n2 == 4):
        p+="卯"
    if (n2 == 5):
        p+="辰"
    if (n2 == 6):
        p+="巳"
    if (n2 == 7):
        p+="午"
    if (n2 == 8):
        p+="未"
    if (n2 == 9):
        p+="申"
    if (n2 == 10):
        p+="酉"
    if (n2 == 11):
        p+="戌"
    if (n2 == 12):
        p+="亥"
    return p

def setdate():
    Y,M,D= map(int, input("Enter date(year,month,date):").split())
    if(Y>2049 or Y<1970 or M>12 or M<1 or D>31 or D<1):
        print("input error")
    elif(D==31 and (M==4 or M==6 or M==9 or M==11)):
        print("input error")
    elif(D>28 and M==2 and runnian(Y)!=""):
        print("input error")
    else:
        rtime['year']=Y
        rtime['month']=M
        rtime['date']=D
        print("resetted")

def settime():
    H,M,S=map(int, input("Enter time(hour,minute,second):").split())
    if(H>23 or H<0 or M>59 or M<0 or S>59 or S<0):
        print("input error")
    else:
        rtime['hour'] = H
        rtime['minute'] = M
        rtime['second'] = S
        print("resetted")



def reset():
    rtime1["year"] = time.strftime('%Y', time.localtime(time.time()))
    rtime1["month"] = time.strftime('%m', time.localtime(time.time()))
    rtime1["date"] = time.strftime('%d', time.localtime(time.time()))
    rtime1["hour"] = time.strftime('%H', time.localtime(time.time()))
    rtime1["minute"] = time.strftime('%M', time.localtime(time.time()))
    rtime1["second"] = time.strftime('%S', time.localtime(time.time()))
    rtime["year"] = int(rtime1["year"])
    rtime["month"] = int(rtime1["month"])
    rtime["date"] = int(rtime1["date"])
    rtime["hour"] = int(rtime1["hour"])
    rtime["minute"] = int(rtime1["minute"])
    rtime["second"] = int(rtime1["second"])

def drawclock(canvas):
    x = 100
    y = 100
    width = 75 + 5
    for i in range(0, 12):
        arc = 2.0 * math.pi / 12 * i
        new_x = x + width * math.sin(arc)
        new_y = y - width * math.cos(arc)
        canvas.create_text(new_x, new_y, text=str(i))


def drawpointer(canvas, hour, minute, second):
    x = 100
    y = 100
    hour_width = 35
    minute_width = 45
    second_width = 60
    hour_arc = 2.0 * math.pi * hour / 12
    minute_arc = 2.0 * math.pi * minute / 60
    second_arc = 2.0 * math.pi * second / 60
    canvas.create_line(x, y, x + hour_width * math.sin(hour_arc), y - hour_width * math.cos(hour_arc))
    canvas.create_line(x, y, x + minute_width * math.sin(minute_arc), y - minute_width * math.cos(minute_arc))
    canvas.create_line(x, y, x + second_width * math.sin(second_arc), y - second_width * math.cos(second_arc))


def showtime(app, canvas):
    while 1:
        # print
        canvas.create_rectangle(0, 0, 200, 200, fill='white')
        canvas.create_oval(25, 25, 175, 175)
        drawclock(canvas)
        drawpointer(canvas, rtime['hour'], rtime['minute'], rtime['second'])
        app.update()
        time.sleep(1)




rtime={}
rtime1={}
rtime1["year"]=time.strftime('%Y',time.localtime(time.time()))
rtime1["month"]=time.strftime('%m',time.localtime(time.time()))
rtime1["date"]=time.strftime('%d',time.localtime(time.time()))
rtime1["hour"]=time.strftime('%H',time.localtime(time.time()))
rtime1["minute"]=time.strftime('%M',time.localtime(time.time()))
rtime1["second"]=time.strftime('%S',time.localtime(time.time()))
rtime["year"]=int(rtime1["year"])
rtime["month"]=int(rtime1["month"])
rtime["date"]=int(rtime1["date"])
rtime["hour"]=int(rtime1["hour"])
rtime["minute"]=int(rtime1["minute"])
rtime["second"]=int(rtime1["second"])
print(rtime1['year'],end="")
print("年",end="")
print(rtime1['month'],end="")
print("月",end="")
print(rtime1['date'],end="")
print("日")
#print(time.strftime("%H:%M:%S", time.localtime()))
#year=int(time.strftime("%Y", time.localtime()))
#runnian(year)
#tgdz(year)


window = Tk()
window.title("Clock")
window.geometry('300x400')
window.resizable(0, 0)

Label1=Label(window, text=rtime1['year']+"年"+rtime1['month']+"月"+rtime1['date']+"日", font=('Arial', 15))     #输出年月日
Label1.pack()
Label2=Label(text=rtime1['hour']+":"+rtime1['minute']+":"+rtime1['second'], font=('Arial', 15))     #输出具体时间
Label2.pack()


year = runnian(rtime['year']) + " " + tgdz(rtime['year']) + " " + shuxiang(rtime['year'])
print(year)
Label3=Label(window, text=year, font=('Arial', 15))     #是否闰年以及天干地支
Label3.pack()

sett=Button(window,text="settime",command=settime)
sett.place(x=175,y=300,width=50,height=30)

setd=Button(window,text="setdate",command=setdate)
setd.place(x=125,y=300,width=50,height=30)

rset=Button(window,text="reset",command=reset)
rset.place(x=75,y=300,width=50,height=30)



canvas = Canvas(window, width=200, height=200)
canvas.pack()
_thread.start_new_thread(showtime, (window, canvas))



#未完成的输入框
#root=Entry(window,width=20)
#root.place(x=40,y=150,width=100,heigh=30)
#var = StringVar()   # 这即是输入框中的内容
#var.get()


#btn7 = Button(window, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5)
#btn7.place(x=0, y=285, width=70, height=55)







def trickit():     #每0.1秒刷新一次
    if((rtime['second'])<59):
        rtime['second'] += 1
    elif(rtime['minute']<59):
        rtime['minute'] += 1
        rtime['second'] = 0
    elif(rtime['hour']<23):
        rtime['hour'] += 1
        rtime['minute'] = 0
        rtime['second'] = 0
    elif (rtime['date'] < 28):
        rtime['date'] += 1
        rtime['hour'] = 0
        rtime['minute'] = 0
        rtime['second'] = 0
    elif (rtime['month'] < 12):
        if(rtime['month']==1 or rtime['month']==3 or rtime['month']==5 or rtime['month']==7 or rtime['month']==8 or rtime['month']==10):
            if(rtime['date']<31):
                rtime['date']+=1
            else:
                rtime['month'] += 1
                rtime['date'] = 1
                rtime['hour'] = 0
                rtime['minute'] = 0
                rtime['second'] = 0
        if(rtime['month']==4 or rtime['month']==6 or rtime['month']==9 or rtime['month']==11):
            if (rtime['date'] < 30):
                rtime['date'] += 1
            else:
                rtime['month'] += 1
                rtime['date'] = 1
                rtime['hour'] = 0
                rtime['minute'] = 0
                rtime['second'] = 0
        else:  #二月
            if(runnian(rtime['year'])):
                if(rtime['date']<29):
                    rtime['date']+=1
                else:
                    rtime['month'] += 1
                    rtime['date'] = 1
                    rtime['hour'] = 0
                    rtime['minute'] = 0
                    rtime['second'] = 0
    else:
        if(rtime['date']<31):
            rtime['date']+=1
        else:
            rtime['year']+=1
            rtime['month'] = 1
            rtime['date'] = 1
            rtime['hour'] = 0
            rtime['minute'] = 0
            rtime['second'] = 0

    t1 = str(rtime['year']).zfill(4) + "年" + str(rtime['month']).zfill(2) + "月" + str(rtime['date']).zfill(2) + "日"
    Label1.config(text=t1, font=('Arial', 15))
    t = str(rtime['hour']).zfill(2) + ":" + str(rtime['minute']).zfill(2) + ":" + str(rtime['second']).zfill(2)
    Label2.config(text=t, font=('Arial', 15))
    y1 = runnian(rtime['year']) + " " + tgdz(rtime['year']) + " " + shuxiang(rtime['year'])
    Label3.config(text=y1, font=('Arial', 15))  # 是否闰年以及天干地支
    window.update()
    Label2.after(1000, trickit)
Label2.after(1000, trickit)



window.mainloop()