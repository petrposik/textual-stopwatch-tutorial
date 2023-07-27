from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button


class StopWatchApp(App):
    def compose(self) -> ComposeResult:
        yield Header(name="Stopwatch", show_clock=True)
        yield Button("Start", name="start")
        yield Button("Stop", name="stop")
        yield Footer()


if __name__ == "__main__":
    StopWatchApp().run()
