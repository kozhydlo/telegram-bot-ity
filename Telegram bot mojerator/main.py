# import config
# from aiogram import Bot, types, executor, Dispatcher

# bot = Bot(token=config.token)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def start(message: types.Message):
#     await message.answer("Привіт")

# @dp.message_handler(content_type=["new_chat_members"])
# async def new_chat(message: types.Message):
#     await message.answer("Ласка просимо до нашого чату!")
    
# @dp.message_handler(content_type=["left_chat_members"]) 
# async def left_chat(message: types.Message):
#     await message.delete()


# if __name__ == '__main__':

    # executor.start_polling(dp)
    
    
import telebot
import logging
from telebot import types

from aiogram import Bot, Dispatcher, executor, types



logging.basicConfig(level=logging.INFO)

bot = Bot(token='5767101347:AAFVNK-aFzInldt-SOQfr7ycxwSm8XfrFn8')
dp = Dispatcher(bot)

words = []
with open("mat.txt") as input:
    for word in input:
        words.append("".join(word.split()))


@dp.message_handler(content_types=["new_chat_members"]) #Зайшов
async def on_user_joined(message: types.Message):
    await message.answer("Ласка просимо до нашого чату! Що вивчаєш?")
    sti = open('/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)


@dp.message_handler(content_types=["left_chat_member"]) #Вийшов
async def on_user_exit(message: types.Message):
    await message.delete()          


@dp.message_handler(content_types=["text"])
async def filter_message(message: types.Message):
    if ".ru" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору @it_poprostomy_manager")
    elif ".org" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору @it_poprostomy_manager")   
    elif ".com" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")   
    elif ".uk" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")   
    elif ".net" in message.text:
        await message.delete()  
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")
    elif ".info" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")
    elif "https" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager") #BlackList
    elif "http" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")   
    elif "www" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")
    elif "xyz" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")           
    elif ".cite" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")   
    elif "@" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")
    elif ".to" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "Eсли Вы хотите отправлять ссылки со своей рекламой, обратитесь к администратору  @it_poprostomy_manager")                        
    elif "Гандон" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "гандон" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!") 
    elif "Їблан" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!") 
    elif "їблан" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "Далбайоб" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "далбайоб" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "Їбанько" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "їбанько" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "Йобнутий" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "йобнутий" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "Додіки" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "Додік" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "додіки" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "додік" in message.text:
        await message.delete()
        await bot.send_message(message.chat.id, "В правилах сказано що не можна матюкатися!")
    elif "слава Україні" in message.text:
        await bot.send_message(message.chat.id, "Героям слава!!!")
    elif "Слава Україні" in message.text:
        await bot.send_message(message.chat.id, "Героям слава!!!")
        
        
        
        
         
# @dp.message_handler()
# async def filer_message(message:types.Message):
#     if  message.text.lower() in words:
#         await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)