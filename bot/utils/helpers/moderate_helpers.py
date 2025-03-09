import re
import logging

from datetime import datetime, timedelta
from typing import Tuple, Union, Optional

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, ChatPermissions


def parse_time_and_reason(
    text: str,
    ) -> Union[Tuple[datetime, str, str], Tuple[None, None, None]]:
    
    if not text:
        return None, None, None

    match = re.search(r"/mute\s+(\d+)([smhd])(?:\s+\[(.*?)\])?", text)

    if not match:
        return None, None, None

    duration = int(match.group(1))  # Количество времени
    unit = match.group(2)  # Тип времени (s, m, h, d)
    reason = match.group(3) if match.group(3) else "no reason provided"

    # Определяем длительность мута
    time_map = {
        "s": (timedelta(seconds=duration), "second" if duration == 1 else "seconds"),
        "m": (timedelta(minutes=duration), "minute" if duration == 1 else "minutes"),
        "h": (timedelta(hours=duration), "hour" if duration == 1 else "hours"),
        "d": (timedelta(days=duration), "day" if duration == 1 else "days"),
    }

    time_delta, readable_time = time_map.get(unit, (timedelta(), "unknown"))
    until_date = datetime.now() + time_delta  # Точное время окончания мута

    readable_time = f"{duration} {readable_time}"
    return until_date, readable_time, reason


print(parse_time_and_reason("/mute 10m"))


async def handler_to_mute(bot: Bot, message: Message) -> None:
    until_date, readable_time, reason = parse_time_and_reason(message.text)

    print(f"Debug: time - ({until_date})")

    admin_name: Optional[str] = message.from_user.username
    user_name: Optional[str] = message.reply_to_message.from_user.username

    try:
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            until_date=until_date.timestamp(),
            permissions=ChatPermissions(
                can_send_messages=False, can_send_photos=False, can_send_videos=False
            ),
        )

        await message.reply(
            f"User @{user_name} has been muted for {readable_time}\nAdmin: @{admin_name}\nReason: {reason}"
        )
        print(until_date, readable_time, reason)

    except TelegramBadRequest as error:
        await message.reply("Error mute!")
        logging.error(f"Ошибка мута пользователя: {error}")


async def handler_to_ban(bot: Bot, message: Message) -> None:

    chat_id: Optional[int] = message.chat.id
    user_id: Optional[int] = message.reply_to_message.from_user.id

    admin_name: Optional[str] = message.from_user.username
    user_name: Optional[str] = message.reply_to_message.from_user.username

    # Проверяем, есть ли причина бана
    args = message.text.split()
    reason = args[2] if len(args) > 2 else "no reason provided"

    try:
        await bot.ban_chat_member(chat_id=chat_id, user_id=user_id)

        await message.reply(
            f"User @{user_name} has been banned\n"
            f"Admin: @{admin_name}\n"
            f"Reason: {reason}"
        )

    except TelegramBadRequest as error:
        await message.reply("Error ban!")
        logging.error(f"Debug.Ban.Error_Ban: {error}")


async def handler_to_unmute(bot: Bot, message: Message) -> None:

    admin_name: Optional[str] = message.from_user.username
    user_name: Optional[str] = message.reply_to_message.from_user.username

    try:
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(
                can_send_messages=True, can_send_photos=True, can_send_videos=True
            ),
        )

        await message.reply(
            f"User @{user_name} has been unmuted\nAdmin: @{admin_name}"
        )

    except TelegramBadRequest as error:
        await message.reply("Error unmute!")
        logging.error(f"Ошибка мута пользователя: {error}")


async def handler_to_unban(bot: Bot, message: Message) -> None:

    chat_id: Optional[int] = message.chat.id
    user_id: Optional[int] = message.reply_to_message.from_user.id

    admin_name: Optional[str] = message.from_user.username
    user_name: Optional[str] = message.reply_to_message.from_user.username

    try:
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_id)

        await message.reply(
            f"User @{user_name} has been unbanned\n"
            f"Admin: @{admin_name}\n"
        )

    except TelegramBadRequest as error:
        await message.reply("Error unban!")
        logging.error(f"Debug.Ban.Error_Ban: {error}")