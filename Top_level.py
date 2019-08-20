from statemachine import StateMachine
import RPi.GPIO as GPIO
import time

Message_detector_pin = 18  # BCM pin 18, BOARD pin 12
climb_starter_pin = 17  # BCM pin --, BOARD pin --

#### Assign GPIO for 4 switches and Buton######
start_point=12
checkpoint1=13
checkpoint2=14
checkpoint3=15
restart_button=16

count_line2=0
count_line3=0

# Pin Setup:
GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
GPIO.setup(Message_detector_pin, GPIO.IN)  # set pin as an input pin
GPIO.setup(climb_starter_pin, GPIO.IN)
GPIO.setup(start_point, GPIO.IN)
GPIO.setup(checkpoint1, GPIO.IN)
GPIO.setup(checkpoint2, GPIO.IN)
GPIO.setup(checkpoint3, GPIO.IN)
GPIO.setup(restart_button, GPIO.IN)

#Assuming that the line following code is realtime running in background

def start_trans(txt):     # wait_idle
    #reading_start_points_buttons
    return (newState, txt)


def message_detected_trans(txt):      # Readig message detector
    #detected=False
    #while detected==False:
    Message= GPIO.input(Message_detector_pin)
    if value == GPIO.HIGH:
        #detected=True
        #Send an arm grabbing string via serial
        newState = "walking_in_gobi"
    else :
        #detected =False
        newState = "message_detected"    
    return (newState, txt)


def walking_in_gobi_1_trans(txt):      # Moving forward while line following and depth reading 

    #According to line follwing code send Serial data to Teensy
    ###start searching line2

    if Line2_detected==True:
        newState = "line2_checkpoint"       
    else :
        newState = "walking_in_gobi_1"    
    return (newState, txt)

def line2_checkpoint_trans(txt):      # Restarting checkpoint_1_reached 
    if count_line2 == 0:
        ##turn 45 degree
        count_line2=+
    else:
    #According to line follwing code send Serial data to Teensy
    ##start depth searching for sand_dune
    ##start searching line3

    if sand_dune==True:
        newState = "sand_dune_detected"
         ##send Serial data to Teensy to climb step
        
    elif Line3_detected==True:
        newState = "line3_checkpoint"       
    else :
        newState = "line2_checkpoint"    
    return (newState, txt)

def sand_dune_detected_trans(txt):    # Depth cam detected sand_dune and proceed climb
        
    #send Serial data to Teensy to climb sand dune
    ##start searching line3
        
    if Line3_detected==True:
        newState = "line3_checkpoint"       
    else :
        newState = "sand_dune_detected"    
    return (newState, txt)    

def line3_checkpoint_trans(txt):      # Restarting checkpoint_2_reached 

    if count_line3 == 0:
        ##turn 45 degree
        count_line3=+
    ## According to line follwing code send Serial data to Teensy
    ## Start detecting Mountain urtu(BLUE zone)
    
    if mountain_urtu=True:
        newState = "mountain_urtu"       
    else :
        newState = "line3_checkpoint"    
    return (newState, txt)



def mountain_urtu_trans(txt):         # Manually stoping and Restarting checkpoint_3_reached 

    #Seding serial string to stop robot
    #start reading proximity sensor

    start_climb= GPIO.input(climb_starter_pin)
    if start_climb == GPIO.HIGH:
        newState = "mountain_climb"
    else :
        newState = "mountain_urtu"  
    
    return (newState, txt)


def mountain_climb_trans(txt):  #Read proximity input and start climbing

    #Isuue line_following commands via serial to teensy
    #Run color detection script to find blue color(top)
    
    if top_deteted_==True:
        newState = "reached_top"
    else :
        newState = "mountain_climb"    
    return (newState, txt)    

def reached_top_trans(txt):           #Detect blue color and stop robot at the top of moutain
    #Stop the robot and lift the message
    # issue command to arm for lift message
    return (newState, txt)



if __name__== "__main__":

    m = StateMachine()
    
    m.add_state("Start", start_trans)
    m.add_state("message_detected", message_detected_trans)
    m.add_state("walking_in_gobi_1", walking_in_gobi_1_trans) 
    m.add_state("line2_checkpoint", line2_checkpoint_trans)
    m.add_state("sand_dune_detected", sand_dune_detected_trans)
    m.add_state("line3_checkpoint", line3_checkpoint_trans)
    m.add_state("mountain_urtu", mountain_urtu_trans)
    m.add_state("mountain_climb", mountain_climb_start_trans)
    m.add_state("reached_top", reached_top_trans)
#    m.add_state("lift_message", None ,end_state=1)

    m.set_start("Start")

    m.run("Python is great")

    
