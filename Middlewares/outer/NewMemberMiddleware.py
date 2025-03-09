from typing import (
    Any, Callable, 
    Dict, Awaitable,
    Optional
)


from aiogram import BaseMiddleware, Bot
from aiogram.types import (
    Message, TelegramObject,
    ChatMemberUpdated, User
)

class WelcomeMiddleware(BaseMiddleware):
    def __init__(self):
        BaseMiddleware.__init__(self)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        
        pass