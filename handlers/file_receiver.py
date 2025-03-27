from asyncio import sleep
from pyrogram.filters import create, chat
from pyrogram.handlers import MessageHandler

from common import batch_files, is_batch
from configs import Config

async def temp(_, __):
    pass

async def receive_files(client, message):
    is_batch = True
    msg_id = message.id
    batch_files[msg_id] = []
    async def event_filter(_, __, message):
        if message and message.text:
            if message.text.startswith('/cancel'):
                is_batch = False
                del batch_files[msg_id]
            elif message.text.startswith('/done'):
                is_batch = False
        batch_files[msg_id].append(message)
    handler = client.add_handler(MessageHandler(temp, filters=create(event_filter) & chat(Config.BOT_OWNER), group=-1))
    while is_batch[user_id]:
        await sleep(0.5)
    client.remove_handler(*handler)
    try:
        return batch_files[msg_id]
    except:
        return []