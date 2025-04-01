import csv
from driving_env.base_env import DrivingEnv
from driving_env.tile_rules_env_a import get_rules as get_rules_a
from driving_env.tile_rules_env_b import get_rules as get_rules_b
from driving_env.visualizer import run_visualizer


def main():
    while True:
        choice = input("Which environment? (a/b): ").strip().lower()
        if choice == "a":
            rules = get_rules_a()
            env = DrivingEnv(tile_rules=rules, width=13, height=9, start_position=(6, 8))
            break
        elif choice == "b":
            rules = get_rules_b()
            env = DrivingEnv(tile_rules=rules, width=13, height=9, start_position=(6, 7))
            break
        else:
            print("Invalid choice. Please enter 'a' or 'b'.")


    obs = env.reset()
    action_log, goal_reached = run_visualizer(rules, env)

    with open("game_log.csv", mode="w", newline="") as logfile:
        writer = csv.writer(logfile)
        writer.writerow(["timestamp", "position_x", "position_y", "action", "reward", "info"])
        writer.writerows(action_log)

    if goal_reached:
        print("🎉 Goal reached in visualizer. Exiting...")
        return


if __name__ == "__main__":
    main()