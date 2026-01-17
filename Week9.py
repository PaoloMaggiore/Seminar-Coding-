# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
# plt.show()
#
#
# from matplotlib.lines import linesStyles










# import matplotlib.pyplot as plt
#
# def display_line(x,y):
#      plt.plot(x,y)
#      plt.show()
#
# def run_task():
#      x_values = [1,2,3,4,5]
#      y_values = [6,7,8,9,10]
#      display_line(x_values,y_values)
#
# plt.show()





# task 2
# import matplotlib.pyplot as plt
#
# def small():
#     x= [3,3,4,4,3]
#     y= [3,4,4,3,3]
#
#     plt.plot(x,y, 'r:o')
#
# def medium():
#     x= [2,2,5,5,2]
#     y= [2,5,5,2,2]
#     plt.plot(x,y, 'g--s')
#
#
#
# def large():
#     x= [1,1,6,6,1]
#     y= [1,6,6,1,1]
#     plt.plot(x,y, 'b--s')
#
# def run_task():
#     small()
#     medium()
#     plt.show()
# run_task()


# task 3

# def coordinate():
#     print("enter X value:")
#     x = int(input())
#
#     print("enter Y value:")
#     y = int(input())
#
#     return (x,y)
# def path():
#     print("retrieving path...")
#     x_value = []
#     y_value = []
#
#     for i in range(4):
#         data=coordinate()
#         x_value.append(data[0])
#         y_value.append(data[1])
#
#     return [x_value, y_value]
#
# def run_task():
#     value = path()
#     plt.plot(value[0], value[1], "r--o")
#     plt.show()
#
# run_task()


