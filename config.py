# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "20435194"))
API_HASH = os.environ.get("API_HASH", "d985469a6d1413ee819126eff078448e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5851621761:AAEz-n6P1vq6I0iIwyVmP76BsdZhW2Jn8fk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1508944065")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Playlinkbot")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Filetolinkbipul:Bipul%25408170@cluster0.qsgja9t.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1508944065")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001802975070")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "playlinkofficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
