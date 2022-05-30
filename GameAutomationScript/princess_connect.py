import os
import random
import time
import math
import cv2
from tkinter import *
import _thread
import threading

scrX=2160
scrY=1080
scrxcm=scrX/157.664
scrycm=scrY/157.664
# scrxcm=13.7
# scrycm=6.85
resolution=scrX*scrY
arg_device="-s 192.168.123.159:5555"
arg_device_id="P7CDU18A17004016"
boffset=random.randint(-5,5)+random.random()
soffset=random.uniform(-0.01,0.01)
awatingarr=[]
settingarr=[]
timesarr=[]

def back():
    click(scrX/scrxcm*3,scrY/scrycm*0.7,1)
def time_sleep(t):
    time.sleep(t+random.random())
def click(tx,ty,t):
    os.system(f"adb {arg_device} shell input tap {tx+boffset} {ty+boffset}")
    time_sleep(t+random.random())
def swipe():
    os.system(f'adb {arg_device} shell input swipe {scrX/2} {scrY/2} {scrX*0.75} {scrY/2}')
    time_sleep(0.5)
def init():
    os.system(f"adb tcpip 5555")
    os.system(f"adb connect 192.168.123.159:5555")
#tab 0.6
def tab1():
    click(scrX/scrxcm*1.5,scrY/scrycm*6.55,2)
def tab2():
    click(scrX/scrxcm*3.5,scrY/scrycm*6.55,2)
def tab3():
    click(scrX/scrxcm*5.0,scrY/scrycm*6.55,2)
def tab4(c):
    click(scrX/2,scrY/scrycm*6.55,2)
    if(c==1):
        #挑战
        click(scrX/5*3,scrY/3,2)
    if(c==2):
        #竞技场
        click(scrX/scrxcm*9,scrY/scrycm*5.3,2)
        #报酬
        click(scrX/scrxcm*4.5,scrY/scrycm*4.35,2)
        click(scrX/scrxcm*3,scrY/scrycm*0.7,2)
#公会之家
#7.85-9.45
def tab5():
    # for i in range(10):
    click(scrX/scrxcm*8.5,scrY/scrycm*6.55,2)
    #全部收取
    click(scrX/scrxcm*12.8,scrY/scrycm*5.6,1)
    back()
    
def screenshot():
    os.system(f"adb {arg_device} shell screencap -p /sdcard/Download/test1.png")
    os.system(f"adb {arg_device} pull /sdcard/Download/test1.png C:/Users/wxy/Desktop/tmp")
    os.system(f"adb {arg_device} shell rm /sdcard/Download/test1.png")
    img = cv2.imread('C:/Users/wxy/Desktop/tmp/test1.png')
    sp = img.shape
    #5.6 6.1 8.05
    b=img[math.ceil(sp[0]/scrycm*0.5),math.ceil(sp[1]/scrxcm*6.1),0]
    g=img[math.ceil(sp[0]/scrycm*0.5),math.ceil(sp[1]/scrxcm*6.1),1]
    r=img[math.ceil(sp[0]/scrycm*0.5),math.ceil(sp[1]/scrxcm*6.1),2]
    if(b>75 and b<85 and g>222 and g<230 and r>250):
        return 1
    
    return -1

def task():
    click(scrX/scrxcm*12.1,scrY/scrycm*5.5,2)
    click(scrX/scrxcm*12.2,scrY/scrycm*5.55,1)
    click(scrX/scrxcm*6.7,scrY/scrycm*6,1)

