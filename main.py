import tkinter as tk
from tkinter import messagebox


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.resizable(False, False)

        # Variables to store login credentials (persist across window switches)
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Reference to the welcome window (to avoid opening duplicates)
        self.welcome_window = None

        self._build_login_ui()

    def _build_login_ui(self):
        """Build the login form UI."""
        frame = tk.Frame(self.root, padx=30, pady=30)
        frame.pack()

        # Username field
        tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.username, width=25).grid(row=0, column=1, pady=5)

        # Password field — show="*" masks the input
        tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Entry(frame, textvariable=self.password, show="*", width=25).grid(row=1, column=1, pady=5)

        # Connect button
        tk.Button(
            frame,
            text="Connect",
            width=15,
            command=self._on_connect
        ).grid(row=2, column=0, columnspan=2, pady=15)

    def _on_connect(self):
        """Validate credentials, hide the login window, and open the welcome window."""
        username_value = self.username.get()
        password_value = self.password.get()

        # Basic validation
        if not username_value or not password_value:
            messagebox.showwarning("Missing fields", "Please enter both username and password.")
            return

        # Hide the login window (withdraw keeps it alive in memory)
        self.root.withdraw()

        # Open the welcome window
        self._open_welcome_window()

    def _open_welcome_window(self):
        """Open (or re-use) the welcome window."""
        # If the window already exists and is still open, just bring it to front
        if self.welcome_window and self.welcome_window.winfo_exists():
            self.welcome_window.deiconify()
            return

        self.welcome_window = tk.Toplevel(self.root)
        self.welcome_window.title("Welcome")
        self.welcome_window.resizable(False, False)

        # Intercept the window close button to also restore the login window
        self.welcome_window.protocol("WM_DELETE_WINDOW", self._on_welcome_close)

        tk.Label(
            self.welcome_window,
            text="Hello, world!",
            font=("Helvetica", 16),
            padx=40,
            pady=30
        ).pack()

        # Back to login button
        tk.Button(
            self.welcome_window,
            text="Login",
            width=15,
            command=self._on_back_to_login
        ).pack(pady=(0, 20))

    def _on_back_to_login(self):
        """Hide the welcome window and show the login window with fields pre-filled."""
        # Hide welcome window
        self.welcome_window.withdraw()

        # Fields already hold the previous values via StringVar — just show the window again
        self.root.deiconify()

    def _on_welcome_close(self):
        """Handle the welcome window X button: restore login window before closing."""
        self._on_back_to_login()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()