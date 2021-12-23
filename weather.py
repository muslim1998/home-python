import requests, json
base = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = 'becc12235f2d2485ef794202963dec4f'
city = input('Введите название города: ')
url = base + 'q=' + city + '&appid=' + api_key
res = requests.get(url)
if res.status_code == 200:
    data = res.json()
    print(data)
    main = data['main']
    temperature = main['temp']
    wind = data['wind']
    s = wind['speed']
    sys = data['sys']
    a = sys['country']
    main = data['main']
    v = main['feels_like']

    print(f'Temperature: {(temperature - 60 /2)/20}')
    print(f's: {s}')
    print(f'a: {a}')
    print(f'v: {v}')
else:
    print('Error')
