from os import listdir
import time


# Brute Force Function
pswrd_files = [f for f in listdir('password DB//') if f.endswith('.txt')]
print(pswrd_files)
i = 0
attempt = 0


def brute(password_set):
    global attempt
    global i
    start = time.time()
    while i < len(pswrd_files):
        f = open('password DB//'+pswrd_files[i],'r')
        txts = f.read()
        f_list = txts.split('\n')
        i += 1
        for letter in f_list:
            attempt += 1
            if letter == password_set:
                end = time.time()
                time_taken = end - start
                f.close()
                return True
    else:
        return False


def cracker(pswd):
    global i
    while True:
        try:
            flag = brute(pswd)
            return flag
        except (TypeError, UnicodeDecodeError):
            i += 1


