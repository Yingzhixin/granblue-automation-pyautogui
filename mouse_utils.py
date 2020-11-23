import pyautogui


class MouseUtils:
    """
    Provides the utility functions needed to perform mouse-related actions.

    Attributes
    ----------
    mouse_speed (float): Time in seconds it takes for the mouse to move to the specified point.

    debug_mode (bool, optional): Optional flag to print debug messages related to this class. Defaults to True.

    Methods
    -------
    scroll_screen(x, y, scroll_clicks):
        Attempt to drag the screen down to reveal more UI elements from the provided x and y coordinates.

    move_and_click_point(x, y, mouse_speed = self.mouse_speed):
        Move the cursor to the specified point on the screen and clicks it.

    click_point_instantly(x, y):
        Click the specified point on the screen instantly.
    """

    def __init__(self, mouse_speed: float = 0.5, debug_mode: bool = False):
        super().__init__()

        self.mouse_speed = mouse_speed
        self.debug_mode = debug_mode

    def scroll_screen(self, x: int, y: int, scroll_clicks: int):
        """Attempt to scroll the screen to reveal more UI elements from the provided x and y coordinates.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            scroll_clicks (int): How much to scroll the screen. Positive for scrolling up and negative for scrolling down.

        Returns:
            None
        """
        if(self.debug_mode):
            print(
                f"[DEBUG] Now scrolling the screen from ({x}, {y}) by {scroll_clicks} clicks...")
        pyautogui.scroll(scroll_clicks, x=x, y=y)
        return None

    def move_and_click_point(self, x: int, y: int, mouse_speed: float = 0.0, mouse_clicks=1):
        """Move the cursor to the specified point on the screen and clicks it.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.
            mouse_speed (float, optional): Time in seconds it takes for the mouse to move to the specified point. Defaults to 0.

        Returns:
            None
        """
        if (mouse_speed <= 0.0):
            mouse_speed = self.mouse_speed
        pyautogui.moveTo(x, y, mouse_speed)
        pyautogui.click(clicks=mouse_clicks)
        return None

    def click_point_instantly(self, x: int, y: int):
        """Click the specified point on the screen instantly.

        Args:
            x (int): X coordinate on the screen.
            y (int): Y coordinate on the screen.

        Returns:
            None
        """
        pyautogui.click(x, y)
        return None