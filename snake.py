import curses
import time
import datetime
import random

# init settings
stdscr = curses.initscr()
curses.noecho()
curses.curs_set(False)

screen_height, screen_width = stdscr.getmaxyx()


stdscr.addstr(1, 0, "-"*(screen_width))

snake = [(screen_height//2, screen_width//2)]
food = (random.randint(3, screen_height-2), random.randint(1, screen_width-2))

direction = "u"

start_time = time.time()

stdscr.addstr(0, 0, "Snake Game in CLI")

start_text = " (WASD TO START)"
stdscr.addstr(0, screen_width//2 - len(start_text)//2, start_text)

elapsed_time = time.time() - start_time
elapsed_timedelta = datetime.timedelta(seconds=elapsed_time)
timedelta_string = str(elapsed_timedelta)
minutes, seconds = divmod(elapsed_timedelta.total_seconds(), 60)
timer_text = "{:0>2}:{:0>2}".format(int(minutes), int(seconds))
stdscr.addstr(0, screen_width - len(timer_text), timer_text)

while True:
    key = stdscr.getch()

    if key == ord("w") and direction != "d":
        direction = "u"
    elif key == ord("s") and direction != "w":
        direction = "d"
    elif key == ord("a") and direction != "r":
        direction = "l"
    elif key == ord("d") and direction != "l":
        direction = "r"

    stdscr.clear()

    for y, x in snake:
        stdscr.addstr(y, x, "S")

    stdscr.addstr(food[0], food[1], "*")

    # top bar with basic stats
    stdscr.addstr(0, 0, "Snake Game in CLI")

    score_text = "SCORE: " + str(len(snake))
    stdscr.addstr(0, screen_width//2 - len(score_text)//2, score_text)

    elapsed_time = time.time() - start_time
    elapsed_timedelta = datetime.timedelta(seconds=elapsed_time)
    timedelta_string = str(elapsed_timedelta)
    minutes, seconds = divmod(elapsed_timedelta.total_seconds(), 60)
    timer_text = "{:0>2}:{:0>2}".format(int(minutes), int(seconds))
    stdscr.addstr(0, screen_width - len(timer_text), timer_text)

    stdscr.addstr(1, 0, "-"*(screen_width))

    stdscr.timeout(150)
    stdscr.refresh()

    y, x = snake[0]
    if direction == "u":
        y -= 1
    elif direction == "d":
        y += 1
    elif direction == "l":
        x -= 1
    elif direction == "r":
        x += 1
    snake.insert(0, (y, x))

    if snake[0] == food:
        food = (random.randint(3, screen_height-2),
                random.randint(1, screen_width-2))
    else:
        snake.pop()

    # collision with a border
    if y == 1 or y == screen_height-1 or x == 0 or x == screen_width-1:
        break

    # collision with itself
    for a, b in snake[1:]:
        if y == a and x == b:
            break

curses.endwin()

print("GAME OVER!\n\nFINAL SCORE: " + str(len(snake)))