from typing import Callable, Awaitable

from botbuilder.core import Middleware, TurnContext
from botbuilder.schema import ActivityTypes


class Middleware1(Middleware):
  async def on_turn(self, turn_context: TurnContext, next: Callable[[TurnContext], Awaitable]):
    if turn_context.activity.type == ActivityTypes.message:
      await turn_context.send_activity("Irei executar a próxima função")
      await next()
      await turn_context.send_activity("Executei a função, você gostou?")
    else:
      await next()