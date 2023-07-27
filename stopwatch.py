from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Static


class TimeDisplay(Static):
    """Custom time display widget"""

    pass


class StopWatch(Static):
    """Custom Stopwatch widget"""

    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00", id="time_display")


class StopWatchApp(App):
    BINDINGS = [("d", "toggle_dark_mode", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield StopWatch()
        yield Footer()

    def action_toggle_dark_mode(self):
        """Toggle dark mode on or off."""
        self.dark = not self.dark


if __name__ == "__main__":
    StopWatchApp().run()
