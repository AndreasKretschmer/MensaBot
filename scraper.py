# import the required packages
import requests
import datetime
# only import specific funtion, class etc.
from bs4 import BeautifulSoup

# variable mit der URl deklarieren
base_url = "https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan"
#url = "https://www.studentenwerk-leipzig.de/mensen-cafeterien/speiseplan?location=106&date=2021-11-19&criteria=&meal_type=all"

"""
test
"""

# define main function
def main():

    # get current date
    today = datetime.datetime.now()
    # get only the day, month and year
    date = today.strftime("%Y-%m-%d")
    
    # Mensa am park - location code 106
    location = 106

    # build the url for the desired day and location
    url = base_url + "?location=" + str(location) + "&date=" + str(date) + "&criteria=&meal_type=all"
    
    mensa_dict = {}
    
    # request the website
    res = requests.get(url)
    # check if we get the status code 200, which means "all okay, website available"
    if(res.status_code == 200):
        # get the html text 
        html = res.text
        soup = BeautifulSoup(html, features="lxml")
        # get the section meals
        meals = soup.find_all('section', attrs={"class":"meals"})
        
        for section in meals:
            # # check a variable for its type
            # print(type(section))

            # get the food category titles
            categories = section.find_all("h3", class_="title-prim")
            for cat in categories:
                print(cat.text)

            category_contents = section.find_all("div", class_="u-block")
            

            # for i in range(len(categories)):
            #     print(categories[i].text + )
    # something went wrong
    else:
        print("error, website not available, statuscode: ", res.status_code)
    
  
# Using the special variable 
# __name__ and call main function
if __name__=="__main__":
    main()