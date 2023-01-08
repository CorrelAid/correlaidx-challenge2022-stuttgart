import wikipedia
from bs4 import BeautifulSoup
import pandas as pd

#Setting the language to german
wikipedia.set_lang("de")

def get_wiki_landtag_list(name: str) -> list:
    '''
    This function returns all names from the "Abgeordnete" List in from the Landtag Wikipedia page

    Input:
        name str: The name of the wikipedia page

    Output:
        name_list list: List of all Names found on the wikipedia page
    '''
    page = wikipedia.page(title=name).html()
    #Using Beautiful Soup to parse the html into something more readable
    soup = BeautifulSoup(page, 'html.parser')
    #Select all tables and access the correct one based on the wahlperiode, which in this case contains the names
    if len(soup.find_all('table',{'class':"wikitable"})) == 4:
        table = soup.find_all('table',{'class':"wikitable"})[2]
    elif len(soup.find_all('table',{'class':"wikitable"})) == 8:
            table = soup.find_all('table',{'class':"wikitable"})[6]
    elif len(soup.find_all('table',{'class':"wikitable"})) == 2:
            table = soup.find_all('table',{'class':"wikitable"})[1]
    else:
        print(len(soup.find_all('table',{'class':"wikitable"})))
        table = ""
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    name_list = df["Name"].to_list()
    return name_list

def get_wiki_bundestag_list(name: str) -> list:
    '''
    This function returns all names from the "Abgeordnete" List in from the Bundestag Wikipedia page

    Input:
        name str: The name of the wikipedia page

    Output:
        name_list list: List of all Names found on the wikipedia page
    '''
    page = wikipedia.page(title=name).html()
    #Using Beautiful Soup to parse the html into something more readable
    soup = BeautifulSoup(page, 'html.parser')
    #Select all tables and access the correct one based on the wahlperiode one, which in this case contains the names
    if len(soup.find_all('table',{'class':"wikitable"})) == 4:
        table = soup.find_all('table',{'class':"wikitable"})[2]
    elif len(soup.find_all('table',{'class':"wikitable"})) == 6:
            table = soup.find_all('table',{'class':"wikitable"})[3]
    elif len(soup.find_all('table',{'class':"wikitable"})) == 2:
            table = soup.find_all('table',{'class':"wikitable"})[1]
    else:
        print(len(soup.find_all('table',{'class':"wikitable"})))
        table = ""
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    try:
        df = df[df["Land"] == "Baden-Württemberg"]
    except KeyError:
        df = df[df["Bundesland1"] == "Baden-Württemberg"]
    try:
        name_list = df["Name"].to_list()
    except KeyError:
        name_list = df["Mitglied des Bundestages"].to_list()
    return name_list

def get_wiki_burgermeister_list(name: str) -> list:
    '''
    This function returns all names from the "Baden-Württemberg" List in from the Bürgermeister Wikipedia page

    Input:
        name str: The name of the wikipedia page

    Output:
        name_list list: List of all Names found on the wikipedia page
    '''
    page = wikipedia.page(title=name).html()
    #Using Beautiful Soup to parse the html into something more readable
    soup = BeautifulSoup(page, 'html.parser')
    #Select all tables and access the third one, which in this case contains the names
    table = soup.find_all('table',{'class':"wikitable"})[2]
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    name_list = df["Name"].to_list()
    return name_list
