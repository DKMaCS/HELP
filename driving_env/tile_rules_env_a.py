def get_rules():
    """
    Creates traversal rules for the board in environment a

    :return:
    Dict of traversal rules for the environment to enforce
    """

    rules = {}

    def set_tile(x, y, allowed_dirs, goal=False, prompt=None, color=None, warn=None):
        all_dirs = {"up", "down", "left", "right"}
        rules[(x, y)] = {
            "block": list(all_dirs - set(allowed_dirs))
        }
        if goal:
            rules[(x, y)]["goal"] = True
            if color:
                rules[(x, y)]["color"] = color
        if prompt:
            rules[(x, y)]["prompt"] = prompt
        if warn:
            rules[(x, y)]["warn"] = warn

    # Center column from start
    set_tile(6, 8, ["up"], prompt="Start")
    set_tile(6, 7, ["up"])
    set_tile(6, 6, ["up"])
    set_tile(6, 5, ["left", "right"])

    # Bottom row left of center column
    set_tile(5, 5, ["left"])
    set_tile(4, 5, ["left"])
    set_tile(3, 5, ["left", "right"], goal=True, prompt="Goal achieved", color=(0, 0, 255))
    set_tile(2, 5, ["left", "right"], goal=True, prompt="Goal achieved", color=(0, 0, 255))

    # Left column
    set_tile(1, 5, ["right", "up"])
    set_tile(1, 4, ["up", "down"])
    set_tile(1, 3, ["up", "down"])
    set_tile(1, 2, ["up", "down"])
    set_tile(1, 1, ["down", "right"]) # dummy goal for time being

    # Bottom row right of center column
    set_tile(7, 5, ["right"], warn="Orange lot full")
    set_tile(8, 5, ["right"])
    set_tile(9, 5, ["left", "right"], goal=True, color=(255, 165, 0))
    set_tile(10, 5, ["left", "right"], goal=True, color=(255, 165, 0))

    # Right column
    set_tile(11, 5, ["up", "left"])
    set_tile(11, 4, ["up", "down"])
    set_tile(11, 3, ["up", "down"])
    set_tile(11, 2, ["up", "down"])
    set_tile(11, 1, ["down", "left"])

    # Top row
    set_tile(2, 1, ["right", "left"])
    set_tile(3, 1, ["right", "left"])
    set_tile(4, 1, ["right", "left"])
    set_tile(5, 1, ["right", "left"])
    set_tile(6, 1, ["right", "left"])
    set_tile(7, 1, ["right", "left"])
    set_tile(8, 1, ["right", "left"])
    set_tile(9, 1, ["right", "left"])
    set_tile(10, 1, ["right", "left"])

    return rules

