import gym
from gym import spaces
import numpy as np

class DrivingEnv(gym.Env):
    def __init__(self, tile_rules, width=10, height=10, start_position=(0, 0)):
        super().__init__()
        self.width = width
        self.height = height

        self.action_space = spaces.Discrete(4)  # up, down, left, right
        self.observation_space = spaces.Box(low=0, high=max(width, height), shape=(2,), dtype=np.int32)

        self.position = np.array(start_position)
        self.tile_rules = tile_rules if tile_rules else {}

    def reset(self, *, seed=None, options=None):
        self.position = np.array(self.position)
        info = {}
        return self.position, info

    def step(self, action):
        x, y = self.position
        blocked = self.tile_rules.get((x, y), {}).get("block", [])

        # Check if movement is blocked from current tile
        if self._direction_name(action) in blocked:
            return self.position, -1, False, {"blocked": True}

        # Predict new position
        new_x, new_y = x, y
        if action == 0 and y > 0:
            new_y -= 1  # Up
        elif action == 1 and y < self.height - 1:
            new_y += 1  # Down
        elif action == 2 and x > 0:
            new_x -= 1  # Left
        elif action == 3 and x < self.width - 1:
            new_x += 1  # Right

        # Check for warning on next tile
        tile_data = self.tile_rules.get((new_x, new_y), {})
        if "warn" in tile_data:
            return self.position, 0, False, {"warn": tile_data["warn"]}

        # Move player
        self.position = np.array([new_x, new_y])
        info = {}

        if "prompt" in tile_data:
            info["prompt"] = tile_data["prompt"]

        is_goal = tile_data.get("goal", False)
        done = is_goal
        reward = 10 if is_goal else 0

        return self.position, reward, done, info

    # def render(self, mode="human"):
    #     grid = np.full((self.height, self.width), ".")
    #     x, y = self.position
    #     grid[y][x] = "P"
    #     for row in grid:
    #         print(" ".join(row))
    #     print()

    @staticmethod
    def _direction_name(action):
        return ["up", "down", "left", "right"][action]
