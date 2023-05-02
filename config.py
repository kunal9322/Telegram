import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "29785000")
    API_HASH = getenv("API_HASH", "2d77466ebb7b64c5ebe05d71306a5546")
    TOKEN = getenv("TOKEN", "6060441968:AAHUHSjx-Uam3M_rY2YuF3C7Pq4R-SNi8i4")
    OWNER_ID = getenv("OWNER_ID","5885920877")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOLwBuzjDbfUHWsRZiwufj6zTtV0wWV85gGTNPTo3du_kyr8uNcR93HrWnBPk--xAuVcM9moy9I2B8DCrA_PvO2x5YhpXoiVacDX3IcUIXz8dPlkv88z13ILrRR7Zhondifvg-qcBPVywSRbM2oAf_3PrguDjU1u1IoMtWeKa0_iahysyrHhm4lND9PjtexbLrwaqK_4L9Oy3Hma7CUzR_X9_oaNCHPn79UVVTjoITHM7JnYQDzmabosOh4K4I7u6VLhDyXD82PGJVy9DnTTPLfUmYUrCHL7cjVQMB34CIVaQ9gL2VXsGTnBkO54-dDhdAw0q1avFYPM4DWyHp1NeFNOC1lA=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "MH17_KUNAL")
    DB_URI = getenv("DATABASE_URL", "postgres://pktttuoh:1LPQQKhy2mpOES27_qF-zAvbUTnEhkAT@balarama.db.elephantsql.com/pktttuoh")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001935950378")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001935950378")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "5885920877")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
