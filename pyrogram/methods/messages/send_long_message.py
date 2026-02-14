#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
from typing import Union, List, Optional

import pyrogram
from pyrogram import enums
from pyrogram import types


class SendLongMessage:
    async def send_long_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        max_length: int = 4096,
        delay: float = 0.5,
        preserve_lines: bool = True,
        reply_to_message_id: Optional[int] = None,
        disable_web_page_preview: bool = True
    ) -> List["types.Message"]:
        """Send long messages by splitting them into parts if they exceed the maximum length.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            text (``str``):
                Text of the message to be sent. The message will be split into parts
                if its length exceeds max_length.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            max_length (``int``, *optional*):
                Maximum length of a single message. If the length of the text exceeds this limit,
                it will be split into several parts. Defaults to 4096.

            delay (``float``, *optional*):
                Delay between sending each part of the message (in seconds). Defaults to 0.5.

            preserve_lines (``bool``, *optional*):
                If True, the formatting of the lines will be preserved. Each line will be
                sent as a separate part. If False, the entire text will be split into parts
                based on max_length. Defaults to True.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message. Defaults to True.

        Returns:
            List of :obj:`~pyrogram.types.Message`: On success, a list of the sent messages is returned.

        Example:
            .. code-block:: python

                # Send a very long message that will be split automatically
                long_text = "Very long text..." * 1000
                await app.send_long_message("me", long_text)

                # Preserve line formatting
                await app.send_long_message("me", long_text, preserve_lines=True)
        """
        # Split text into parts while preserving lines
        if preserve_lines:
            parts = []
            current = ""
            for line in text.split('\n'):
                if len(current) + len(line) + 1 > max_length:
                    if current:
                        parts.append(current)
                        current = line
                    else:
                        # Line itself is too long, split it
                        parts.extend([line[i:i + max_length] for i in range(0, len(line), max_length)])
                else:
                    current = '\n'.join([current, line]) if current else line
            if current:
                parts.append(current)
        else:
            parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]

        # Send messages in parts
        messages = []
        for i, part in enumerate(parts):
            try:
                if i == 0:
                    # Send the first message with reply_to
                    msg = await self.send_message(
                        chat_id=chat_id,
                        text=part,
                        parse_mode=parse_mode,
                        disable_web_page_preview=disable_web_page_preview,
                        reply_to_message_id=reply_to_message_id
                    )
                else:
                    # Send remaining messages without reply_to
                    msg = await self.send_message(
                        chat_id=chat_id,
                        text=part,
                        parse_mode=parse_mode,
                        disable_web_page_preview=disable_web_page_preview
                    )
                messages.append(msg)
                # Delay between parts
                if i < len(parts) - 1 and delay > 0:
                    await asyncio.sleep(delay)
            except Exception:
                # If an error occurs, try sending without special parameters
                msg = await self.send_message(
                    chat_id=chat_id,
                    text=part,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview
                )
                messages.append(msg)

        return messages
