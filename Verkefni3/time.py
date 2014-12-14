#1

# import time
# import sys

# toolbar_width = 40

# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

# for i in range(toolbar_width):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()

# sys.stdout.write("\n")



#2
# import time

# import sys

 

# def do_task():

#     time.sleep(1)

 

# def example_1(n):

#     steps = n/10

#     for i in range(n):

#         do_task()

#         if i%steps == 0:

#             print ('\b.'),

#             sys.stdout.flush()

#     print(' Done!')

     

# print('Starting ')

# sys.stdout.flush()

# example_1(100)

#3
# import time
# import sys

# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r%d%%" % i)
#     sys.stdout.flush()



# from tkinter import *
# import ttk
# root = Tk()
# progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
# progressbar.pack(side="bottom")
# progressbar.start()
# root.mainloop()

# from tkinter import *
# import tkinter
# import ttk

# root = tkinter.Tk()
# progressbar = ttk.Progressbar(orient=VERTICAL, length=300, mode='determinate', variable='Hallo')
# progressbar.pack(side="bottom")

# progressbar.start()
# # root.mainloop()
# for x in range(1,100):
# 	print('Hallo')	

# progressbar.stop()
