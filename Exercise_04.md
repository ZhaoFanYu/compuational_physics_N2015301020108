# Exercise_04
## 张健 2015301020108
### 题目:2.9题
![](https://github.com/2739515436/compuational_physics_N2015301020108/blob/master/%24MU%40R%5BAWX8%24VDZE%24%40UP~%401O.png)
### 分析
首先通过图像判断出射程最远时对应角度所在区间，再在所得区间内求出最远时的角度
先用下述程序画出角度分别为30、40、50度时的图像
```python
import matplotlib.pyplot as plt
import math
def area(v_0, theta_0):
    v_x_0 = v_0 * math.cos(theta_0)
    v_y_0 = v_0 * math.sin(theta_0)
    x_0 = 0
    y_0 = 0
    x_i = x_0
    y_i = y_0
    v_x_i = v_x_0
    v_y_i = v_y_0              
    delta_t = 0.1
    drag_0 = 4 * (10 **(-5))     
    list_x = []
    list_y = []
    list_x.append(x_i)
    list_y.append(y_i)         
    while(1):
        drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5
        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)
        x_iplus = x_i + v_x_i * delta_t
        y_iplus = y_i + v_y_i * delta_t
        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t
        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t
        if y_iplus < 0:
            x_final = x_i - y_i * ((x_i - x_iplus) / (y_i - y_iplus))
            y_final = 0
            list_x.append(x_final)
            list_y.append(y_final)
            break
        else:
            x_i = x_iplus
            y_i = y_iplus
            v_x_i = v_x_iplus
            v_y_i = v_y_iplus
            list_x.append(x_i)
            list_y.append(y_i)
    plt.plot(list_x,list_y,label = theta_0 * 180 / math.pi)
    plt.legend()
    plt.title(u"Cannon shell trajectory") 
    plt.xlabel(u"x(m)")
    plt.ylabel(u"y(m)")
    return x_final
area(700,math.pi * 40 / 180)
area(700,math.pi * 30 / 180)
area(700,math.pi * 50 / 180)
```
图像如下

![](https://github.com/2739515436/compuational_physics_N2015301020108/blob/master/20171016083439.png)

可以判断出距离最远时角度在30到50度之间
再用下述程序求出最远距离
```python
import math
def area(v_0, theta_0):
    v_x_0 = v_0 * math.cos(theta_0)
    v_y_0 = v_0 * math.sin(theta_0)
    x_0 = 0
    y_0 = 0
    x_i = x_0
    y_i = y_0
    v_x_i = v_x_0
    v_y_i = v_y_0             
    delta_t = 0.1
    drag_0 = 4 * (10 **(-5))     
    list_x = []
    list_y = []
    list_x.append(x_i)
    list_y.append(y_i)        
    while(1):
        drag_i = drag_0 * ((1 - y_i * (6.5 * 10 **(-3)) / 300) ** (2.5))   #a=6.5*10^(-3)K/m, T=300K, α=2.5
        v_i = math.sqrt(v_x_i ** 2 + v_y_i ** 2)
        x_iplus = x_i + v_x_i * delta_t
        y_iplus = y_i + v_y_i * delta_t
        v_x_iplus = v_x_i - drag_i * v_i * v_x_i * delta_t
        v_y_iplus = v_y_i - drag_i * v_i * v_y_i * delta_t - 9.8 * delta_t
        if y_iplus < 0:
            x_final = x_i - y_i * ((x_i - x_iplus) / (y_i - y_iplus))
            y_final = 0
            list_x.append(x_final)
            list_y.append(y_final)
            break
        else:
            x_i = x_iplus
            y_i = y_iplus
            v_x_i = v_x_iplus
            v_y_i = v_y_iplus
            list_x.append(x_i)
            list_y.append(y_i)
    return x_final
area_max = area(700,math.pi * 30 / 180)
for i in range(21):
    n = i + 30
    area_2 = area(700,math.pi * n / 180)
    if area_max >= area_2:
        max_angle = 30
    else:
        area_max = area_2
        max_angle = n
print("when the range is maximun of %d m"%(area_max))
print("the angle is %d"%(max_angle))
```
### 结论
角度为40度时，最远距离为24522m
