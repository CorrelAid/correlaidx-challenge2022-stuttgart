from database import Neo4jConnection
from get_wikipedia_list import get_wiki_landtag_list
import pandas as pd

conn = Neo4jConnection(uri="bolt://localhost:7687", user="test", pwd="test")

def find_officer(name: str, limit: int):
    '''
    This function returns the information of a name if one is found
    '''
    query_string = f"""
    MATCH (a:Officer)
    WHERE a.name CONTAINS "{name}"
    RETURN a
    LIMIT {limit}
    """
    result = conn.query(query_string)
    return result

def save_results(results: list):
    leaked_list = [find_officer(name,1) for name in results]
    output_record_list = [leak for leak in leaked_list if leak != []]
    output_name_list = [record[0].values()[0]["name"] for record in output_record_list]
    for name in output_name_list:
        if name not in open("output/Officers.csv"):
            with open('output/Officers.csv','a') as fd:
                fd.write("," + name)
    return output_name_list

#Bereits ausgeführt, hier weitere Listen anfügen
#save_results(get_wiki_landtag_list("Liste der Mitglieder des Landtags von Baden-Württemberg (17. Wahlperiode)"))
#read input excel file
#name_df = pd.read_excel("input/names.xlsx")
#save_results(list(name_df["Name"]))