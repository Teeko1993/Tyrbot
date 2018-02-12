import json
import time
from core.registry import Registry

config = json.load(open("./conf/config.json", "r"))

Registry.inject_all()

while True:
    bot = Registry.get_instance("budabot")
    bot.connect("chat.d1.funcom.com", 7105)

    if not bot.login(config["username"], config["password"], config["character"]):
        bot.disconnect()
        time.sleep(5)
    else:
        bot.run()
