from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN = '<YOUR TOKEN HERE>'

aapl = Stock('FB', token=TOKEN)
data = aapl.get_quote()
# pp.pprint(data)
print(data['companyName'], data['latestPrice'])