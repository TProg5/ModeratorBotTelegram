from typing import Optional

from aiogram.types import ChatMember, Message
from functools import wraps


def is_admin(handler):
    @wraps(handler)
    async def wrapper(message: Message, *args, **kwargs):
        member: Optional[ChatMember] = await message.bot.get_chat_member(
            chat_id=message.chat.id, user_id=message.from_user.id
        )

        if member.status in ["creator", "administrator"]:
            return await handler(message, *args, **kwargs)
        
        await message.reply("You are not a group administrator")

    return wrapper
