from pynput.mouse import Button,Controller
import time
import random
import pyautogui
mouse=Controller()
print(mouse.position)
resolution=2560*1440

def mouse_click(t):
    mouse.press(Button.left)
    time_sleep(0.1+random.random()/10)
    mouse.release(Button.left)
    time_sleep(t+random.random())

def backwards():
    mouse_position(95,110,90,95)
    mouse_click(0.5)
def mouse_position(x1,x2,y1,y2):
    mouse.position=(random.randint(x1,x2),random.randint(y1,y2))
def time_sleep(t):
    time.sleep(t)
def get_pixel_color(curx,cury):
    # mouse.position=(curx,cury)
    return pyautogui.screenshot().getpixel((curx,cury))
#启动模拟器
def vm():
    mouse.position=(42,1265)
    mouse.click(Button.left,2)
    time_sleep(40)
#模拟器启动游戏
def init():
    mouse.position=(730, 433)
    mouse_click(10)
    # #调整模拟器位置
    mouse.position=(1073, 216)
    mouse.press(Button.left)
    time_sleep(random.random())
    mouse.position=(592, 15)
    mouse.release(Button.left)
    time_sleep(2.5+random.random())

    # #进入游戏
    mouse_position(50,917,60,604)
    mouse_click(5)
    mouse_position(790,793,672,682)
    mouse_click(9)

    mouse.position=(1542,103)
    for i in range(8):
        mouse_click(0.5)
# #基建
def house():
    print(mouse.position)
    mouse_position(1284,1294,818,828)
    mouse_click(5)
# #基建消息
def normalize():
    mouse.position=(1527, 146)
    mouse_click(1)
    get_exp()
# #干员up
def get_exp():
    mouse_position(302,308,898,904)
    mouse_click(1)
    mouse.position=(309,196)
    mouse_click(1)
#贸易
def trade():
    mouse_position(185,225,410,415)
    mouse_click(2)
    mouse_position(105,110,510,515)
    mouse_click(2)
    # mouse_position(242,406,773,780)
    # mouse_click(1)
    # for i in range(2):
    #     pixelColor=get_pixel_color(445,583)
    #     while(pixelColor[0]<10 and pixelColor[1]<190 and pixelColor[2]>230):
    #         mouse_position(440,450,592,594)
    #         mouse_click(1)
    #         pixelColor=get_pixel_color(445,583)
    #     #(57, 67, 81)
    #     if(i==0):
    #         mouse_position(117,167,421,428)
    #         mouse_click(1)
    for i in range(3):
        backwards()
    # time_sleep(2)
#补充体力
#366 604 842
#公开招募
def public_recuit():
    mouse_position(1244,1254,664,672)
    mouse_click(0.5)
    fir_pos=[592,507]
    four_arr=[fir_pos[0],fir_pos[0]+random.randint(1,12),fir_pos[1],fir_pos[1]+random.randint(1,4),
              fir_pos[0]+820,fir_pos[0]+820+random.randint(1,12),fir_pos[1],fir_pos[1]+random.randint(1,4),
              fir_pos[0],fir_pos[0]+random.randint(1,12),fir_pos[1]+350,fir_pos[1]+350+random.randint(1,4),
              fir_pos[0]+820,fir_pos[0]+820+random.randint(1,12),fir_pos[1]+350,fir_pos[1]+350+random.randint(1,4)]
    for number in range(4):
        mouse_position(four_arr[number*4],four_arr[number*4+1],four_arr[number*4+2],four_arr[number*4+3])
        curx,cury=pyautogui.position()
        pixelColor=get_pixel_color(curx,cury)
        if(pixelColor[0]<100 and pixelColor[1]<100 and pixelColor[2]<100):
            continue
        if(pixelColor[0]>=0 and pixelColor[0]<=50 and pixelColor[1]>=100 and pixelColor[1]<=180 and pixelColor[2]>=186 and pixelColor[2]<=240):
            mouse_click(4)
            #skip
            for i in range(2):
                mouse_position(1512,1516,73,75)
                mouse_click(2)
        else: continue
    backwards()
