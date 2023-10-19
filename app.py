import asyncio

from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings

from echobot import EchoBot
from middleware import Middleware1

app = Flask(__name__)
loop = asyncio.get_event_loop()

bot_settings = BotFrameworkAdapterSettings("","")
bot_adapter = BotFrameworkAdapter(bot_settings)
bot_adapter.use(Middleware1())

echobot = EchoBot()

@app.route('/api/messages', methods=['POST'])
def api_messages():
  if "application/json" in request.headers["Content-Type"]:
    json_message = request.json
  else:
    return Response(status=415)

  activity = Activity().deserialize(json_message)

  async def on_turn(turn_context):
    await echobot.on_turn(turn_context)

  task = loop.create_task(bot_adapter.process_activity(activity, "", on_turn))
  loop.run_until_complete(task)

  return Response(status=200)

if __name__ == '__main__':
  app.run('localhost', 3978)