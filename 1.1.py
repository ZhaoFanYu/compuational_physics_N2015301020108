import numpy as np

import matplotlib.pyplot as plt







v = []





for i in range(0,1001):

    if i == 0:

        velocity_i = 0

        v.append(velocity_i)

    else:

        velocity_iplus = velocity_i - 0.01 * 9.8

        velocity_i = velocity_iplus

        v.append(velocity_iplus)

        if i == 200:

            t = 2

            plt.plot(t,velocity_i,'sb')

            print("t=",t,"时","v=",velocity_i)

        elif i == 400:

            t = 4

            plt.plot(t,velocity_i,'sb')

            print('t=',t,'时','v=',velocity_i)

        elif i == 600:

            t = 6

            plt.plot(t,velocity_i,'sb')

            print('t=',t,'时','v=',velocity_i)

        elif i == 800:

            t = 8

            plt.plot(t,velocity_i,'sb')

            print('t=',t,'时','v=',velocity_i)      

            



t = np.linspace(0,10,1001)

plt.plot(t,v)          







t = np.linspace(0,10)

Velocity = (-9.8) * t

plt.plot(t,Velocity)   





plt.show()
