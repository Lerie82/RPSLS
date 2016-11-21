import curses


class Window(object):
    width = 800
    height = 600

    screen = None
    window = None

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.setup()

    def setup(self):
        """
        Sets up the terminal with a window. Waiting to be drawn on.
        :return: None
        """
        self.screen = curses.initscr()

        curses.noecho()  # Don't echo user input
        curses.cbreak()  # React to key-presses instantly
        self.screen.keypad(1)  # Makes it easier to get access to keys like 'KEY_LEFT', etc.

        # Create the window
        self.window = curses.newwin(self.height, self.width, 0, 0)

    def drawText(self, text: str):
        self.screen.addstr(0, 0, text)

    def refresh(self):
        self.screen.refresh()

    def exit(self):
        """
        Reverses the changes made to terminal in setup() and exits the rendering context.
        :return: None
        """

        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
