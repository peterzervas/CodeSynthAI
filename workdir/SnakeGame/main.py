import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = generate_food_position()
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        direction = update_snake_position(direction, change_to)
        snake_pos, snake_body, score, food_spawn = check_collision(snake_pos, snake_body, score, food_spawn, food_pos, direction)

        if not food_spawn:
            food_pos = generate_food_position()
        food_spawn = True

        screen.fill(Config.BG_COLOR)
        for pos in snake_body:
            pygame.draw.rect(screen, Config.SNAKE_COLOR, pygame.Rect(pos[0], pos[1], Config.SNAKE_BLOCK, Config.SNAKE_BLOCK))

        pygame.draw.rect(screen, Config.FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], Config.SNAKE_BLOCK, Config.SNAKE_BLOCK))

        if snake_pos[0] < 0 or snake_pos[0] > Config.WINDOW_WIDTH-Config.SNAKE_BLOCK or snake_pos[1] < 0 or snake_pos[1] > Config.WINDOW_HEIGHT-Config.SNAKE_BLOCK:
            game_over(score, screen)

        for block in snake_body[1:]:
            if snake_pos == block:
                game_over(score, screen)

        show_score(score, screen)
        pygame.display.flip()
        clock.tick(Config.SNAKE_SPEED)

def game_over(score, screen):
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is {score}', True, Config.RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (Config.WINDOW_WIDTH/2, Config.WINDOW_HEIGHT/4)
    screen.fill(Config.BG_COLOR)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    sys.exit()

def show_score(score, screen):
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render(f'Score : {score}', True, Config.GREEN)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (Config.WINDOW_WIDTH / 10, 15)
    screen.blit(score_surface, score_rect)

if __name__ == "__main__":
    main()
