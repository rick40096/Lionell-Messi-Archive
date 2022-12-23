# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Messi/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 16328949  # integer value, dont use ""
    API_HASH = "edd45c4aeb051d0e3a3e925f1fc9a287"
    TOKEN = "5828305192:AAFXirVUWzxUhKLJJoEptNcYfr8WB6e-0ec"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2005266280  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Archx_exe_Gods"
    SUPPORT_CHAT = "messi_probot_support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001195907541
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001195907541
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://nlxlkpuc:qnx84ZMh6Jwfytojhp1PSRtCzz20htjI@otto.db.elephantsql.com/nlxlkpuc"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    MONGO_DB_URI = "mongodb+srv://Rick:Rick@cluster0.mq48ssf.mongodb.net/?retryWrites=true&w=majority"
    MONGO_PORT = int("27017")
    MONGO_DB = "Messi"
    URL = None
    STRING_SESSION = "1BVtsOG4Bu3VoydJbMMCM3W8G0LT_dip2boNKQYPvqmfgdk2JIRyCjwIXU4jxIQzu6OfMjBbxmtV3N4jo57GFwf_dFXk-ANmYdI0I111JwzNEWMvsIKu8qMt4EluZYd6HfbbjZy19IV-qdQFiJs5AwX31LYlS6vQNnjjivfKys9IogDxtaAyQ4FUXoCe8RNbkc4d2ISMKHjsmFmNltMUp-BIj-yEnvlhjCtDAN6rQ0E2E8GBiyIiClilmp_1c_jU7EXzWHy5AlayBlIv-ILi26fumwCKJrv3mMUvA-ajkqPyT8GqEeD6wj1InqdRrm_yaRXd3I5-ycppZ3IA8Fdup9PUHqCg0Awk="
    ARQ_API_URL = "http://arq.hamker.dev"
    ARQ_API_KEY = "TMDHQO-RKVYDN-HXUAOR-MZAYVA-ARQ"
    SPAMWATCH_API = "pQ9y9GTPTlkMrZtBuTcyMU7xyxSSmUu_pEbkosNd_LLAbhNoxvtPVc1FUFfFiRVU"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ALLOW_CHATS = True
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
