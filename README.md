## Pyrogram

> [!NOTE]
> Unfortunately, the original pyrogram is no longer supported. I will try to be your @delivrance.

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()
```

**Pyrogram** is a modern, elegant and asynchronous [MTProto API](https://docs.kurigram.live/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Key Features

- **Ready**: Install Pyrogram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Monkeygram Extensions

This fork includes additional methods for handling long messages:

``` python
# Send long messages (auto-split if > 4096 chars)
await client.send_long_message(chat_id, very_long_text)

# Edit with auto-split
await message.edit_long_message(very_long_text)
```

Parameters:
- `max_length` - Maximum length per message (default: 4096)
- `delay` - Delay between sending parts (default: 0.5s)
- `preserve_lines` - Preserve line formatting when splitting (default: True)
- `disable_web_page_preview` - Disable link previews (default: True)

### Installing

Stable version

``` bash
pip3 install git+https://github.com/deadboizxc/monkeygram.git
```

Dev version
``` bash
pip3 install https://github.com/deadboizxc/monkeygram/archive/dev.zip --force-reinstall
```
