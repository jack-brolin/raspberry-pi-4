import requests
import time
import datetime

from app.db import User, MessageSenderRegisty

TEMPLATE_URL = "https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"

while True:
    for user in User.get_users():
        phone = user.phone
        api_key = user.api_key

        for registry in MessageSenderRegisty.get_registry_by_username(username=user.username):
            if datetime.datetime.now().replace(second=0, microsecond=0) == registry.time:
                url = TEMPLATE_URL.format(
                    phone=phone,
                    text=registry.text,
                    apikey=api_key
                )

                session = requests.Session()
                session.trust_env = False

                response = session.get(
                    url=url
                )
    time.sleep(3600)
