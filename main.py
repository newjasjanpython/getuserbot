import aiogram as aio
import aiogram.types as typ
import aiogram.filters.command as cmd
import pyrogram as clt
import asyncio as asn
import logging
import auth

logging.basicConfig(level=logging.DEBUG)


bot = aio.Bot("7480340893:AAH4H1hcZbmB7iJyf5Y0yDOywcF2Sa4-AGI")
dp = aio.Dispatcher()

client = clt.Client(
    "myclient",
    api_id=auth.API_ID,
    api_hash=auth.API_HASH,
    phone_number=auth.PHONE
)


@dp.message(cmd.CommandStart())
async def start_handler(msg: typ.Message):
    await msg.answer("HEHEHE!")


@dp.message(aio.F.text.startswith("@"))
async def get_userinfo(msg: typ.Message):
    username = msg.text.split('@')[-1].strip()

    try:
        user = await client.get_users(username)
        
        text = (
            f"👤 **User Info**:\n"
            f"ID: `{user.id}`\n"
            f"First Name: `{user.first_name}`\n"
            f"Last Name: `{user.last_name}`\n"
            f"Username: `@{user.username}`\n"
            f"Is Bot: `{user.is_bot}`"
        )
        await msg.answer(text, parse_mode='Markdown')
    except Exception as e:
        await msg.answer(f"Error fetching user: {e}")


async def main():
    await client.start()
    await dp.start_polling(bot)
    await client.stop()


if __name__ == '__main__':
    asn.run(main())