#采购中心
def market():
    mouse_position(1017,1027,615,625)
    mouse_click(2)
# #信用交易所
def credit():
    mouse_position(1463,1473,163,166)
    mouse_click(0.5)
    mouse_position(1263,1268,83,85)
    for i in range(2):
        mouse_click(0.5)
    time_sleep(1)
    fir_pos=[149,328]
    for i in range(10):
        if(i<5): pixelColor=get_pixel_color(fir_pos[0]+317*i+100,fir_pos[1]-90)
        else: pixelColor=get_pixel_color(fir_pos[0]+317*(i-5)+100,fir_pos[1]+227)
        if(pixelColor[0]>150): continue
        if(i<5):
            pixelColor=get_pixel_color(fir_pos[0]+317*i,fir_pos[1])
            if(pixelColor[0]>=145 and pixelColor[0]<=172 and pixelColor[1]>=14 and pixelColor[1]<=45 and pixelColor[2]>=45 and pixelColor[2]<=80):
                continue
            mouse_position(fir_pos[0]+317*i,fir_pos[0]+317*i+10,fir_pos[1],fir_pos[1]+10)
        else:
            pixelColor=get_pixel_color(fir_pos[0]+317*(i-5),fir_pos[1]+317)
            if(pixelColor[0]>=145 and pixelColor[0]<=172 and pixelColor[1]>=14 and pixelColor[1]<=45 and pixelColor[2]>=45 and pixelColor[2]<=80):
                continue
            mouse_position(fir_pos[0]+317*(i-5),fir_pos[0]+317*(i-5)+10,fir_pos[1]+317,fir_pos[1]+318)
        mouse_click(1)
        pixelColor=get_pixel_color(1102,678)
        if(pixelColor[0]==49):
            mouse_position(1228,1238,762,764)
            mouse_click(1)
            pixelColor=get_pixel_color(1102,478)
            if(pixelColor[0]==132):
                backwards()
                continue
            mouse_click(1)
    backwards()
    time_sleep(1)
#作战
def battle():
    mouse_position(1240,1248,262,288)
    mouse_click(0.4)
#作战设置
def setting():
    #  # #粉碎防御2位置
    # mouse_position(266,270,859,872)
    # mouse_click(1.2)
    # mouse_position(574,584,450,470)
    # mouse_click(1.2)
    # mouse_position(1145,1155,250,253)
    # mouse_click(1)
    # # 130-135

    #1-7
    # print("作战第1章")
    # for i in range(3):
    #     time_sleep(random.random())
    #     mouse.position=(49,300)
    #     mouse.press(Button.left)
    #     for i in range(mouse.position[0],1020):
    #         # for j in range(mouse.position[1],finaly):
    #             mouse.position=(i,300)
    #             time_sleep(0.001)
    #     mouse.release(Button.left)
    #     time_sleep(random.random())
    # mouse_position(1090,1100,408,413)
    # mouse_click(2)

    # for i in range(10):
    #     pixelColor=get_pixel_color(1337,850)
    #     if(pixelColor[0]>10):
    #         #关卡位置
    #         mouse_position(758,768,296,299)
    #         mouse_click(0.5)
    #     else: break
    # time_sleep(random.random())

    print("作战第3章")
    for i in range(1):
        time_sleep(random.random())
        mouse.position=(49,300)
        mouse.press(Button.left)
        for i in range(mouse.position[0],1020):
            # for j in range(mouse.position[1],finaly):
                mouse.position=(i,300)
                time_sleep(0.001)
        
        mouse.release(Button.left)
        time_sleep(random.random())
    # # S3
    mouse.position=(280+random.randint(1,5),515+random.randint(1,5))
    mouse_click(1)
    # S3-4
    for i in range(10):
        pixelColor=get_pixel_color(1337,850)
        if(pixelColor[0]>10):
            mouse_position(750,810,552,552)
            mouse_click(0.5)
        else: break
    time_sleep(random.random())
