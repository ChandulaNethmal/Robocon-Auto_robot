from statemachine import StateMachine
import RPi.GPIO as GPIO
import time

Message_detector_pin = 18  # BCM pin 18, BOARD pin 12

#### Assign GPIO for 4 switches and Buton######
start_point=12
checkpoint1=13
checkpoint2=14
checkpoint3=15
restart_button=16


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
    #reading_Depth_sensor
    if sand_dune==True:
        newState = "sand_dune_detected"
    else :
        newState = "walking_in_gobi_1"    
    return (newState, txt)

def line2_checkpoint_trans(txt):      # Restarting checkpoint_1_reached 

    return (newState, txt)

def sand_dune_detected_trans(txt):    # Depth cam detected sand_dune and proceed climb
        
    #send Serial data to Teensy to climb step
    
    return (newState, txt)

def line3_checkpoint_trans(txt):      # Restarting checkpoint_2_reached 
    
    return (newState, txt)


def walking_in_gobi_2_trans(txt):      # Moving forward while line following and depth reading 

    #According to line follwing code send Serial data to Teensy
    #reading_Depth_sensor
    if checkpoinit3_==True:
        newState = "sand_dune_detected"
    else :
        newState = "walking_in_gobi_2"    
    return (newState, txt)

def mountain_urtu_trans(txt):         # Manually stoping and Restarting checkpoint_3_reached 

    return (newState, txt)

def climb_start_trans(txt):  #Read proximity input and start climbing

    #Reading proximity sensor to strat
    if start_deteted_==True:
        newState = "mountain_climb"
    else :
        newState = "mountain_climb_start"    
    return (newState, txt)    

def mountain_climb_trans(txt):  #Read proximity input and start climbing

    #Isuue ramp walking commands via serial to teensy
    #Run color detection script to find blue color
    if top_deteted_==True:
        newState = "reached_top"
    else :
        newState = "mountain_climb_start"    
    return (newState, txt)    
    return ("neg_state", "")

def reached_top_trans(txt):           #Detect blue color and stop robot at the top of moutain
    #Stop the robot and lift the message
    # issue command to arm for lift message
    return (newState, txt)



if __name__== "__main__":

    m = StateMachine()
   #m2= State_machine2()
    m.add_state("Start", start_trans)
    m.add_state("message_detected", message_detected_trans)
    m.add_state("walking_in_gobi_1", walking_in_gobi_1_trans) 
    m.add_state("line2_checkpoint", line2_checkpoint_trans)
    m.add_state("sand_dune_detected", sand_dune_detected_trans)
    m.add_state("line3_checkpoint", line3_checkpoint_trans)
    m.add_state("walking_in_gobi_2", walking_in_gobi_2_trans)
    m.add_state("mountain_urtu", mountain_urtu_trans)
    m.add_state("mountain_climb_start", mountain_climb_start_trans)
    m.add_state("reached_top", reached_top_trans)
    m.add_state("lift_message", None ,end_state=1)

    m.set_start("Start")

    m.run("Python is great")
    m.run("Python is difficult")
    m.run("Perl is ugly")
    
