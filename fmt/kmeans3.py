import os
import sys

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import stringmethod
import fmt2
import time

def parse_file(filepath):
    """解析外部输入文件，生成二维表格 V"""
    data = np.loadtxt(filepath)
    x, y, values = data[:, 0], data[:, 1], data[:, 2]
    grid_x = np.unique(x)
    grid_y = np.unique(y)
    V = np.zeros((len(grid_y), len(grid_x)))
    for i in range(len(x)):
        row = np.where(grid_y == y[i])[0][0]
        col = np.where(grid_x == x[i])[0][0]
        V[row, col] = values[i]
    return grid_x, grid_y, V

def save_path_data(path_data, filename):
    """保存路径数据到文本文件"""
    np.savetxt(filename, path_data, fmt='%.6f', header='x y energy')

def calculate(task_id):
    input_file_path = os.path.join("uploads", f"{task_id}.txt")
    x,y,V=parse_file(input_file_path)
    S = stringmethod.String2D(x, y, V)

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
                points.append([x_list[i], y_list[j]])
                energy.append(V_list[i][j])
                weight.append((V_list[i][j]) ** 10)

    kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto").fit(points, sample_weight=weight)

    for i in kmeans.cluster_centers_:
        for j in range(len(points)):
            if ((i[0] - points[j][0]) ** 2 + (i[1] - points[j][1]) ** 2) < 5e-4:
                print(points[j])
                print(energy[j])
                print(int((points[j][1] - y_min) / y_step))
                print(int((points[j][0] - x_min) / x_step))
                break

    map_design = [[1 for _ in range(100)] for _ in range(100)]
    map_design_ = np.array(map_design)

    planner = fmt2.FMTPlanner(map_design_, V, n_samples=5000, r_n=8, path_resolution=0.01, rr=1.0,
                              max_search_iter=100000)
    path_info = planner.plan([73, 34], [10, 77])


    path = path_info['path']
    pathX, pathY, pathE, pathX_c, pathY_c = [], [], [], [], []
    mult = 5

    pathL = list(path)
    for i in range(len(pathL)):
        pathL[i] = list(pathL[i])
        pathX.append(pathL[i][0] * x_step + x_min)
        pathY.append(pathL[i][1] * y_step + y_min)
        pathE.append(pathL[i][2])

    for i in range(len(pathX)):
        if i < len(pathX) - 1:
            for j in range(mult):
                pathX_c.append(pathX[i] + j / mult * (pathX[i + 1] - pathX[i]))
                pathY_c.append(pathY[i] + j / mult * (pathY[i + 1] - pathY[i]))
        else:
            pathX_c.append(pathX[-1])
            pathY_c.append(pathY[-1])

    for i in range(len(pathX_c)):
        pathX_c[i] = y_min + y_step * ((pathX_c[i] - x_min) / x_step)
        pathY_c[i] = x_min + x_step * ((pathY_c[i] - y_min) / y_step)

    pathX_ = np.asarray(pathX_c)
    pathY_ = np.asarray(pathY_c)
    string = np.vstack([pathX_, pathY_]).T
    string[:, [0, 1]] = string[:, [1, 0]]
    maxsteps = 30
    tol = 0.01
    S.compute_mep(begin=[-0.558, 1.442], end=[0.623, 0.028], maxsteps=maxsteps, traj_every=1, npts=len(pathX_c),
                  init_guess=string,
                  x_min=x_min, y_min=y_min, x_step=x_step, y_step=y_step, flexible=True, tol=tol)
    path_data = np.vstack([pathX, pathY, pathE]).T
    path_data_path = os.path.join("output", f"{task_id}.txt")
    with open(path_data_path, "w") as f:
        for row in path_data:
            # 将每行数据写入文件，用制表符分隔
            f.write("\t".join(map(str, row)) + "\n")

    time_FMT = time.perf_counter()

    S.plot_mep(clip_max=200, levels=20)
    img_path = os.path.join("output",f"{task_id}.png")
    plt.savefig(img_path)
    plt.show()
    plt.figure()
    '''
    把path_data里的数据输出成类似输入的三列：x坐标 y坐标 的txt文本文件
    输出上面绘图器输出的图片
    '''

    print('The FMT time is ' + "{:.3f}".format(time_FMT - start))

if __name__ == "__main__":
    task_id= sys.argv[1]
    calculate(task_id)
    pass
    # 示例：输入文件路径和输出文件路径