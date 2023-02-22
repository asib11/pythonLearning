import requests
from bs4 import BeautifulSoup
from random import choice

all_data = []
root_url = "http://quotes.toscrape.com"
nxt_url = "/page/1/"
while nxt_url:
    response = requests.get(f"{root_url}{nxt_url}")
    #print(f"now access {root_url}{nxt_url}....")
    soup = BeautifulSoup(response.text, "html.parser")
    quote = soup.find_all(class_="quote")

    for details in quote:
        all_data.append(
            {
                "text": details.find(class_="text").get_text(),
                "name": details.find(class_="author").get_text(),
                "url": details.find("a")["href"]
            }
        )

    nxt_btn = soup.find(class_="next")
    nxt_url = nxt_btn.find("a")["href"] if nxt_btn else None
#print(all_data)

def play_game():

    pick_quote = choice(all_data)
    print(f'here quote is : {pick_quote["text"]}')
    print(pick_quote['name'])
    user_input = ''
    reminder = 4
    while user_input.lower() != pick_quote['name'].lower() and reminder > 0:
        user_input = input(f'who tell it? your have {reminder} chance: ')
        reminder -= 1
        if user_input.lower() == pick_quote['name'].lower():
            print('congratulations!!!')
            
        if reminder == 3:
            response2 = requests.get(f'{root_url}{pick_quote["url"]}')
            soup = BeautifulSoup(response2.text, 'html.parser')
            birth_date = soup.find(class_ ="author-born-date").get_text()
            birth_location = soup.find(class_ ="author-born-location").get_text()
            print(f'hint: birth date: {birth_date}')
        elif reminder == 2:
            print(f'hint: birth location: {birth_location}')
        elif reminder == 1:
            first_last = pick_quote['name'].split(' ')
            print(f'hint: first name 1st letter "{first_last[0][0]}" and lsat name 1st letter "{first_last[1][0]}"')
        else:
            print(f'sorry, you loose.the answer is: {pick_quote["name"]}')

    play = ''
    while play.lower() not in ('y','n'):
        play = input('do you want to play again? (y/n): ')
        if play.lower() in 'y':
            return play_game()
        elif play.lower() in 'n':
            print('Vlo theko, Sukhe theko')
play_game()