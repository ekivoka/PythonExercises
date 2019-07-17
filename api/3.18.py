import requests


numbers = []

with open("dataset_24476_3.txt", "r") as f:
    for n in f:
        numbers.append(int(n.strip()))
        
print(numbers)

params = {
    'default':'boring'
}
url = "http://numbersapi.com/"

for numb in numbers:
    api_url = url+str(numb)+'/math/'
    res = requests.get(api_url,params = params)
    if res.text == 'boring':
        print('Boring')
    else:
        print('Interesting')
