from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import CameraModule
from time import sleep
import cv2
import threading


curveVal=0
motor = Motor(2,3,4,17,22,27)

def getMeasurementInput():
    while True:
        global curveVal
        ## read image
        img = CameraModule.getImg()
        ## calculate translation required
        curveVal = getLaneCurve(img)

        maxVal = 0.8
        if curveVal>maxVal:curveVal = maxVal
        if curveVal<(-maxVal):curveVal = -maxVal

        cv2.waitKey(1)
        #print(curveVal)

def SetMeasurementOutput():
    while True:
        global curveVal

        if curveVal < -0.3:
            state = 1
        elif curveVal > 0.3:
            state = 2
        else:
            state = 0


        if (state == 0):
            # Move forward
            motor.move(0.6,0,0.2)
            #sleep(0.2)
            motor.move(0.0,0,0.2)
            # for 2 seconds
            # stop()
        elif (state == 1):
            # Turn Left
            motor.move(0.6,-0.6,0.2)
            #sleep(0.2)
            # for 1 seconds
            # stop()
        elif (state == 2):
            # Turm Right
            motor.move(0.6,0.6, 0.2)
            #sleep(0.2)
            # for 1 seconds
            # stop()

        motor.stop(0.5)
        print(curveVal)
        print("---")
        print(state)

t1 = threading.Thread(target=getMeasurementInput)
t2 = threading.Thread(target=SetMeasurementOutput)


if __name__ == '__main__':
    t1.start()
    t2.start()