#!/usr/bin/python
from Tkinter import *
import cv2
import os
import subprocess
from time import sleep


def colourpal():
	os.system("idle-python2.7 -r opencvcolour.py &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --name cam10"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 100 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())

def fan():
	os.system("/home/nvidia/./jetson_clocks.sh &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --name cam10"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 100 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())


def ball_detect():
	os.system("/home/nvidia/jetson-inference/build/aarch64/bin/./imagenet-camera --prototxt=$NET/deploy_class.prototxt --model=$NET/snapshot_iter_1230.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax &")
	os.system("idle-python2.7 -r /home/nvidia/ball_search.py &")
	os.system("idle-python2.7 -r /home/nvidia/laksh_map.py &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())




a = Tk()
a.title("MRM") 																																											


def motorcode():

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	os.system("idle-python2.7 -r tcp_send.py &")
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --name gear"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 1060 150 &"
	os.system(cmd)

	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	#print out
	for i in out.split():
		cmd="xdotool windowsize "+i.strip()+" 350 100 && xdotool windowmove "+i.strip()+" 0 97 &"
		print cmd
		os.system(cmd)
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	#os.system("xdotool search --onlyvisible --sync --classname --sync --name Python\ 2.7 windowminimize")



        
def close():
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	for i in out.split():
		os.system("xdotool windowactivate --sync "+i)
		os.system("xdotool getactivewindow windowkill")

#Button(a, text="DigitalCam9", command = digitalcam9, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 0)
Button(a, text="Colourpal", command = colourpal, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 1)
Button(a, text="Fan Bruh?", command = fan, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 4)
#Button(a, text="Map", command = map1, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 5)
Button(a, text="BallDetect", command = ball_detect, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 6)
#Button(a, text="Motorcode", command = motorcode, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=2)
#Button(a, text="Autonomous", command = Autonomous, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=3)
Button(a, text="Close All", command = close, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=7)

a.mainloop()

