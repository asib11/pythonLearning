import requests
from  termcolor import colored
from pyfiglet import figlet_format
url = 'https://icanhazdadjoke.com/search'
term_input = input('what type of jokes you want: ')
response = requests.get(url,headers={'accept': 'application/json'},params={'term':term_input})
data = response.json()
num = data['total_jokes']
if num  <1:
    print(f'sorry there are no jokes for {term_input}')
else:
    print(f'there is {num} jokes.here one is: ')
    print(data['results'][0]['joke'])

thank = figlet_format('ENJOY')
color = colored(thank, color= 'magenta', attrs=['bold','blink'])
print(color)