def get_rules():
    return {
        (0, 5): {"prompt": "Env B: Tunnel entrance"},
        (4, 4): {"goal": True, "prompt": "Env B: Welcome to the bunker!"},
        (5, 0): {"block": ["down"]},
    }