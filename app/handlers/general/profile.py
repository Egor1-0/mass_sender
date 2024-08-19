import time

from aiogram import F, Router
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery

from app.keyboards.profile_keyboard import main_profile_menu, delete_channel, subscription_, buy_subscription
from app.keyboards.user_keyboard import main_menu
from app.database import db

profile_router = Router()


@profile_router.message(F.text == 'Профиль⚙️')
async def profile(message: Message):
    await message.answer('Выберите пункт меню', reply_markup=main_profile_menu())
    # await message.bot.refund_star_payment(message.from_user.id,
    #                                       '')


@profile_router.message(F.text == 'Подписка')
async def subscription(message: Message):
    if db.check_user_status(message.from_user.id)[0] > int(time.time()):
        await message.answer('Подписка оформлена', reply_markup=main_menu())
    else:
        await message.answer('Подписка не оформлена', reply_markup=subscription_())


@profile_router.message(F.text == 'Назад')
async def back(message: Message):
    await message.answer('Выберите пункт меню', reply_markup=main_profile_menu())


@profile_router.message(F.text == 'Купить подписку')
async def buy(message: Message):
    prices = [LabeledPrice(label='XTR', amount=1)]
    await message.answer_invoice(
        title='Покупка подписки',
        description='Покупка подписки за 1 звезду',
        prices=prices,
        provider_token='',
        payload="buy_subscription",  
        currency="XTR",  
        reply_markup=buy_subscription(),  
    )
    # db.set_user_status(message.from_user.id, True)
    # await message.answer('Подписка куплена', reply_markup=main_menu())


@profile_router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):  
    await pre_checkout_query.answer(ok=True)


@profile_router.message(F.successful_payment)
async def succes(message: Message):
    # await message.bot.refund_star_payment(message.from_user.id,
    #                                       message.successful_payment.telegram_payment_charge_id)
    print(time.time_ns(), int(time.time()) + 2592000)
    db.set_user_status(message.from_user.id, (int(time.time()) + 2592000))
    await message.answer('Подписка куплена', reply_markup=main_menu())


@profile_router.message(F.text == 'Мои каналы')
async def profile(message: Message):
    channels = db.get_channels(message.from_user.id)
    for channel in channels:
        await message.answer(str(channel[2]), reply_markup=delete_channel(channel[0]))
    
    await message.answer('Выберите пункт меню', reply_markup=main_menu())