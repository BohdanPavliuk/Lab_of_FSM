"""Module of description student`s day in UCU"""

import random
import time as tme
def sleeping(time):
    """State of sleeping"""
    if time in range(6, 9) and random.random() < 0.45:
        print("Just watching a dream")
        return sleeping
    elif time == 9 and random.random() < 0.7:
        print("Oh, nice, I wake up in time")
        return washing_up

    elif time == 10:
        print("Okay, I'm late, have to go")
        return studying

    elif time == 2:
        print("Time to sleep, what a pleasure day")
        return sleeping
    elif time == 20:
        print("Enough to sleep")
        print("Want to talk to someone")
        return socialize

    print("zzzz....")
    return sleeping

def washing_up(time):
    """State of washing_up"""
    if time == 10:
        print("Don`t forget to brush your teeth")
        return eating
    elif time == 1:
        print("Taking shower")
        return sleeping

def eating(time):
    "State of taking food"
    if time == 11:
        print("English breakfast?...")
        return studying

    elif time == 15:
        if random.random() < 0.5:
            print("It`s time to studying after launch")
            return studying
        else:
            print("Hmm, walking in park after potato?")
            return walking

def studying(time):
    """State of studying"""
    print("Studying....")
    if random.random() > 0.68:
        print('Time to smoke for a while')
    if time == 14:
        print('Okay, time to eat')
        return eating
    elif time == 0:
        print('Oh, feeling so tired')
        print('Time to prepare for bed')
        return washing_up
    elif time in range(16, 19) and random.random() < (time - 16) * 0.1 + 0.3:
        print("Short nap doesn`t seems to be a bad idea")
        return sleeping
    elif time == 19:
        print("Lets go to Collegium, want to talk to someone")
        return socialize
    print("Preparing to exams")
    return studying

def socialize(time):
    """State of socializing"""
    print("What we are talking about?... Communism?")
    if time == 22:
        if random.random() > 0.3:
            print("Oh, there are some deadlines, i need to finished")
            return studying
        else:
            print("Feel tired, lets watch funny tiktoks")
            return wasting_time
    return socialize

def wasting_time(time):
    """State of wasting time"""
    if random.random() > 0.68:
        print('Time to smoke for a while')
    if time == 0:
        print('Time to preparing for bed')
        return washing_up
    print("What a ridiculuois cats")
    return wasting_time

def walking(time):
    """State of walking"""
    print("The weather is so nice")
    print("Let`s continue studying")
    return studying

class MyDay:
    """Class of my day. Start state is sleeping"""
    def __init__(self):
        self.cur_state = sleeping

    def day(self):
        """My day from 6 a.m. to 3 a.m"""
        for hour in range(6, 28):
            tme.sleep(1)
            print(f'It`s {hour % 24} o`clock')
            self.cur_state = self.cur_state(hour % 24)


if __name__ == '__main__':
    myday = MyDay()
    myday.day()
