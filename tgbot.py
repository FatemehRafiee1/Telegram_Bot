import logging
import requests
from aiogram import Bot, Dispatcher, types

import asyncio
import logging
import sys
import random

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold, hitalic

from shared.gpt import make_request
from mongoengine import connect

from shared.utils import *
from shared.coinex import coin_symbols
from shared.mongo_models import User, Message, ChatSession, Question


connect("my_database", host="localhost", port=27017)

bot = None
guid = None
wating = False
typing_coin = False
choosing_coin = False
choosing_topic = False

history = []

dp = Dispatcher()

def inline_key_builder(keyword_responses, x, y):
    builder=InlineKeyboardBuilder()
    if isinstance(keyword_responses, dict):
        for k in keyword_responses.keys():
            builder.add(InlineKeyboardButton(text = k[1:], callback_data=k))
    else:
        for k in keyword_responses:
            builder.add(InlineKeyboardButton(text = k[1:], callback_data=k))
    builder.adjust(x, y)
    builder = builder.as_markup()
    return builder

builder = inline_key_builder(keyword_responses=menu_responses, x=2, y=2)
    

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    global guid
    guid = message.from_user.id
    user_exists = User.objects(uid=guid).first()

    if user_exists:
        await message.answer(f"Welcome back {hbold(message.from_user.first_name)}!", reply_markup=builder)
    else:
        user_data = {
            "uid": message.from_user.id,
            "name": message.from_user.full_name
        }
        User.objects.create(**user_data)
        await message.answer(f"Welcome, {hbold(message.from_user.full_name)} ☘️", reply_markup=builder)


@dp.message(Command('menu'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"What do you want {hbold(message.from_user.first_name)}?", reply_markup=builder)


@dp.message()
async def command_handler(message: Message) -> None:
    global wating, guid, typing_coin, choosing_coin

    if wating:
        if message.text.lower() == 'stop' or message.text.lower() == 'cancel':
            wating = False
            await message.answer('Talk to you later. Take care.')

        else:
            current_user = User.objects(uid=message.from_user.id).first()
            chat_session = ChatSession.objects(user_instance=current_user).first()
            if chat_session is None:
                # If no chat session exists, create a new one
                chat_session = ChatSession(user_instance=current_user, messages=[])

            new_message = Message(role="user", content=message.text)
            chat_session.messages.append(new_message)
            chat_session.save()

            # ------------------------------------------------
            chat_session = ChatSession.objects(user_instance=current_user).first()
            if chat_session:
                chat_history = [
                    {"role": message.role, "content": message.content}
                    for message in chat_session.messages
                ]
            # ------------------------------------------------

            result = make_request(config, chat_history)
            gpt_response = result['choices'][0]['message']['content']

            new_response = Message(role="assistant", content=gpt_response)
            chat_session.messages.append(new_response)
            chat_session.save()

            await message.answer(gpt_response)
    
    elif typing_coin:
        try:
            now, hc, dc, wc = get_change(config, message.text)
            await message.answer(
                f"🔹 {hbold((message.text).upper())}: {now[-1]['close']} \n\n 📌Changes in: \n\n"
                f"{get_color(hc)} Last hour  =>  {hc} % \n\n"
                f"{get_color(dc)} Last day  =>  {dc} % \n\n"
                f"{get_color(wc)} Last week  =>  {wc} %"
            )

        except TypeError:
            await message.answer("Didn't find such symbol.")

        typing_coin = False
        choosing_coin = False
        
    else:
        await message.answer("Sorry, wrong command.\nTo access possible options, type /menu.")
    

@dp.callback_query()
async def callback_handler(callback_query: types.CallbackQuery):
    global wating, choosing_coin, typing_coin, choosing_topic

    if choosing_coin: 
        keyword = callback_query.data
        text_response = coin_symbols.get(keyword)
        
        if keyword == '/other':
            typing_coin = True
            await callback_query.message.answer('Waiting for you to type.\nIt should be in the right format. (e.g: BTCUSDT)')
        else:
            now, hc, dc, wc = get_change(config, text_response)
            await callback_query.message.answer(
                f"🔹 {hbold(keyword[1:])}: {now[-1]['close']} $\n\n 📌Changes in: \n\n"
                f"{get_color(hc)} Last hour  =>  {hc} % \n\n"
                f"{get_color(dc)} Last day  =>  {dc} % \n\n"
                f"{get_color(wc)} Last week  =>  {wc} %"
            )
        choosing_coin = False
 
    elif choosing_topic:
        keyword = callback_query.data
        question_object = Question.objects(topic=keyword[1:])
        selected_question = random.choice(question_object)
        await callback_query.message.answer(selected_question.question)
        choosing_topic = False

    else:
        keyword = callback_query.data

        if keyword == '/gpt':
            wating = True
            await callback_query.message.answer(f"I'm all ears... \n(Type {(hitalic('cancel'))} or {hitalic('stop')} anytime you wanted to interrupt.)")

        elif keyword == '/ielts':
            wating = False
            choosing_topic = True
            ielts_builder = inline_key_builder(keyword_responses=conversation_topics, x=3, y=3)
            await callback_query.message.answer('Choose a topic.', reply_markup=ielts_builder)
    
        elif keyword == '/joke':
            wating = False
            response = requests.get("https://official-joke-api.appspot.com/jokes/random")
            data = response.json()
            await callback_query.message.answer(data['setup'])
            await callback_query.message.answer(data['punchline'])
            
        elif keyword == '/crypto':
            wating = False
            choosing_coin = True
            crypto_builder = inline_key_builder(keyword_responses=coin_symbols, x=3, y=4)
            await callback_query.message.answer('Pick a coin.', reply_markup=crypto_builder)

        else:
            await callback_query.message.answer("You should select an item from the menu first.\nTo access possible options, type /menu.")


async def main() -> None:
    global bot
    telegram_bot_token = config["telegram_bot_token"]
    bot = Bot(token=telegram_bot_token, default=DefaultBotProperties(parse_mode="HTML"))
    
    await dp.start_polling(bot)

if __name__ == "__main__":       
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
