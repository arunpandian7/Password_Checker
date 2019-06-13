from os import listdir
import time


# Brute Force Function
pswrd_files = [f for f in listdir('password DB//') if f.endswith('.txt')]
i = 0
attempt = 0


def brute(password_set):
    global attempt
    global i
    start = time.time()
    f = open('password DB//'+pswrd_files[i],'r')
    txts = f.read()
    f_list = txts.split('\n')
    for letter in f_list:
        attempt += 1
        if letter == password_set:
            end = time.time()
            time_taken = end - start
            f.close()
            return attempt, time_taken


def cracker(pswd):
    global i
    while True:
        try:
            tries, timetaken = brute(pswd)
            print('Yeah boi')
            return True, tries, timetaken
            break
        except (TypeError, UnicodeDecodeError):
            i += 1
        except IndexError:
            return False, 0, 0