def setting(chapter,level):
    # stagearr=''
    curpos=''
    curchapter=0
    curlevel=0
    forward=0
    # backward=0
    adb_home=os.getenv('ADB_HOME')   
    with open(f'{adb_home}/tmp/curstage.txt','r') as curinfo:
        curpos=curinfo.read()
    curinfo.close()
    curchapter=int(curpos[0])
    #chapter jump
    forb=chapter-curchapter
    if(forb>0):
        for i in range(forb):
            click(scrX/scrxcm*13.25,scrY/2,1)
            curchapter=curchapter+1
    else:
        for i in range(-forb):
            click(scrX/scrxcm*0.45,scrY/2,1)
            curchapter=curchapter-1
    os.system(f'adb {arg_device} shell input swipe {scrX/2} {scrY/2} {scrX*0.75} {scrY/2}')
    if(curchapter==1): click(scrX/scrxcm*2.1,scrY/2,0)
    if(curchapter==2): click(scrX/scrxcm*2.3,scrY/scrycm*5.3,0)
    if(curchapter==3): click(scrX/scrxcm*2.5,scrY/scrycm*2.5,0)
    if(curchapter==4): click(scrX/scrxcm*3.2,scrY/scrycm*3.2,0)
    if(curchapter==5): click(scrX/scrxcm*2.5,scrY/scrycm*2.5,0)
    if(curchapter==6): click(scrX/scrxcm*3.1,scrY/scrycm*5,0)
    curlevel=1
    forward=level-curlevel
    for i in range(forward):
        # #前进小
        os.system(f"adb {arg_device} shell input tap {scrX/scrxcm*12.75+boffset} {scrY/2.15+boffset}")
    # curlevel=level
    curchapter=chapter
    with open(f'{adb_home}/tmp/curstage.txt','w+') as curinfo:
        curinfo.write(f'{curchapter}')
    curinfo.close()

def likerankup():
    for i in range(10):
        #第一个
        click(scrX/scrxcm*10,scrY/scrycm*1.75,1)
        #最后一话
        click(scrX/scrxcm*10,scrY/scrycm*3.1,2)
        #无语音
        click(scrX/scrxcm*6.7,scrY/scrycm*4.7,2)
        #MENU
        click(scrX/scrxcm*12.2,scrY/scrycm*0.5,2)
        #跳过
        click(scrX/scrxcm*11,scrY/scrycm*0.5,2)
        #确认跳过
        click(scrX/scrxcm*8,scrY/scrycm*4.7,2)
        #返回
        click(scrX/scrxcm*0.35,scrY/scrycm*0.35,2)
        click(scrX/scrxcm*0.35,scrY/scrycm*0.35,2)  

def autorun(elapsed,times):
    #挑战
    click(scrX/scrxcm*11.5,scrY/scrycm*5.75,1)
    #战斗开始
    click(scrX/scrxcm*11.5,scrY/scrycm*5.75,elapsed)
    s=-1
    for i in range(times):
        while(s==-1):
            #跳过好感度
            click(scrX/scrxcm*10,scrY/scrycm*0.5,0)
            click(scrX/scrxcm*12,scrY/scrycm*0.5,0)
            click(scrX/scrxcm*10,scrY/scrycm*0.5,0)
            time_sleep(4) 
            s=screenshot()
            time_sleep(4)
            
        #前往主线关卡
        #click(scrX/scrxcm*11,scrY/scrycm*6.2,2)
        #return -1
        #下一步
        click(scrX/scrxcm*11.5,scrY/scrycm*6.45,3)
        #跳过限定商店
        click(scrX/scrxcm*10,scrY/scrycm*0.5,0)
        print(i)
        if(times>1 and i != times-1):
            #重新开始
            click(scrX/scrxcm*9.2,scrY/scrycm*6.15,1)
            #确认开始
            click(scrX/scrxcm*8.2,scrY/scrycm*4.65,elapsed) 
        s=-1
    #下一步
    click(scrX/scrxcm*11.2,scrY/scrycm*6.2,1)
    #关闭剧情working on
    back()
    back()
    return 1

def namecallback(name):
        namestatus=0
        for i in awatingarr:
            if(i==name):
                namestatus=1
        if(namestatus==1): awatingarr.remove(name)
        else: awatingarr.append(name)
        print(awatingarr)

def timecallback(t):
    # timestatus=0
    # for i in timesarr:
    #     if(i==t):
    #         timestatus=1
    # if(timestatus==1): timesarr.remove(t)
    # else: 
    timesarr.append(t)
    print(timesarr)

def clearcallback(arr):
    arr.clear()
    print(arr)

def settinginit():
    for i in range(len(awatingarr)):
        settingarr.append(int(awatingarr[i].split('-')[0]))
        settingarr.append(int(awatingarr[i].split('-')[1]))
    j=0
    tab4(1)
    for i in range(0,len(settingarr),2):
        setting(settingarr[i],settingarr[i+1])
        status=autorun(50+random.randint(0,5),timesarr[j])
        if(status==-1): print("挑战失败")
        if(status==1): print("挑战成功")
        j=j+1
    awatingarr.clear()
    settingarr.clear()
    timesarr.clear()

