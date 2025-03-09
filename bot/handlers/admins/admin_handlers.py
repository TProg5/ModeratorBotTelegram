import logging

from typing import Optional
from aiogram import Bot, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from filters.admin_filters import is_admin

from utils.helpers.moderate_helpers import (
    handler_to_ban, handler_to_mute, 
    handler_to_unban, handler_to_unmute
)

admin_command = Router()


@admin_command.message(Command("mute"))
@is_admin
async def mute_users(message: Message, command: CommandObject) -> None:
    bot: Optional[Bot] = message.bot

    if not message.reply_to_message:
        await message.reply("reply to message users")
        return

    await handler_to_mute(bot, message)


@admin_command.message(Command("ban"))
@is_admin
async def ban_users(message: Message, command: CommandObject) -> None:
    bot: Optional[Bot] = message.bot

    if not message.reply_to_message:
        await message.reply("reply to message users")
        return

    await handler_to_ban(bot, message)


@admin_command.message(Command("unmute"))
@is_admin
async def unmute_user(message: Message, command: CommandObject) -> None:
    bot: Optional[Bot] = message.bot

    if not message.reply_to_message:
        await message.reply("reply to message users")
        return

    await handler_to_unmute(bot, message)


@admin_command.message(Command("unban"))
@is_admin
async def unmute_user(message: Message, command: CommandObject) -> None:
    bot: Optional[Bot] = message.bot

    if not message.reply_to_message:
        await message.reply("reply to message users")
        return

    await handler_to_unban(bot, message)