import random_word_gen as rwg
import Morse_Gen as mg
import time
import machine
from machine import I2C

from ht16k33 import HT16K33Segment14

buzzer = machine.PWM(machine.Pin(20))
button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

button_value = 0

i2c1 = I2C(0,scl=machine.Pin(9),sda=machine.Pin(8))
display0 = HT16K33Segment14(i2c1,board=HT16K33Segment14.ECBUYING_054)
display0.set_brightness(2)
display0.clear()

i2c2 = I2C(1,scl=machine.Pin(11),sda=machine.Pin(10))
display1 = HT16K33Segment14(i2c2,board=HT16K33Segment14.ECBUYING_054)
display1.set_brightness(2)
display1.clear()

def play_tone(frequency, duration, buzzer):
    buzzer.freq(frequency)     # Set the pitch (e.g., 440 for A4)
    buzzer.duty_u16(32768)     # Set volume (50% duty cycle is standard)
    time.sleep_ms(duration)    # Play for a set time
    buzzer.duty_u16(0)

def play_morse(morse):
    
    global button_value
    
    for i in range (len(morse)):
        print ("nl")
        time.sleep(0.7)
        for x in range (len(morse[i])):
            if button.value() == 0:
                print ("MutedS")
                if button_value == 1:
                    button_value = 0
                    
                else:
                    button_value = 1
                    
                time.sleep(0.1)
                return (1)
            
            if button_value == 1:
                return ("")
                
                
            if morse[i][x] == ".":
                print (0)
                play_tone(440, 500, buzzer)
                time.sleep(0.2)
                        
            elif morse[i][x] == "-":
                print (1)
                play_tone(300, 1000, buzzer)
                time.sleep(0.2)
                        
            else:
                print ("Error")
                    
    return (0)

def play_morse_verse(mv):
    global button_value
    
    for x in range (len(morse[i])):
        if button.value() == 0:
            print ("Muted")
            if button_value == 1:
                button_value = 0
                    
            else:
                button_value = 1
                    
            time.sleep(0.1)
            return (1)
            
        if button_value == 1:
            return ("")
                
                
        if morse[i][x] == ".":
            print (0)
            play_tone(440, 500, buzzer)
            time.sleep(0.2)
                        
        elif morse[i][x] == "-":
            print (1)
            play_tone(300, 1000, buzzer)
            time.sleep(0.2)
                        
        else:
            print ("Error")

i = 0

while True:
    word_og = (rwg.Generate_Word())
    morse = mg.String_To_Morse(word_og)
    
    word  = word_og.upper()
    print (word)
    print (morse)
    
 #   play_morse(morse)

    display1.update()
    display0.update()
    display0.clear()
    display1.clear()
    
    if (len(word)) > 4:
        word1 = word[:4]
        word2 = word[4:]
        
        for i in range (4):
            play_morse_verse(morse[i])
            display0.set_character(word1[i], i, False)
            display0.update()
            time.sleep(1)
            
        for i in range (len(word2)):
            play_morse_verse(morse[i+4])
            display1.set_character(word2[i], i, False)
            display1.update()
            time.sleep(1)
            
        display0.clear()
        display1.clear()
        display1.update()
        display0.update()
        
    else:
        for i in range (len(word)):
            play_morse_verse(morse[i])
            display0.set_character(word[i], i, False)
            display0.update()
            time.sleep(1)
        
        display0.clear()
        display0.update()
    
    