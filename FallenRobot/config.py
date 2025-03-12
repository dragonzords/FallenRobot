class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 6
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

    CASH_API_KEY = "L67DVENPKLB00X8H"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://sandi:manyun13@localhost/elijang"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1002254300100  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://xyzuan1608:ieeRJVKIN65oNb3J@cluster0.fbx82.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNvcMpwQvnEyYnwBdzEpQVWm4lnH9e_mgjffQLpTjKnVJze-GqnzKQd2YB&s=10"

    SUPPORT_CHAT = "hostelfa"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7718285953:AAGDHm4s_nv66pAdzvdMwQ-Za2C_msTu5sw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6942457756  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
