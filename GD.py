import numpy as np
import random

class GradientDescent():
    def __init__(self, 
                 learning_rate, 
                 max_iterations, 
                 cov_threshold, 
                 energy_map,
                 x_grid,
                 y_grid):
        # hyperparameters
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.convergence_threshold = cov_threshold
        self.energy_map = energy_map
        self.x_grid = x_grid
        self.y_grid = y_grid


    # Numerical gradient function
    def numerical_gradient(self,energy_map, x, y, x_grid, y_grid,r1):
        if energy_map[x+r1][y] == 0 or energy_map[x-r1][y] == 0:
            grad_x = 0.
        else:
            grad_x = (energy_map[x+r1][y] - energy_map[x-r1][y]) / (2*r1*x_grid)
        if energy_map[x][y+1] == 0 or energy_map[x][y-1] == 0:
            grad_y = 0.
        else:
            grad_y = (energy_map[x][y+r1] - energy_map[x][y-r1]) / (2*r1*y_grid)
        return np.array([grad_x, grad_y])

    def GradientDescentPlanning(self,start_point,batch_size):
        # Gradient Descent loop

        path  = [start_point]

        for i in range(self.max_iterations):
            x = int(path[-1][0])
            y = int(path[-1][1])
            grad = 0
            for j in range(batch_size):
                r1 = random.randint(1,5)
                grad += self.numerical_gradient(self.energy_map, x, y, self.x_grid, self.y_grid,r1)
            grad = grad/batch_size
            new_position_x = int(path[-1][0] - self.learning_rate * grad[0])
            new_position_y = int(path[-1][1] - self.learning_rate * grad[1])
            new_position = [int(new_position_x), int(new_position_y)]
            path.append(new_position)
            # Check for convergence
            gradN = np.asarray(grad)
            if np.linalg.norm(gradN) < self.convergence_threshold and grad[0] != 0. and grad[1] != 0.:
                break

        path = np.array(path)

        return path