#自动刷本
def autoClearStage(frange,trange,count):
    for san in range(count):
        # # #开始行动1
        mouse_position(1371,1383,843,846)
        mouse_click(2)
        pixelColor=get_pixel_color(1453,629)
       
        if(pixelColor[0]>240 and pixelColor[1]>240 and pixelColor[2]>240):
            backwards()
            time_sleep(0.5)
            break
        # # #开始行动2
        mouse_position(1320,1325,557,567)
        mouse_click(random.randint(frange,trange))

        # # #结束按键范围
        mouse_position(789,1156,325,486)
        mouse_click(random.randint(3,5))

    for i in range(3):
        backwards()
        time_sleep(0)
    time_sleep(2)
#黄金
def testinandout(x1,x2,y1,y2):
    mouse_position(x1,x2,y1,y2)
    mouse_click(1.5)
    pixelColor=get_pixel_color(504,269)
    print(pixelColor)
    if(pixelColor[2]<200):
        time_sleep(1.5)
        backwards()
        normalize()

def gold():
    gold_pos=[417,424]
    time.sleep(1)
    testinandout(gold_pos[0]-4,gold_pos[0]+5,gold_pos[1]-2,gold_pos[1]+2)
    testinandout(gold_pos[0]-200,gold_pos[0]-200+random.randint(1,12),gold_pos[0]+222,gold_pos[0]+222+random.randint(1,4))
    testinandout(gold_pos[0],gold_pos[0]+random.randint(1,12),gold_pos[0]+222,gold_pos[0]+222+random.randint(1,4))
    testinandout(gold_pos[0]+200,gold_pos[0]+200+random.randint(1,12),gold_pos[0]+222,gold_pos[0]+222+random.randint(1,4))
    backwards()
    time_sleep(2)
#日常任务working
def get_daliy_points():
    for tab in range(2):
        if(tab==0):
            mouse_position(934,941,750,762)
            mouse_click(0.5)
        if(tab==1):
            mouse_position(1000,1005,60,82)
            mouse_click(0.5)
        pixelColor=get_pixel_color(1360, 183)
        #????????
        while(pixelColor[0]<40):
            if(pixelColor[1]<50 and pixelColor[2]<60):
                mouse_click(2)
            if(pixelColor[1]>100 and pixelColor[2]>100):
                time_sleep(1)
                mouse_position(1358,1368,200,210)
                pixelColor=get_pixel_color(1105,231)
                if(pixelColor[0]==152 or pixelColor[0]==238):
                    break
                mouse_click(1)
            pixelColor=get_pixel_color(1360, 183)
    backwards()
#好友信用
def friends_credit():
    mouse_position(428,438,748,751)
    mouse_click(1.5)
    mouse_position(84,94,295,297)
    mouse_click(1.5)
    mouse_position(1224,1229,210,213)
    mouse_click(5)
    pixelColor=get_pixel_color(1507,858)
    while(pixelColor[0]>200):
        mouse_position(1433,1442,795,800)
        mouse_click(5)
        pixelColor=get_pixel_color(1507,858)
    backwards()
    mouse_position(1231,1235,655,659)
    mouse_click(5)
    backwards()
    #(1506, 862)
    # (209, 88, 6)ju
    #(44, 44, 44)hei

if __name__ == "__main__":
    print(mouse.position)
    for i in range(10):
        curx,cury=pyautogui.position()
        pixelColor=get_pixel_color(curx,cury)
        print(pixelColor)
       
    # vm()
    # init()
    # friends_credit()
    # market()
    # credit()
    # house()
    # normalize()
    # gold()
    # house()

    # normalize()
    # trade() 
    # public_recuit()

    # battle()
    # setting()
    autoClearStage(130,135,6)
    
    # get_daliy_points()
    

    #仓库1天倒计时坐标颜色
    #(1492, 768)
    #(120, 40, 62)