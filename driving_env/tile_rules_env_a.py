def get_rules():
    """
    Creates traversal rules for the board

    :return:
    Dict of traversal rules for the environment to enforce
    """

    rules = {}

    def set_tile(x, y, allowed_dirs, goal=False, prompt=None):
        all_dirs = {"up", "down", "left", "right"}
        rules[(x, y)] = {
            "block": list(all_dirs - set(allowed_dirs))
        }
        if goal:
            rules[(x, y)]["goal"] = True
        if prompt:
            rules[(x, y)]["prompt"] = prompt

    # === Vertical path ===
    set_tile(6, 8, ["up"], prompt="Start")
    set_tile(6, 7, ["up"])
    set_tile(6, 6, ["up"])
    set_tile(6, 5, ["left", "right"])

    # === Horizontal path left of center ===
    set_tile(5, 5, ["left"], prompt="Can't go right son")
    set_tile(4, 5, ["left"])
    set_tile(3, 5, ["left", "right"])
    set_tile(2, 5, ["left", "right"])

    # === Vertical down on far left ===
    set_tile(1, 5, ["right", "up"])
    set_tile(1, 4, ["up", "down"])
    set_tile(1, 3, ["up", "down"])
    set_tile(1, 2, ["up", "down"])
    set_tile(1, 1, ["down", "right"], goal=True, prompt="Ye made it!") # dummy goal for time being

    # === Horizontal path right of center ===
    set_tile(7, 5, ["right"])
    set_tile(8, 5, ["right"])
    set_tile(9, 5, ["left", "right"])
    set_tile(10, 5, ["left", "right"])

    # === Vertical down on far right ===
    set_tile(11, 5, ["up", "left"])
    set_tile(11, 4, ["up", "down"])
    set_tile(11, 3, ["up", "down"])
    set_tile(11, 2, ["up", "down"])
    set_tile(11, 1, ["down", "left"])

    # === Horizontal path up top ===
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

