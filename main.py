#!/usr/bin/env python
#
# Project: Video Streaming with Flask
# Author: Log0 <im [dot] ckieric [at] gmail [dot] com>
# Date: 2014/12/21
# Website: http://www.chioka.in/
# Description:
# Modified to support streaming out with webcams, and not just raw JPEGs.
# Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
# Credits: http://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.

from flask import Flask, render_template, Response, url_for, request, redirect
from camera import VideoCamera
import time
import threading
import cv2
import os
import backend

app = Flask(__name__)

timer = None   # For Threading
count = 0      # For transition of sequence

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('interface.html')

def gen(camera):
    
    timer = threading.Timer(5, add) # Start Sequence
    timer.start()

    while True:
        if count == 0:
           frame = camera.get_start()
           #frame = camera.get_default()
           #time.sleep(1)
           yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 1:
            frame = camera.get_default()
            #time.sleep(1)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 2:   
            frame = camera.get_starting()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\
                   r\n\r\n' + frame + b'\r\n\r\n')
        
        elif count == 3:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 4:
            frame = camera.get_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 5:
            frame = camera.get_frame2()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 6:
            frame = camera.get_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 7:
            frame = camera.get_frame3()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n') 

        elif count == 8:
            frame = camera.get_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')      	

        elif count == 9:
            frame = camera.get_frame4()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 10:
            frame = camera.get_image()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 11:
            frame = camera.get_frame5()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n') 

        elif count == 12:
        	frame = camera.get_saygoodbye()
        	yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 13:
        	frame = camera.get_default()
        	yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        elif count == 14:
        	frame = camera.get_end()
        	yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def add():
    global timer, count
    count = count + 1
    timer = threading.Timer(5, add2)  # 5 secs Sequence
    timer.start()

def add2():
    global timer, count
    count = count + 1
    timer = threading.Timer(5, add3) # 5 secs Sequence
    timer.start()

def add3():
    global timer, count
    count = count + 1
    timer = threading.Timer(10, add2) # 10 secs Sequence
    timer.start()

@app.route('/result')
def Score():

    templatepic = {}
    for i in range(1,6):
      templatepic["template{}".format(i)]=cv2.imread("Template{}.jpg".format(i), 0)
      # Declaring template image to compare

    edges = {}
    for i in range(1,6):
      edges["edges{}".format(i)] = cv2.Canny(cv2.imread("webcam{}.jpg".format(i),0),100,200)
      # Declaring Canny Detection Image to compare
    
    score = {}
    for i in range(1,6):
      score["{}".format(i)] = "/static/Correct.png"
      # Declaring Correct Image before comparison 

    height,width = templatepic["template1"].shape #Find shape of array to compare
    correctpercentage = 100 # Initialise Percentage
    counter = 0 # Keep Track of Wrong Attempts
    
    for number in range(1,6):
      for i in range(height):
        for j in range(width):
            if templatepic["template"+ str(number)][i][j] < 100 and edges["edges" + str(number)][i][j] > 150:
               score[str(number)] = "/static/Incorrect.png"
               correctpercentage = correctpercentage - 20
               counter = counter + 1
               # Compares the two images
               break
        if score[str(number)] == "/static/Incorrect.png":
        	break

    if counter == 0:
    	counter = "Great Job!"
    elif counter == 1:
    	counter = "Just a bit more!"
    elif counter < 5:
      counter = "Try Harder Next Time!"
    elif counter == 5:
    	counter = "Uh-Oh"

    return render_template('interface3.html', inside=score["1"], inside2=score["2"], 
    inside3=score["3"], inside4=score["4"], inside5=score["5"], 
    percentage=correctpercentage, statement=counter)


@app.route('/game')
def game():
    return render_template('interface2.html')


@app.route('/video_feed')
def video_feed():
    global timer, count
    count = 0
    if timer != None:
    	timer.cancel() # Reset the timer when webpage is reloaded
    
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/webcam')
def webcam():
	return backend.resultpic(imagename="webcam1", template="Template1")

@app.route('/webcam2')
def webcam2():
	return backend.resultpic(imagename="webcam2", template="Template2")

@app.route('/webcam3')
def webcam3():
	return backend.resultpic(imagename="webcam3", template="Template3")

@app.route('/webcam4')
def webcam4():
	return backend.resultpic(imagename="webcam4", template="Template4")

@app.route('/webcam5')
def webcam5():
	return backend.resultpic(imagename="webcam5", template="Template5")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

