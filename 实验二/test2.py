import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #从零开始到3Π结束
y = np.sin(x) #y是关于X的正弦信号

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #在第一行到第二列的第一个
plt.title(r'$f(x)=sin(x)$') #在上方出现该正弦信号的函数注释
plt.plot(x, y) #用于画图它可以绘制点和线, 并且对其样式进行控制.画出图形一
#plt.show()

x1 = [t*0.375*np.pi for t in x] #第二个波形为将X中的出入转换的t中变成关于t的格式输出
y1 = np.sin(x1) #输出关于x1的函数值
plt.subplot(1,2,2) ##在第一行到第二列的第2个
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1) #画出图形二
plt.show() #输出显示图一和图二