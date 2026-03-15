import tkinter as tk
import configparser
import os

# Path to the configuration file
CONFIG_DIR = "conf"
CONFIG_FILE = os.path.join(CONFIG_DIR, "configuration.ini")
CONFIG_SECTION = "settings"
CONFIG_KEY_CHOICE = "choice"


class ConfigApp:
    def __init__(self, parent):
        # Create a Toplevel window attached to the parent (Welcome window)
        self.window = tk.Toplevel(parent)
        self.window.title("Configuration")
        self.window.resizable(False, False)

        # Variable to hold the choice field value
        self.choice = tk.StringVar()

        # Load existing value from file before building the UI
        self._load_config()

        self._build_ui()

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------

    def _build_ui(self):
        """Build the configuration form UI."""
        frame = tk.Frame(self.window, padx=30, pady=30)
        frame.pack()

        # Choice label and input field
        tk.Label(frame, text="Choice:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.choice, width=25).grid(row=0, column=1, pady=5)

        # Save button
        tk.Button(
            frame,
            text="Save",
            width=15,
            command=self._on_save
        ).grid(row=1, column=0, columnspan=2, pady=15)

    # ------------------------------------------------------------------
    # Config file handling
    # ------------------------------------------------------------------

    def _load_config(self):
        """Read conf/configuration.ini and populate the choice field if the file exists."""
        config = configparser.ConfigParser()

        if os.path.isfile(CONFIG_FILE):
            config.read(CONFIG_FILE)
            saved_value = config.get(CONFIG_SECTION, CONFIG_KEY_CHOICE, fallback="")
            self.choice.set(saved_value)

    def _on_save(self):
        """Save the choice value to conf/configuration.ini and close the window."""
        choice_value = self.choice.get()

        # Create the conf directory if it does not exist
        os.makedirs(CONFIG_DIR, exist_ok=True)

        # Write the value to the INI file
        config = configparser.ConfigParser()
        config[CONFIG_SECTION] = {CONFIG_KEY_CHOICE: choice_value}

        with open(CONFIG_FILE, "w") as config_file:
            config.write(config_file)

        # Close the configuration window
        self.window.destroy()
