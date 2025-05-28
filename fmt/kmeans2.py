# File opening and processing

from sklearn.cluster import KMeans
import numpy as np
import fmt2
import stringmethod
import time
import copy

def camelback(coords):

    assert isinstance(coords,np.ndarray)
    assert coords.shape[-1] == 2
    
    ndims = coords.ndim
    x, y = coords[(ndims-1)*(slice(None),)+(0,)], coords[(ndims-1)*(slice(None),)+(1,)]
    
    return - 425 * np.exp(-((x+1.75)**2/2+((y+2)**2/10))) - 445 *np.exp(-(((x-1.75)**2)/8+((y-1.5)**2))) - 40 * np.exp(-(((x+1.75)**2)+((y-1.75)**2)/2)) + 50 * np.exp(-(((x-1.75)**2)/3+((y+1.5)**2)/2))
x = np.arange(-2.5,2.5,0.05)
y = np.arange(-2.5,2.5,0.05)
coords = [x,y]
xx, yy = np.meshgrid(x,y)
V = camelback(np.swapaxes(np.array([xx,yy]),0,-1))
S = stringmethod.String2D(x, y, V)
S2 = stringmethod.String2D(x, y, V)


start = time.perf_counter()

x_min = -2.5
y_min = -2.5
x_step = 0.05
y_step = 0.05

V_list, x_list, y_list = list(V), list(x), list(y)
points = []
weight = []
energy = []
V_calc = copy.deepcopy(V_list)

for i in range(len(x)):
    for j in range(len(y)):
        V_calc[i][j] = V_calc[i][j]
        if V_list[i][j] < -400:
            points.append([x_list[i],y_list[j]])
            energy.append(V_list[i][j])
            weight.append((V_list[i][j])**10)

kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(points,sample_weight=weight)

time_clus = time.perf_counter()

for i in kmeans.cluster_centers_:
    for j in range(len(points)):
        if ((i[0]-points[j][0])**2 + (i[1]-points[j][1])**2) < 1e-3:
            print(points[j])
            print(energy[j])
            print(int((points[j][1]-y_min)/y_step))
            print(int((points[j][0]-x_min)/x_step))
            break

map_design = [[ 1 for _ in range(100)] for _ in range(100)]
map_design_ = np.array(map_design)
V_calc = np.asarray(V_calc)

planner = fmt2.FMTPlanner(map_design_, V_calc, n_samples=5000, r_n=20, path_resolution=0.01, rr=1.0, max_search_iter=100000)
path_info = planner.plan([9,14],[79,84])

fmt_time = time.perf_counter()

path = path_info['path']
pathX, pathY, pathE, pathX_c, pathY_c = [], [], [], [], []
mult = 4

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
maxsteps = 60

S.compute_mep(begin=[-1.8, -2.05], end=[1.7, 1.45], maxsteps=maxsteps, traj_every=1, npts=len(pathX_c), init_guess = string,
              x_min = x_min, y_min = y_min, x_step = x_step, y_step = y_step, flexible=True, tol = 0.01)

time_FMT = time.perf_counter()

S2.compute_mep(begin=[-1.8, -2.05], end=[1.7, 1.45], maxsteps=maxsteps, traj_every=1, npts=len(pathX_c), init_guess = [],
              x_min = x_min, y_min = y_min, x_step = x_step, y_step = y_step, flexible=True, tol = 0.01)

time_iter = time.perf_counter()
'''S.plot_mep(clip_max=200, levels=20)
plt.show()
S2.plot_mep(clip_max=200, levels=20)
plt.show()
plt.figure()
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
print('The linear time is ' + "{:.3f}".format(time_iter-time_FMT+time_clus-start))