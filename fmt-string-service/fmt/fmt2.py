import math

import numpy as np
import networkx as nx
from scipy.spatial import cKDTree
from pqdict import pqdict


class FMTPlanner():
    def __init__(
        self,
        map_design: np.ndarray,
        energy_map: np.ndarray,
        n_samples: int = 1000,
        r_n: float = 20.0,
        path_resolution: float = 0.1,
        rr: float = 1.0,
        max_search_iter: int = 10000,
        seed: int = 0,
    ):
        """
        Fast Marching Tree Path Planner 

        Args:
            map_design (np.ndarray): Obstacle map described by a binary image. 1: free nodes; 0: obstacle nodes
            energy_map (np.ndarray): The energy of each point in map_design
            n_samples (int, optional): Number of nodes to sample. Defaults to 1000.
            r_n (float, optional): Range to find neighbor nodes. Defaults to .0.
            path_resolution (float, optional): Resolution of paths to check collisions. Defaults to 0.1.
            rr (float, optional): Distance threshold to check collisions. Defaults to 1.0.
            max_search_iter (int, optional): Number of maximum iterations. Defaults to 10000.
            seed (int, optional): Random seed. Defaults to 0.
        """

        # hyperparameters
        self.map_size = map_design.shape
        self.energy_map = energy_map
        self.path_resolution = path_resolution
        self.rr = rr
        self.n_samples = n_samples
        self.r_n = r_n
        self.max_search_iter = max_search_iter
        self.prng = np.random.RandomState(seed)  # initialize PRNG

        # construct obstacle tree
        obstacles = np.argwhere(map_design == 0)
        self.obstacles_tree = cKDTree(obstacles)

        # initialize graph
        self.graph = nx.Graph()
        self.node_list = list()
        i = 0
        while len(self.node_list) < self.n_samples:
            node = self.prng.uniform(0, self.map_size)
            if self.check_collision(node, node):
                nodeN = node.tolist()
                nodeN.append(float(energy_map[int(node[0])][int(node[1])]))
                nodeN = np.asarray(nodeN)
                self.node_list.append(nodeN)
                self.graph.add_node(i)
                i += 1

    def plan(self,
             start: np.ndarray,
             goal: np.ndarray,
             heuristic_weight: int = 0.0) -> dict:
        """
        Run path planning

        Args:
            start (np.ndarray): Start location
            goal (np.ndarray): Goal location
            heuristic_weight (int, optional): Weight for Euclidean heuristics. Defaults to 0.0.

        Returns:
            dict:Containing path, number of steps required, and goal flag
        """
        start.append(round(float(self.energy_map[int(start[0])][int(start[1])]),2))
        goal.append(round(float(self.energy_map[int(goal[0])][int(goal[1])]),2))
        start = np.asarray(start)
        goal = np.asarray(goal)
        assert self.check_collision(start, start)
        assert self.check_collision(goal, goal)

        self.graph.remove_edges_from(list(self.graph.edges))
        start_id = len(self.node_list)
        goal_id = start_id + 1
        for n_steps, node in zip([start_id, goal_id], [start, goal]):
            self.graph.add_node(n_steps)
            self.node_list.append(node)
        node_tree = cKDTree(self.node_list)
        heuristic = [np.linalg.norm(x - goal) for x in self.node_list]

        # initialize
        goal_flag = 0
        z = start_id
        V_open = pqdict({z: 0.})
        V_closed = list()
        V_unvisited = list(range(len(self.node_list)))
        V_unvisited.remove(z)

        # start search
        for n_steps in range(self.max_search_iter):
            if z == goal_id:
                print("Reached goal")
                goal_flag = 1
                break
            N_z = node_tree.query_ball_point(self.node_list[z], self.r_n)
            X_near = list(set(N_z) & set(V_unvisited))
            for x in X_near:
                N_x = node_tree.query_ball_point(self.node_list[x], self.r_n)
                Y_near = list(set(N_x) & set(V_open))
                y_min = Y_near[np.argmin([V_open[y] for y in Y_near])]
                list_y_main = list(self.node_list[y_min])
                if int(list_y_main[2]) == 0:
                    continue
                if self.check_collision(self.node_list[y_min],
                                        self.node_list[x]):
                    self.graph.add_edge(y_min, x)
                    if x in V_open:
                        V_open.updateitem(
                            x, V_open[y_min] +
                            np.linalg.norm(self.node_list[y_min] -
                                           self.node_list[x]))
                    else:
                        V_open.additem(
                            x, V_open[y_min] +
                            np.linalg.norm(self.node_list[y_min] -
                                           self.node_list[x]))
                    V_unvisited.remove(x)
            V_open.pop(z)
            V_closed.append(z)
            if len(V_open) == 0:
                print("Search failed")
                break
            z = V_open.top()

        path = np.vstack([
            self.node_list[x]
            for x in nx.shortest_path(self.graph, start_id, z)
        ])

        return {
            "path": path,
            "n_steps": n_steps,
            "goal_flag": goal_flag,
        }

    def check_collision(self, src: np.ndarray, dst: np.ndarray) -> bool:
        """
        Check collision

        Args:
            src (np.ndarray): Source node
            dst (np.ndarray): Destination node

        Returns:
            bool: True if no collisions were found and False otherwise
        """
        srcN = src.tolist()
        if len(srcN) == 3:
            srcN.pop()
            src = np.asarray(srcN)
        else:
            src = np.asarray(srcN)
        dstN = dst.tolist()
        if len(dstN) == 3:
            dstN.pop()
            dst = np.asarray(dstN)
        else:
            dst = np.asarray(dstN)
        if np.all(src == dst):
            return self.obstacles_tree.query(src)[0] > self.rr
        pr = self.path_resolution
        dx, dy = dst[0] - src[0], dst[1] - src[1]
        yaw = math.atan2(dy, dx)
        d = math.hypot(dx, dy)
        steps = np.arange(0, d, pr).reshape(-1, 1)
        pts = src + steps * np.array([math.cos(yaw), math.sin(yaw)])
        pts = np.vstack((pts, dst))
        return bool(self.obstacles_tree.query(pts)[0].min() > self.rr)
