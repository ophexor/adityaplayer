import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", "2032501254"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Sanki_Owner")
BOT_USERNAME = getenv("BOT_USERNAME", "EsportRobot")
BOT_TOKEN = getenv("BOT_TOKEN", "1917637742:AAGQgry6cz73uyKgqBmH0ihidxWj2d11Lk8")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1728b3a43616d35affa68.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
STRING_SESSION = getenv("SESSION_NAME", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2032501254 1812140191 1964732367").split()))
