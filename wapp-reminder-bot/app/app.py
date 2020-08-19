import requests
import time
import datetime
import logging

from db import User, Message, MessageSenderRegistry

TEMPLATE_URL = "https://api.callmebot.com/whatsapp.php?phone={phone}&text={text}&apikey={apikey}"

while True:
    for user in User.get_users():
        phone = user.phone
        api_key = user.api_key

        for registry in MessageSenderRegistry.get_registry_by_username(username=user.username):
            if not registry.MessageSenderRegistry.is_sent:
                if datetime.datetime.now() > registry.MessageSenderRegistry.sending_time:
                    url = TEMPLATE_URL.format(
                        phone=phone,
                        text=registry.Message.text,
                        apikey=api_key
                    )

                    session = requests.Session()
                    session.trust_env = False

                    response = session.get(url=url)

                    logging.warning(url)
                    logging.warning(str(response.status_code))
                    logging.warning(str(response.content))
    time.sleep(60)
