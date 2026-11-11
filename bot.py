import os, asyncio, logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
TOKEN=os.environ["BOT_TOKEN"]
APP_URL=os.environ["WEBAPP_URL"]
logging.basicConfig(level=logging.INFO)
bot=Bot(TOKEN); dp=Dispatcher()
def keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text="🚀 افتح الأكاديمية",web_app=WebAppInfo(url=APP_URL))],
      [InlineKeyboardButton(text="📚 الدروس",callback_data="lessons"),InlineKeyboardButton(text="🎮 الألعاب",callback_data="games")],
      [InlineKeyboardButton(text="🏆 الشهادات",callback_data="cert")]
    ])
@dp.message(CommandStart())
async def start(m:Message):
    await m.answer(f"أهلاً {m.from_user.first_name or 'يا بطل'} في 🌟 أكاديمية الطفل الذكي\nاضغط الزر لفتح الأكاديمية من داخل تيليجرام.",reply_markup=keyboard())
@dp.message(Command("help"))
async def help_cmd(m:Message):
    await m.answer("افتح الأكاديمية من الزر، ثم اختر الدروس أو الألعاب أو الاختبارات.",reply_markup=keyboard())
@dp.callback_query(F.data.in_({"lessons","games","cert"}))
async def info(c):
    msgs={"lessons":"📚 الدروس: اللغة العربية وEnglish Grammar.","games":"🎮 افتح الأكاديمية واختر الألعاب التعليمية.","cert":"🏆 إصدار الشهادة متاح من قسم الشهادات داخل الأكاديمية."}
    await c.message.answer(msgs[c.data],reply_markup=keyboard()); await c.answer()
async def main(): await dp.start_polling(bot)
if __name__=="__main__": asyncio.run(main())
