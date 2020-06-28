import time
import random
import os
from threading import Thread

class password(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global i
        characters = " !#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\\^_`abcdefghijklmnopqrstuvwxyz{|}~€,"
        percent = 0.0
        percent2 = 0.0
        password = ""
        user_input = int(input("longueur du mot de passe : "))

        for i in range(user_input) :
            a = random.randint(0,(len(characters) - 1))
            character = characters[a]
            password = password + character

            if i != 0 :
                percent = (i/user_input) * 100
                percent = round(percent, 1)
                if percent2 != percent :
                    percent2 = percent
                    print(str(percent) + " percent completed")

        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        f = open(os.path.join(__location__, 'password.txt'), "w+")
        print("Writing password in text file")
        f.write(password)
        print("Writing complete !")
        f.close()
        time.sleep(1)
        i = 0
        time.sleep(300)

# class calculator(Thread):

#     def __init__(self):
#         Thread.__init__(self)

#     def run(self):
#         global i
#         i = 0
#         buffer = 0
#         while True:
#             buffer = i
#             time.sleep(1)
#             buffer = i - buffer
#             if buffer < 0:
#                 buffer = 0
#             print(str(buffer) + " characters per second")

# starting threads
thread_1 = password()
# thread_2 = calculator()

thread_1.start()
# thread_2.start()

thread_1.join()
# thread_2.join()