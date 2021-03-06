#!/usr/bin/env python3

import sys
import os

WINDOW_WIDTH = 87
WINDOW_HEIGHT = 20

# Start up the engine, given that the
#   current standard output is not piped.
if not sys.stdin.isatty():
    print("Oomph, I can not be run from a piped output. Please run directly from a terminal.")
else:
    # If we start these imports on a screen that doesn't support curses, the program just crashes.
    from Engine import Engine
    from Scenes.Menu.MenuScene import MenuScene
    from Window import Window

    # If user specifies 'debug' as argument, start pydevd debugging.
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        import pydevd

        # Start debugging
        pydevd.settrace('localhost', port=34564, stdoutToServer=False, stderrToServer=True, suspend=False)
        os.environ['TERM'] = 'xterm'  # pydevd breaks this environment var, this fixes it again.

        # Create the environment for our game
        window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
        engine = Engine(window)

        engine.scene = MenuScene()  # First scene in the game.

        engine.start()  # Starts the main game loop.
        window.exit()  # Engine has stopped. Clean and exit window.
    elif len(sys.argv) > 1 and sys.argv[1] == "snake":  # Starting with snake as an argument bumps us right into snake
        from Scenes.Snake.SnakeScene import SnakeScene

        # Create the environment for our game
        window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
        engine = Engine(window)

        engine.scene = SnakeScene()  # First scene in the game.

        engine.start()  # Starts the main game loop.
        window.exit()  # Engine has stopped. Clean and exit window.
    else:
        # Create the environment for our game
        window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
        engine = Engine(window)

        engine.scene = MenuScene()  # First scene in the game.

        engine.start()  # Starts the main game loop.
        window.exit()  # Engine has stopped. Clean and exit window.
