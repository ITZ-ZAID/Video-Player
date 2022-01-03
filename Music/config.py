##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'Session')
BOT_TOKEN = getenv('BOT_TOKEN', '')
API_ID = int(getenv('API_ID', '6435225'))
API_HASH = getenv('API_HASH','')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1669178360').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-100'))
ASS_ID = int(getenv("ASS_ID", '2038306661'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1669178360').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GodfatherSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "The_Godfather_Network")
GROUP = getenv("GROUP", "GodfatherSupport")
CHANNEL = getenv("CHANNEL", "The_Godfather_Network")
