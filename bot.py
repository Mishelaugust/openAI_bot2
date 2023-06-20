import logging, re
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from config import tg_token, api_token
import requests
import openai

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=tg_token)
storage = MemoryStorage()
# Диспетчер
dp = Dispatcher(bot,storage=storage)

#openai.api_key = api_token

# Хэндлер на команду /start
@dp.message_handler(commands =("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.first_name}! Please, input your response and get a picture!")

# @dp.message_handler()
# async def main(message: types.Message):
#     headers = {
#         'Authorization': f'Bearer {api_token}',
#         'Content-Type': 'application/json'
#     }

#     response = requests.post(url, json={'prompt':message.text}, headers=headers)

#     if response.status_code == 200:
#         result = response.json()
#         await message.reply(result)
#     else:
#         await message.reply(f'Error:{response.text}')

@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
    # response = openai.Image.create(
    #     prompt=message.text,
    #     n=1,
    #     size="1024x1024")


    
    # if response and response.choices:
    #     reply = response['data'][0]['url']
    #     await message.reply(reply)
    # else:
    #     await message.reply('ой...')
    
    url1 = 'https://image.pollinations.ai/prompt/[%s]' % message.text.replace(' ','+')  
    
    response = requests.get(url1)

    if response.status_code == 200:
        with open('image.jpg', 'wb') as ph_file:
            ph_file.write(response.content)
            print("Картинка успешно сохранена.")
            photo = open('image.jpg', 'rb')
        await bot.send_photo(message.chat.id, photo)
    else:
        await message.reply(f'Error:{response.text}')

    




if __name__ == "__main__":
    executor.start_polling(dp)