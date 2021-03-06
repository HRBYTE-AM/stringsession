import Config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="StringSessionBot"),
)


if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("عـذرا هنـالك خـطأ في الايب ايدي او الايبي هاش")
    except AccessTokenInvalid:
        raise Exception("عـذرا توكـن البـوت غيـر صالـح")
    uname = app.get_me().username
    print(f"@{uname} اشتغل بنجاح  ✓!")
    idle()
    app.stop()
    print("تم ايقاف البوت  ×")
