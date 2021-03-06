from gps3 import gps3
from math import degrees, radians, cos, sin, asin, sqrt
from geopy import distance
from balldetectClient import getball
import time,serial
import pyproj
from magneto import get_imu_head
g = pyproj.Geod(ellps='WGS84')
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
ser = serial.Serial(port='/dev/ttyTHS2',baudrate = 38400)

global val
det = 0
val = "NOTFOUND" 
def detect():
        val = getball()
        if(val=="Found"):
                print("FOUND bveurgv uergcergcnrnergqgfcoegognncrgcrxg" )
                brute_stop()
                #det = ()
                if det == 0:
                    while(val!="Found"):
                                val=getball()
                                print("moving clockwise ball found once checking")
                                clockwise()
                elif det < 200:
                    quit()
                elif det < 400:
                    for i in range (2):
                                print("moving straight ball found")
                                straight_slow(4)
                        ser.write('f')
                        quit()
                elif det < 600:
                    for i in range (4):
                                print("moving straight ball found")
                                straight_slow(4)
                        ser.write('f')
                        quit()

                val = getball()
                print("ball found 1 stage")
                if(val=="Found"):
                        for i in range (2):
                                print("moving straight ball found")
                                straight_slow(4)
                        ser.write('f')
                        quit()
                else:
                        while(val!="Found"):
                                val=getball()
                                print("moving clockwise ball found once checking")
                                clockwise()
                        for i in range (2):
                                print("moving straight ball found")
                                straight()
                        ser.write('f')
                        quit()                
                print(val)
                #quit()

def straight():
    stm_send='m8x4999y0000z'
    print ('Going straight')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def straight_slow(p):
    stm_send='m'+str(p)+'x4999y0000z'
    print ('Going straight')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def anticlockwise():
    stm_send='m5x0000y4999z'
    print('Rotating anticlockwise')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def clockwise():
    stm_send='m5x9999y4999z'
    print('Rotating clockwise')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def clockwise1():
    stm_send='m5x9999y4999z'
    print('Rotating clockwise')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def backward():
    stm_send='m5x4999y9999z'    
    print('Going backward')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())
def brute_stop():
    stm_send='m4x4999y4999z'
    print('Brute Stop')
    ser.write(stm_send.encode())
    ser.write(stm_send.encode())

def pos_update():
    while True:
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                global latitude,longitude
                latitude =  data_stream.TPV['lat']
                longitude =  data_stream.TPV['lon']
                if type(longitude) is type('sdas') or type(latitude) is type('sdas'):
                    continue                 
                #print(latitude,longitude)
                return latitude,longitude
        break  
def get_heading():
    startlat,startlong=pos_update()
    (az12, az21, dist) = g.inv(startlong, startlat, endlong, endlat)
    if az12<0:
        az12=az12+360
    return az12, dist
def match_head():
    waypoint_heading,dist=get_heading()    
    while True:
        #waypoint_heading_opp=waypoint_heading+180
        imu_heading=get_imu_head()
        heading_diff=imu_heading-waypoint_heading
        #print(imu_heading,waypoint_heading,heading_diff)
        print('heading_diff',heading_diff)
        #detect()
        if imu_heading < waypoint_heading+15 and imu_heading>waypoint_heading-15:
                #brute_stop()
                break
        if heading_diff >=-180:
                if heading_diff<=0:
                        clockwise()
        if heading_diff <-180:
                anticlockwise()
        if heading_diff>=0:
                if heading_diff<180:
                        turn = 2 
                        anticlockwise()             
        if heading_diff >= 180:
                turn = 1
                clockwise()
