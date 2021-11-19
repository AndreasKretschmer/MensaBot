import requests
from bs4 import BeautifulSoup

def GetHttpResponse(Date):
    url = 'https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan?location=all&date=2021-11-19&criteria=&meal_type=all'
    return requests.get(url)

def FilterResponse(Date):
    menus = []
    mensaCounter = 0

    response = GetHttpResponse(Date) 
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("section", class_="meals");

    for mensa in results:
        menus = [{"Standort": mensa.find("h2").text, "Datum": Date, "Gericht": []}]

        meals = mensa.find_all("div", class_="meals__head")
        for meal in meals:
            gericht = {"Name": meal.find("h4").text ,"Zutaten": "","Preis": "2.00","Zusatzstoffe": [],"Allergene": [],"Labels": []};
            menus[mensaCounter]["Gericht"]

        mensaCounter += 1

    print(menus)