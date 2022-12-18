import wikipedia
from bs4 import BeautifulSoup
import pandas as pd

wikipedia.set_lang("de")

def get_wiki_landtag_list(name: str):
    page = wikipedia.page(title=name).html()
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table',{'class':"wikitable"})[2]
    df = pd.read_html(str(table))
    df = pd.DataFrame(df[0])
    name_list = df["Name"].to_list()
    return name_list