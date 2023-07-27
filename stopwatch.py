from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button


class StopWatchApp(App):
    BINDINGS = [("d", "toggle_dark_mode", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header(name="Stopwatch", show_clock=True)
        yield Button("Start", name="start")
        yield Button("Stop", name="stop")
        yield Footer()

    def action_toggle_dark_mode(self):
        """Toggle dark mode on or off."""
        self.dark = not self.dark


if __name__ == "__main__":
    StopWatchApp().run()
