from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("Start Generating Session", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Bot Status and More Bots", url="https://t.me/jasebxall/15")],
        [
            InlineKeyboardButton("How to Use", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("More Info", url="https://t.me/Jasebxall")],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @Jasebxall
    """

    HELP = """
**Available Commands**

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @Jasebxall

Support : [Click Here](https://t.me/ixallsupport)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @jPipis
    """
