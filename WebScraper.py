import requests
from bs4 import BeautifulSoup

def GetHttpResponse():
    url = 'https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan?location=all&date=2021-11-19&criteria=&meal_type=all'
    return requests.get(url)

def FilterResponse():
    menu = {}
    response = GetHttpResponse() 
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("section", class_="meals");

    for mensa in results:
        mensaText = mensa.find("h2").text
        menu[mensaText] = []
        meals = mensa.find_all("div", class_="meals__head")
        for meal in meals:
            menu[mensaText] += [meal.find("h4").text, meal.find("p", class_="meals__price")]

    print(menu)