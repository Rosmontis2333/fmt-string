import fmt
import utils
import os

cwd = os.getcwd()
map_design = utils.load_map_design(cwd + "/map.png", size=[400, 200])

planner = fmt.FMTPlanner(map_design, n_samples=1000, r_n=20, path_resolution=0.1, rr=1.0, max_search_iter=10000)
path_info = planner.plan([180, 20], [20, 380])
utils.visualize_result(map_design, planner, path_info)