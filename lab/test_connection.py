import tclab
import time

def test_led(lab):
    ''' 
    Test led module intensity 
    '''
    intensity = 0
    for i in range(6):
        if intensity == 0:
            intensity = 100  
        else:
            intensity = 0
        lab.LED(intensity)
        time.sleep(1)

def test_sensors(lab):
    ''' 
    Test temperature sensors 
    '''
    print("T1 is: ", lab.T1)
    print("T2 is: ", lab.T2)


def test_actuators(lab):
    ''' 
    Test actuators 
    '''
    print("Q1 at 100 and Q2 at 50")
    lab.Q1(100)
    lab.Q2(50)
    print("Wait for 1 minute")
    time.sleep(60)
    test_sensors(lab)
    print("Turning off the heaters")
    lab.Q1(0)
    lab.Q2(0)   

with tclab.TCLab() as lab:
    # Defining max power por actuators (0 to 255)
    lab.P1 = 200
    lab.P2 = 100

    print("Test all modules")
    print("Testing led ...")
    lab.LED(0)
    test_led(lab)
    print("Testing sensors ...")
    test_sensors(lab)
    print("Testing actuators ...")
    test_actuators(lab)