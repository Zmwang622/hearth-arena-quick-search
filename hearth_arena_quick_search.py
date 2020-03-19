import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#Dictionary of each hero
heroes = {
1 : 'Druid',
2 : 'Hunter',
3 : 'Mage',
4 : 'Paladin',
5 : 'Priest',
6 : 'Rogue',
7 : 'Shaman',
8 : 'Warlock',
9 : 'Warrior'}

#Takes int corresponding to user's hero
#Returns text file containing hero's tierlist
def get_hero_file(hero):
    return open(heroes[hero] + '-tierlist.txt', 'r')

#Searches file for lines containing key and prints those lines
def search_cards(key, file):
    for string in file.readlines():
        if(key.lower() in string.lower()):
            print(string)

#Creates or overwrites a text file containing tierlist data (name and rank)
def build_files():
    section_count = -2
    for section in soup.findAll('section'):
        if(section_count > 0 and section_count < 10):
            filename = heroes[section_count] + '-tierlist.txt'
            hero_text = open(filename, 'w')
            card_count = 0
            for dt_tag in section.findAll('dt'):
                for dt_string in dt_tag.stripped_strings:
                    hero_text.write(dt_string + ':\t' + str(dt_tag.parent.find('dd').next_element) + '\n')
                    break
            hero_text.close()
        section_count += 1

#Welcome
begin = input("\nWelcome to the Hearth arena quick search! Press enter to begin...")

#Special welcome cases
#'build' - builds all local text files storing arena tier list data
if(begin == 'build'):
    print('\nConnecting to heartharena.com...')
    url = 'https://www.heartharena.com/tierlist'
    response = requests.get(url, 'body')
    soup = BeautifulSoup(response.text, 'html.parser')
    build_files()
    print('\nBUILD COMPLETE!')
if(begin == 'exit'):
    quit('Come again!')

#Input int corresponding to hero
#Stores corresponding hero text file in hero_file
hero = int(input('''\nEnter the number corresponding to your hero:
1. Druid
2. Hunter
3. Mage
4. Paladin
5. Priest
6. Rogue
7. Shaman
8. Warlock
9. Warrior
Enter class: '''))
print('\nYou have chosen {}.'.format(heroes[hero]))
hero_file = get_hero_file(hero)

#Loops for user inputed keyword until user presses enter
search = True
while(search):
    card = input("Enter a valid keyword or press Enter to exit: ").lower()
    if(card == ''):
        search = False
        hero_file.close()
        break
    print()
    search_cards(card, hero_file)