def thread_it(func,*args):
    # 创建
    t = threading.Thread(target=func) 
    # 守护
    t.setDaemon(True) 
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()

def ui():
    name_list=['1-1','1-2','1-3','1-4','1-5','1-6','1-7','1-8','1-9','1-10',
    '2-1','2-2','2-3','2-4','2-5','2-6','2-7','2-8','2-9','2-10','2-11','2-12',
    '3-1','3-2','3-3','3-4','3-5','3-6','3-7','3-8','3-9','3-10','3-11','3-12',
    '4-1','4-2','4-3','4-4','4-5','4-6','4-7','4-8','4-9','4-10','4-11','4-12','4-13',
    '5-1','5-2','5-3','5-4','5-5','5-6','5-7','5-8','5-9','5-10','5-11','5-12','5-13',
    '6-1','6-2','6-3','6-4','6-5','6-6','6-7','6-8','6-9','6-10','6-11','6-12','6-13','6-14',
    '7-1','7-2','7-3','7-4','7-5','7-6','7-7','7-8','7-9','7-10','7-11','7-12','7-13','7-14']
    times_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    root= Tk()
    root.title('gzlj')
    root.geometry('1400x800')
    with open('D:/adb/tmp/stage1.txt','r') as f:
        row=f.read().split(',')
    f.close()
    j=1
    i=0
    for inx,name in enumerate(name_list):
        if(inx>=int(row[j])):
            i=i+1
            j=j+1
        Button(root,width=10,height=1,text=name,command=lambda arg=name:namecallback(arg)).grid(row=i,column=(inx-int(row[j-1]))%(int(row[j])-int(row[j-1])))
        
    for inx,t in enumerate(times_list):
        Button(root,width=10,height=3,text=t,command=lambda arg=t:timecallback(arg)).grid(row=math.floor(19+inx/10),column=inx%10)
    Button(root,width=20,height=1,text='clear',command=lambda:clearcallback(timesarr)).grid(row=20,column=10)
    Button(root,width=20,height=1,text='start',command=lambda:thread_it(settinginit,[])).grid(row=21,column=5)
    Button(root,width=20,height=1,text='工会之家',command=lambda:thread_it(tab5,[])).grid(row=22,column=0)
    root.mainloop()

if __name__ == "__main__":
    init()
    # ui()
    autorun(50,20)



# stagechapter=[1,2,3,4]
# stagelevel=[2,2,3,4]
# for i in zip(stagechapter,stagelevel):
#     setting(i[0],i[1])
#     status=autorun(50+random.randint(0,5),4)
#     if(status==-1): print("挑战失败")
#     if(status==1): print("挑战成功")



# tab3()
# #角色
# click(scrX/scrxcm*8,scrY/scrycm*4.5,1)


# with open(f'C:/Users/wxy/Desktop/tmp/gk.csv','r') as gk:
#     eachstage=gk.read().replace('\n',',').split(',')
#     for i in range(0,len(eachstage),3):
#         if(eachstage[i]=='35'):
#             print(f'{eachstage[i+1]} {eachstage[i+2]}')
# gk.close()



# for i in range(2):
#     tab1()
#     task()



# else:
#     for i in range((chapter-1)*2,(curchapter-1)*2,2):
#         if(int(stagearr[i])==chapter):
#             backward=backward+int(stagearr[i+1])-level
#         else:
#             if(int(stagearr[i])<curchapter):
#                 backward=backward+int(stagearr[i+1])
#     backward=backward+1
#     for i in range(backward):
#         # #后退小
#         os.system(f"adb {arg_device} shell input tap {scrX/scrxcm*0.95+boffset} {scrY/2.15+boffset}")


# def findstagemax(curchapter,stagearr):
#     for i in range(0,len(stagearr),2):
#         if(int(stagearr[i])==curchapter):
#             return int(stagearr[i+1])
#     return 0


#generate levels
# with open('D:/adb/tmp/stage.txt','r') as f:
#     tmp=f.read().replace('\n',',').split(',')
#     for i in range(0,len(tmp),2):
#         for j in range(1,int(tmp[i+1])):
#             print(f"'{tmp[i]}-{j}',",end="")
#         print(f"'{tmp[i]}-{j+1}',",end="")
