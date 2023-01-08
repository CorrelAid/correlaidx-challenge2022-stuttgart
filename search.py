from database import Neo4jConnection
from get_wikipedia_list import get_wiki_landtag_list, get_wiki_bundestag_list, get_wiki_burgermeister_list
import pandas as pd

conn = Neo4jConnection(uri="bolt://localhost:7687", user="test", pwd="test")

def find_officer(name: str, limit: int) -> list:
    '''
    This function returns the information of a name if one is found

    Input:
        name str: Name of the Officer to be searched
        limit int: Amount of results wanted

    Output:
        result list: The resulting neo4j record as a list
    '''
    query_string = f"""
    MATCH (a:Officer)
    WHERE a.name CONTAINS "{name}"
    RETURN a
    LIMIT {limit}
    """
    result = conn.query(query_string)
    return result

def save_results(results: list) -> list:
    '''
    This function searches the record for the name of the officer and saves it into a file

    Input:
        results list: List of the results found in the Database

    Output:
        output_name_list list: List of all Officer names found in the database
    '''
    leaked_list = [find_officer(name,1) for name in results]
    #Remove all empty lists
    output_record_list = [leak for leak in leaked_list if leak != []]
    #Only use the names found
    output_name_list = [record[0].values()[0]["name"] for record in output_record_list]
    officers = pd.read_csv("output/Officers.csv")
    officer_list = list(officers["Officers"])
    for name in output_name_list:
        #Check if Officer name was found before
        if not name in officer_list:
            officer_list.append(name)
    officers = pd.DataFrame(officer_list,columns=["Officers"])
    officers.to_csv("output/Officers.csv",index=False)
    return output_name_list

#Bereits ausgeführt, hier weitere Listen anfügen
#Landtagsmitglieder
#save_results(get_wiki_landtag_list("Liste der Mitglieder des Landtags von Baden-Württemberg (17. Wahlperiode)"))
#save_results(get_wiki_landtag_list("Liste der Mitglieder des Landtags von Baden-Württemberg (16. Wahlperiode)"))
#save_results(get_wiki_landtag_list("Liste der Mitglieder des Landtags von Baden-Württemberg (15. Wahlperiode)"))
#Bundestagsmitglieder
#save_results(get_wiki_bundestag_list("Liste der Mitglieder des Deutschen Bundestages (20. Wahlperiode)"))
#save_results(get_wiki_bundestag_list("Liste der Mitglieder des Deutschen Bundestages (19. Wahlperiode)"))
#save_results(get_wiki_bundestag_list("Liste der Mitglieder des Deutschen Bundestages (18. Wahlperiode)"))
#Bürgermeister
#save_results(get_wiki_burgermeister_list("Liste der deutschen Oberbürgermeister"))
#read input excel file
#name_df = pd.read_excel("input/names.xlsx")
#save_results(list(name_df["Name"]))