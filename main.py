import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
SESSION =  "BAAS_fEAKgvQcbVoPQ2R-4_AQ84X6_FsxeM-9VyHfKM50Rau_w0c76_N0mh4zuPsgH8iNn89T_kvxOvGi7JOppA-RPiT6keYKuSmKfGORNPEVezL4m3iOkDUqh65BfLVP32sxVbHLPB4VC2b5jQy2Pmfvy3v4bmeEPVRBWnkHT_Jm2w8U7HUw-BZYZ62o7YWve02pd3iCC1YXO5CODrHD9eAcQndyENFJLcXm8zKRpUokjAHs2a87T0zNiFspH1xcA6XUItl7X7vQLgkxUjkM_7_-oYGyF-OZo309f0EtpJe4iVoh0grbsxz7xsbMFv9PPgKxJKZi7BajM83MJAYBge6wOhw5AAAAAGmLCu2AQ"
StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=SESSION,
#    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="Asuraa"),
)


if __name__ == "__main__":
    print("Your bot is starting..")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} Successfully started !")
    idle()
    app.stop()
    print("BOT STOPPED")
