# coding=utf-8

import requests
from bs4 import BeautifulSoup


# clanID = "2VUVQ8R9"
# site = "https://statsroyale.com/de/clan/2VUVQ8R9"
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(site,headers={'User-Agent': 'Mozilla/5.0'})
# requests.get('https://statsroyale.com/clan/LCVUYCR/refresh',headers={'User-Agent': 'Mozilla/5.0'}))

def stasi_bot():
    session = requests.Session()
    session.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/65.0.3325.162 Safari/537.36'}

    page = session.get('https://statsroyale.com/de/clan/2VUVQ8R9')
    page.raise_for_status()

    soup = BeautifulSoup(page.text, 'html.parser')

    r = session.get('https://statsroyale.com/clan/2VUVQ8R9/refresh')
    r.raise_for_status()
    refresh_state = r.json()

    if refresh_state["success"]:
        print("Refreshed!")
    else:
        print(refresh_state["message"])

    # print("Herzlich willkommen Genosse, wie kann Dir STASIROYAL dienlich sein?")
    print(soup.find('div', class_='clan__tip ui__smallText ui__greyText').text)
    # auswahl=int(input("1 - Aktualisieren 2 - Statistik anzeigen 3 - Ende:"))
    # if auswahl == 1:
    #	requests.get('https://statsroyale.com/clan/LCVUYCR/refresh',headers={'User-Agent': 'Mozilla/5.0'})
    # elif auswahl ==2:
    clan_data_list = soup.find_all('div', class_='clan__rowContainer')
    clan_final_data = []
    for clan__rowContainer in clan_data_list:

        rank = clan__rowContainer.div.text.strip()
        playerID = clan__rowContainer.a.attrs['href'].split('/')[-1]
        playerName = clan__rowContainer.a.text
        crowns = int(clan__rowContainer.find('div', 'div', class_='clan__crown').text)
        donations = int(clan__rowContainer.find('div', 'div', class_='clan__donation').text)
        noob = crowns < 20
        #rint('{:3}{:20}{:10}Spenden: {:5}CT: {:5}'.format(rank, playerName, playerID, donations, crowns, noob))
        clan_final_data.append({
            'rank': rank,
            'playerName': playerName,
            'playerID': playerID,
            'donations': donations,
            'crowns': crowns,
            'noob': noob
        })
    return clan_final_data
# else:
#	sys.exit()
# print(clan__rowContainer.div.div.text)
