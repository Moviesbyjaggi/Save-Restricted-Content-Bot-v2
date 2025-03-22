# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "14628899"))
API_HASH = getenv("API_HASH", "c5f8d5cd4fd9206add14bc12d53f9e5b")
BOT_TOKEN = getenv("BOT_TOKEN", "6991440602:AAEDiGhDwdnVc3GNMyfgzeMVAQf9Ph0Ef3Q")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6699748310").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mvstmyb658:Mz3jSZ8b7oJdl0LR@cluster0.dptxavv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002376293808")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002218325868"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
