def get_rules():
    """
    Creates traversal rules for the board in environment b

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

    # Center column
    set_tile(6, 7, ["up"], prompt="Start")
    set_tile(6, 6, ["up"])
    set_tile(6, 5, ["up"])
    set_tile(6, 4, ["up"])
    set_tile(6, 3, ["up"])
    set_tile(6, 2, ["up"])

    # Top row
    set_tile(3, 1, ["left", "right"])
    set_tile(4, 1, ["left", "right"])
    set_tile(5, 1, ["left", "right"], warn="Green has no eggs")
    set_tile(6, 1, ["left", "right"])
    set_tile(7, 1, ["left", "right"])
    set_tile(8, 1, ["left", "right"])
    set_tile(9, 1, ["left", "right"])

    # Left column
    set_tile(1, 2, ["down"])
    set_tile(1, 3, ["down"])
    set_tile(1, 4, ["down"])
    set_tile(1, 5, ["down"])
    set_tile(1, 6, ["down"])
    set_tile(1, 7, ["down"])

    # Right column
    set_tile(11, 2, ["down"])
    set_tile(11, 3, ["down"])
    set_tile(11, 4, ["down"])
    set_tile(11, 5, ["down"])
    set_tile(11, 6, ["down"])
    set_tile(11, 7, ["down"])

    # Bottom row
    set_tile(1, 7, ["right"])
    set_tile(2, 7, ["right"])
    set_tile(3, 7, ["right"])
    set_tile(4, 7, ["right"])
    set_tile(5, 7, ["right"])
    set_tile(7, 7, ["left"])
    set_tile(8, 7, ["left"])
    set_tile(9, 7, ["left"])
    set_tile(10, 7, ["left"])
    set_tile(11, 7, ["left"])

    # Goals
    set_tile(1, 1, ["right"], goal=True, color=(0, 128, 0))
    set_tile(2, 1, ["right"], goal=True, color=(0, 128, 0))
    set_tile(10, 1, ["left"], goal=True, color=(128, 0, 128))
    set_tile(11, 1, ["left"], goal=True, color=(128, 0, 128))

    return rules
