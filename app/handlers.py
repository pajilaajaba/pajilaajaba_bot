from mailbox import Message

from aiogram import  types, filters, F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboard as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(filters.CommandStart())
async def cmd_start(message:types.Message):
    await message.answer("дарова чувачок)", reply_markup=kb.main)
    await message.reply("как дила")



@router.message(filters.Command('help'))
async def cmd_help(message:types.Message):
    await message.answer("помощь нужна")


@router.message(F.text == 'мем 2017 года')
async def cmd_2017mem(message:types.Message):
    await message.answer("Выберете мемасик", reply_markup=kb.mem_2017)


@router.callback_query(F.data == 'Diana_sh')
async def diana_sh(callback:types.CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Мемчик Дианы Шуригиной')


@router.message(filters.Command('register'))
async def register(message: types.Message, state:FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите имя')


@router.message(Register.name)
async def register_name(message: types.Message, state:FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')


@router.message(Register.age)
async def register_age(message: types.Message, state:FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Register.number)
    await message.answer('Введите ваш номер', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: types.Message, state:FSMContext):
    await state.update_data(number = message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Вы{data["name"]}\nвам стоко лет{data["age"]}\nвы юзаете такой то номерок{data["number"]}")
    await state.clear()