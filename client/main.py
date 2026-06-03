from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
import config_parser

config = config_parser.ini_conf("client_config.ini")

class my_app(App):
    TITLE = "F12 Engineering - GlobalSynk - KiCAD/LCSC Libary Syncing"
    def compose(self):
        yield Header()

        if config.client.username == "":
            yield Static("no user loaded")
        else:
            yield Static(f"Welcome {config.client.username}")

        yield Button("Click me")
        yield Footer()

    def on_button_pressed(self):
        self.exit("Button clicked!")


if __name__ == "__main__":
    my_app().run()