#x = (lambda x,y: x+y)(2,3)
#print(x)

# add = lambda x,y: x+y
# print(type(add))
# print(add)

# x = add(2,3)
# print(x)


data = [
  {
    "id": "binancecoin",
    "symbol": "bnb",
    "name": "Binance Coin",
    "image": "https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png?1547034615",
    "current_price": 212.03,
    "market_cap": 33015186690,
    "total_volume": 2490184836,
    "high_24h": 230.59,
    "low_24h": 210.87,
  },
  {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin",
    "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
    "current_price": 47553,
    "market_cap": 901453728232,
    "total_volume": 47427138554,
    "high_24h": 51131,
    "low_24h": 48056,
  },
  {
    "id": "cardano",
    "symbol": "ada",
    "name": "Cardano",
    "image": "https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860",
    "current_price": 0.84514,
    "market_cap": 27210647217,
    "total_volume": 3204270671,
    "high_24h": 0.919055,
    "low_24h": 0.843236,
  },
  {
    "id": "ethereum",
    "symbol": "eth",
    "name": "Ethereum",
    "image": "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880",
    "current_price": 1479.97,
    "market_cap": 172447578072,
    "total_volume": 24709055087,
    "high_24h": 1597.13,
    "low_24h": 1493,
  },
  {
    "id": "litecoin",
    "symbol": "ltc",
    "name": "Litecoin",
    "image": "https://assets.coingecko.com/coins/images/2/large/litecoin.png?1547033580",
    "current_price": 171.49,
    "market_cap": 11561005268,
    "total_volume": 4950077782,
    "high_24h": 187.34,
    "low_24h": 172.45,
  },
  {
    "id": "polkadot",
    "symbol": "dot",
    "name": "Polkadot",
    "image": "https://assets.coingecko.com/coins/images/12171/large/aJGBjJFU_400x400.jpg?1597804776",
    "current_price": 29.28,
    "market_cap": 28856989783,
    "total_volume": 1266769267,
    "high_24h": 32.2,
    "low_24h": 29.54,
  },
  {
    "id": "ripple",
    "symbol": "xrp",
    "name": "XRP",
    "image": "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1605778731",
    "current_price": 0.360658,
    "market_cap": 16580549437,
    "total_volume": 2357746464,
    "high_24h": 0.381072,
    "low_24h": 0.358941,
  },
  {
    "id": "tether",
    "symbol": "usdt",
    "name": "Tether",
    "image": "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1598003707",
    "current_price": 0.83869,
    "market_cap": 32307660438,
    "total_volume": 82854947322,
    "high_24h": 0.843104,
    "low_24h": 0.832594,
  },
  {
    "id": "uniswap",
    "symbol": "uni",
    "name": "Uniswap",
    "image": "https://assets.coingecko.com/coins/images/12504/large/uniswap-uni.png?1600306604",
    "current_price": 24.94,
    "market_cap": 13099199643,
    "total_volume": 939432128,
    "high_24h": 27.92,
    "low_24h": 24.78,
  }
]

def sort_funkcija(x):
    print(f"{x['id']} \t {x['market_cap']}")
    return x["market_cap"]

#y = sorted(data, key=sort_funkcija)
y = sorted(data, key=lambda x: x["market_cap"])

print("SORTING DONE")
print(y)