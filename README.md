
# Discord Remote Desktop Bot

A Python-based Discord bot that allows you to remotely view and control your desktop using Discord commands. The bot uses the `discord.py` library to interact with Discord and leverages Python libraries for desktop control and screenshot functionalities.

## Features

- **View Desktop**: Captures and sends screenshots of your desktop directly to a designated Discord channel.
- **Mouse Control**: Move the mouse to specific coordinates, simulate clicks, and perform drag-and-drop actions.
- **Keyboard Input**: Send keystrokes to type text or perform specific keyboard actions.
- **Live Updates**: Receive updated desktop screenshots after performing actions.
- **Secure Access**: Restricted to the bot owner for secure control.

---

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.10 or higher installed on your system
- A Discord bot token (see [Creating a Discord Bot](https://discordpy.readthedocs.io/en/stable/discord.html))
- Administrator permissions for the Discord server where the bot will be added

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/southwestfrance/discord-remote-desktop.git
   cd discord-remote-desktop
   ```

2. **Install Dependencies:**

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Token Variable:**

   Add the bot token into config.py:

   ```config.py
   TOKEN='token_here'
   ```

4. **Run the Bot:**

   Start the bot with the following command:

   ```bash
   python main.py
   ```

---

## Usage

### Bot Commands

Once the bot is running and added to your server, use the following commands:

- **`!screenshot`**: Captures the current desktop view and sends it to the channel.
- **`!mouse X Y`**: Moves the mouse to the specified coordinates (X, Y).
- **`!click`**: Simulates a mouse click at the current pointer location.
- **`!type <text>`**: Sends keystrokes to type the provided text.
- **`!press <key>`**: Press specific key.
- See https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys for valid keys


---

## Security Notes

- **Server Privacy:** Avoid using the bot in public Discord servers to prevent unauthorized access to your desktop.
- **Local Execution:** The bot must run on the computer you want to control.

---

## Limitations

- This bot does not support live streaming of the desktop; screenshots are the primary method of viewing.
- Commands may have slight latency depending on the internet connection and system performance.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Acknowledgments

- Built with [discord.py](https://discordpy.readthedocs.io/)
- Inspired by boredom and the need for lightweight remote desktop control.

---

## Disclaimer

Use this tool responsibly. The author is not liable for any misuse of this software.
