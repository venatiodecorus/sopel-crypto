import sopel.module
from requests import get
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

api = 'https://api.coingecko.com/api/v3/'

@sopel.module.commands('crypto')
@sopel.module.example('.crypto bitcoin')
def crypto(bot, trigger):
    # res = get(api + 'simple/price?ids=' + trigger.group(2) + '&vs_currencies=usd').json()
    res = cg.get_price(ids= trigger.group(2), vs_currencies='usd')
    output = str(res[trigger.group(2)]['usd'])
    bot.say(output)