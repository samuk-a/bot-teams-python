from typing import List
from botbuilder.core import TurnContext, ActivityHandler
from botbuilder.schema import ChannelAccount


class EchoBot(ActivityHandler):
  async def on_message_activity(self, turn_context: TurnContext):
    return await turn_context.send_activity(turn_context.activity.text)
  
  async def on_members_added_activity(self, members_added: List[ChannelAccount], turn_context: TurnContext):
    await turn_context.send_activity("Seja bem vindo ao EchoBot!")
    await turn_context.send_activity("Irei repetir tudo que você me enviar!")