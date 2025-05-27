# File opening and processing

from sklearn.cluster import KMeans
import numpy as np
import fmt2
import matplotlib.pyplot as plt
import stringmethod
import time

def muller_brown(x, y):
    a = [-1, -1, -6.4, 0.7]
    b = [0, 0, 11, 0.6]
    c = [-10, -10, -6.5, 0.7]
    A = [-200, -100, -170, 15]
    x_bar = [1, 0, -0.5, -1]
    y_bar = [0, 0.5, 1.5, 1]

    value = 0
    for i in range(4):
        value += A[i] * np.exp(a[i] * (x - x_bar[i]) ** 2 + b[i] * (x - x_bar[i]) * (y - y_bar[i]) + c[i] * (y - y_bar[i]) ** 2)
    return value

x = np.linspace(-1.5, 1.2, 100)
y = np.linspace(-0.2, 2, 100)
xx, yy = np.meshgrid(x, y)
V = muller_brown(xx, yy)
'''
V是传入参数，一个二维表格
上面的代码是生成测试数据用的，你需要解析传入的文件来填充V
你会收到一个txt文本文件，前两列数据是网格上的坐标，第三列数据是同一行前两列坐标对应的值
'''
S = stringmethod.String2D(x, y, V)
S2 = stringmethod.String2D(x, y, V)

start = time.perf_counter()

x_min = -1.5
y_min = -0.2
x_step = 0.027
y_step = 0.022

V_list, x_list, y_list = list(V), list(x), list(y)
points = []
weight = []
energy = []
rows, cols = V.shape
for i in range(rows):
    for j in range(cols):
        if V_list[i][j] < -100:
            points.append([x_list[i],y_list[j]])
            energy.append(V_list[i][j])
            weight.append((V_list[i][j])**10)

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(points,sample_weight=weight)
time_clus = time.perf_counter()

for i in kmeans.cluster_centers_:
    for j in range(len(points)):
        if ((i[0]-points[j][0])**2 + (i[1]-points[j][1])**2) < 5e-4:
            print(points[j])
            print(energy[j])
            print(int((points[j][1]-y_min)/y_step))
            print(int((points[j][0]-x_min)/x_step))
            break

map_design = [[ 1 for _ in range(100)] for _ in range(100)]
map_design_ = np.array(map_design)


planner = fmt2.FMTPlanner(map_design_, V, n_samples=5000, r_n=8, path_resolution=0.01, rr=1.0, max_search_iter=100000)
path_info = planner.plan([73,34],[10,77])

fmt_time = time.perf_counter()

path = path_info['path']
pathX, pathY, pathE, pathX_c, pathY_c = [], [], [], [], []
mult = 5

pathL = list(path)
for i in range(len(pathL)):
    pathL[i] = list(pathL[i])
    pathX.append(pathL[i][0]*x_step+x_min)
    pathY.append(pathL[i][1]*y_step+y_min)
    pathE.append(pathL[i][2])

for i in range(len(pathX)):
    if i < len(pathX)-1:
        for j in range(mult):
            pathX_c.append(pathX[i] + j/mult*(pathX[i+1]-pathX[i]))
            pathY_c.append(pathY[i] + j/mult*(pathY[i+1]-pathY[i]))
    else:
        pathX_c.append(pathX[-1])
        pathY_c.append(pathY[-1])

for i in range(len(pathX_c)):
    pathX_c[i] = y_min + y_step*((pathX_c[i]-x_min)/x_step)
    pathY_c[i] = x_min + x_step*((pathY_c[i]-y_min)/y_step)

pathX_ = np.asarray(pathX_c)
pathY_ = np.asarray(pathY_c)
string = np.vstack([pathX_, pathY_]).T
string[:,[0,1]] = string[:,[1,0]]
maxsteps = 30
tol = 0.01
S.compute_mep(begin=[-0.558, 1.442], end=[0.623, 0.028], maxsteps=maxsteps, traj_every=1, npts=len(pathX_c), init_guess = string,
              x_min = x_min, y_min = y_min, x_step = x_step, y_step = y_step, flexible=True, tol = tol)
path_data = np.vstack([pathX, pathY, pathE]).T
print(path_data)
time_FMT = time.perf_counter()

# S2.compute_mep(begin=[-0.558, 1.442], end=[0.623, 0.028], maxsteps=maxsteps, traj_every=1, npts=len(pathX_c), init_guess = [],
#               x_min = x_min, y_min = y_min, x_step = x_step, y_step = y_step, flexible=True, tol = None)
time_iter = time.perf_counter()
S.plot_mep(clip_max=200, levels=20)
plt.show()
# S2.plot_mep(clip_max=200, levels=20)
# plt.show()
plt.figure()
'''
把path_data里的数据输出成类似输入的三列：x坐标 y坐标 的txt文本文件
输出上面绘图器输出的图片
'''


'''iterations = [i+1 for i in range(maxsteps)]
error = S.plot_error()
error2 = S2.plot_error()
iterations = np.asarray(iterations)
plt.yscale("log")
plt.plot(iterations, error, label = 'FMT guess')
plt.plot(iterations, error2, label = 'linear guess')
plt.legend()
plt.show()'''

print('The FMT time is ' + "{:.3f}".format(time_FMT-start))
# print('The linear time is ' + "{:.3f}".format(time_iter-time_FMT+time_clus-start))