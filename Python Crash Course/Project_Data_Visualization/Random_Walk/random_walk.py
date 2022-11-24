from random import choice

class RandomWalk:
    '''A class to generate random walks'''

    def __init__(self, num_points = 5000):
        '''Initialize attributes of a walk'''
        self.num_points = num_points
        # Start point
        self.x_value = [0]
        self.y_value = [0]

    def get_step(self):
        '''Get step for walk'''
        direction = choice([1, -1])            
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""
    
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_value) < self.num_points:
        
            # Calculate the new position.
            x = self.x_value[-1] + self.get_step()
            y = self.y_value[-1] + self.get_step()
        
            self.x_value.append(x)
            self.y_value.append(y)