def matchdist():
        try:
            while True:
                match_head()
                waypoint_heading,waypoint_dist=get_heading()
                # if waypoint_dist>3:
                #     print('Matching Distance',waypoint_dist)
                #     straight()
                #     #detect()
                # elif waypoint_dist>3:
                #     print('Matching Distance',waypoint_dist)
                #     straight_slow()
                #     #detect()

                if waypoint_dist > 20:
                    print('Matching Distance',waypoint_dist)
                    straight()
                elif waypoint_dist > 10:
                    print('Matching Distance',waypoint_dist)
                    straight_slow(5)
                elif waypoint_dist > 3:
                    print('Matching Distance',waypoint_dist)
                    straight_slow(4)
                #elif waypoint_dist > 6:
                #    print('Matching Distance',waypoint_dist)
                #    straight_slow(3)
                #elif waypoint_dist > 6:
                #    print('Matching Distance',waypoint_dist)
                #    straight_slow(2)

                else:
                    brute_stop()
                    break
        except KeyboardInterrupt:
                brute_stop()

def match_head_BD():
    waypoint_heading,dist=get_heading()    
    while True:
        #waypoint_heading_opp=waypoint_heading+180
        imu_heading=get_imu_head()
        heading_diff=imu_heading-waypoint_heading
        #print(imu_heading,waypoint_heading,heading_diff)
        print('heading_diff',heading_diff)
        detect()
        if imu_heading < waypoint_heading+15 and imu_heading>waypoint_heading-15:
                #brute_stop()
                break
        if heading_diff >=-180:
                if heading_diff<=0:
                        clockwise()
        if heading_diff <-180:
                anticlockwise()
        if heading_diff>=0:
                if heading_diff<180:
                        turn = 2 
                        anticlockwise()             
        if heading_diff >= 180:
                turn = 1
                clockwise()
def matchdist_BD():
        try:
            while True:
                match_head_BD()
                waypoint_heading,waypoint_dist=get_heading()
                if waypoint_dist>2:
                    print('Matching Distance',waypoint_dist)
                    straight_slow(5)
                    detect()
                else:
                    brute_stop()
                    break
        except KeyboardInterrupt:
                brute_stop()
                
def clock_turn():
        h=get_imu_head()
        z=0
        while z-h <90:
                n=get_imu_head()
                if n<h:
                        z=360+n
                else:
                        z=n
                clockwise1()
                val=getball()
                #if(val == "Found"):
                 #       brute_stop()
                  #      print(val,"Ball detected")
                   #     quit()
                detect()

                      


def anti_turn():
    h = get_imu_head()
    n = get_imu_head()
    if h>90:
        while abs(h-n)<90:
            anticlockwise()
            n =get_imu_head()
    else:
        while n>=0:
            anticlockwise()
            n=get_imu_head()
        while (360+h-n)<90:
            anticlockwise()
            n=get_imu_head()


global startlat,startlong
startlat,startlong=pos_update()
global endlat,endlong
endlat=13.3505976
endlong=74.7916358
matchdist()

#for i in range (1):
#        print("moving straight ball found")
#        straight_slow(4)
#exit()

print("Ball search starting")
startlat,startlong=pos_update()
x = startlat
y = startlong
way = []
r = 6
# plt.plot(x,y,marker='o',markersize=5, color='red')
for i in range(0, 361, 60):
    cx = cos(radians(i))*r/111035 + x
    cy = sin(radians(i))*r/111035 + y
    a = []
    a.append(cx)
    a.append(cy)
    way.append(a)
    print("way", way)
    # plt.plot(cx,cy,marker='o',markersize=3, color='green')
    # plt.draw()
    # plt.pause(0.001)
for i in range(len(way)):
    for j in range(0,4):
        clock_turn()
    endlat = way[i][0]
    endlong = way[i][1]
    matchdist_BD()
    print(i, "REACHED!!!!!!")

r = 10
# plt.plot(x,y,marker='o',markersize=5, color='red')
for i in range(0, 361, 60):
    cx = cos(radians(i))*r/111035 + x
    cy = sin(radians(i))*r/111035 + y
    a = []
    a.append(cx)
    a.append(cy)
    way.append(a)
    print("way", way)
    # plt.plot(cx,cy,marker='o',markersize=3, color='green')
    # plt.draw()
    # plt.pause(0.001)
for i in range(len(way)):
    for j in range(0,4):
        clock_turn()
    endlat = way[i][0]
    endlong = way[i][1]
    matchdist_BD()
    print(i+6, "REACHED!!!!!!")

