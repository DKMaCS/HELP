import pygame
import time

TILE_SIZE = 50
GRID_WIDTH = 13
GRID_HEIGHT = 9
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT

COLORS = {
    "bg": (255, 255, 255),
    "path": (200, 200, 200),
    "goal": (255, 165, 0),
    "prompt": (100, 149, 237),
    "agent": (0, 0, 0),
}


def draw_grid(screen, tile_rules, agent_pos, car_image):
    arrow_color = (0, 0, 0)
    arrow_thickness = 2
    head_size = 5

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            rule = tile_rules.get((x, y), {})
            color = COLORS["bg"]
            if rule.get("goal"):
                color = rule.get("color", COLORS["goal"])
            elif (x, y) in tile_rules:
                color = COLORS["path"]

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            # Draw directional arrows
            if (x, y) in tile_rules:
                blocked = rule.get("block", [])
                allowed = {"up", "down", "left", "right"} - set(blocked)
                cx = x * TILE_SIZE + TILE_SIZE // 2
                cy = y * TILE_SIZE + TILE_SIZE // 2

                for direction in allowed:
                    if direction == "up":
                        end = (cx, cy - TILE_SIZE // 2 + 5)
                        pygame.draw.line(screen, arrow_color, (cx, cy), end, arrow_thickness)
                        pygame.draw.polygon(screen, arrow_color,
                                            [(end[0], end[1] - head_size), (end[0] - head_size, end[1]),
                                             (end[0] + head_size, end[1])])
                    elif direction == "down":
                        end = (cx, cy + TILE_SIZE // 2 - 5)
                        pygame.draw.line(screen, arrow_color, (cx, cy), end, arrow_thickness)
                        pygame.draw.polygon(screen, arrow_color,
                                            [(end[0], end[1] + head_size), (end[0] - head_size, end[1]),
                                             (end[0] + head_size, end[1])])
                    elif direction == "left":
                        end = (cx - TILE_SIZE // 2 + 5, cy)
                        pygame.draw.line(screen, arrow_color, (cx, cy), end, arrow_thickness)
                        pygame.draw.polygon(screen, arrow_color,
                                            [(end[0] - head_size, end[1]), (end[0], end[1] - head_size),
                                             (end[0], end[1] + head_size)])
                    elif direction == "right":
                        end = (cx + TILE_SIZE // 2 - 5, cy)
                        pygame.draw.line(screen, arrow_color, (cx, cy), end, arrow_thickness)
                        pygame.draw.polygon(screen, arrow_color,
                                            [(end[0] + head_size, end[1]), (end[0], end[1] - head_size),
                                             (end[0], end[1] + head_size)])

    x, y = agent_pos
    car_rect = car_image.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
    screen.blit(car_image, car_rect)

def run_visualizer(tile_rules, env):
    visualizer_log = []
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    car_image = pygame.image.load("assets/car.png").convert_alpha()
    car_image = pygame.transform.scale(car_image, (TILE_SIZE - 10, TILE_SIZE - 10))

    clock = pygame.time.Clock()
    running = True
    goal_reached = False

    font = pygame.font.SysFont(None, 24)

    current_warning = ""  # <-- Store warning across frames

    while running:
        screen.fill(COLORS["bg"])
        draw_grid(screen, tile_rules, env.position, car_image)

        # Draw warning if any
        if current_warning:
            warning_surface = font.render(f"{current_warning}", True, (255, 0, 0))
            screen.blit(warning_surface, (10, SCREEN_HEIGHT - 30))

        # Draw prompt if any
        x, y = env.position
        tile_data = tile_rules.get((x, y), {})
        prompt = tile_data.get("prompt", "")
        if prompt:
            prompt_surface = font.render(prompt, True, (0, 0, 0))
            screen.blit(prompt_surface, (10, SCREEN_HEIGHT - 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        done = False

        if keys[pygame.K_UP]:
            obs, reward, done, info = env.step(0)
            current_warning = info.get("warn", "")
            visualizer_log.append([time.time(), obs[0], obs[1], 'up', reward, str(info)])
        elif keys[pygame.K_DOWN]:
            obs, reward, done, info = env.step(1)
            current_warning = info.get("warn", "")
            visualizer_log.append([time.time(), obs[0], obs[1], 'down', reward, str(info)])
        elif keys[pygame.K_LEFT]:
            obs, reward, done, info = env.step(2)
            current_warning = info.get("warn", "")
            visualizer_log.append([time.time(), obs[0], obs[1], 'left', reward, str(info)])
        elif keys[pygame.K_RIGHT]:
            obs, reward, done, info = env.step(3)
            current_warning = info.get("warn", "")
            visualizer_log.append([time.time(), obs[0], obs[1], 'right', reward, str(info)])

        if done:
            goal_reached = True
            running = False

        clock.tick(10)

    pygame.quit()
    return visualizer_log, goal_reached


def draw_arrow(surface, x, y, direction, color=(0, 0, 0)):
    cx = x * TILE_SIZE + TILE_SIZE // 2
    cy = y * TILE_SIZE + TILE_SIZE // 2
    size = TILE_SIZE // 4

    if direction == "up":
        points = [(cx, cy - size), (cx - size//2, cy), (cx + size//2, cy)]
    elif direction == "down":
        points = [(cx, cy + size), (cx - size//2, cy), (cx + size//2, cy)]
    elif direction == "left":
        points = [(cx - size, cy), (cx, cy - size//2), (cx, cy + size//2)]
    elif direction == "right":
        points = [(cx + size, cy), (cx, cy - size//2), (cx, cy + size//2)]
    else:
        return

    pygame.draw.polygon(surface, color, points)

