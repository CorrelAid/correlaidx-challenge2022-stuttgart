from database import Neo4jConnection

conn = Neo4jConnection(uri="bolt://localhost:7687", user="test", pwd="test")

def find_officer(name: str, limit: int):
    '''
    This function returns the information of a name if one is found.
    '''
    query_string = f"""
    MATCH (a:Officer)
    WHERE a.name CONTAINS "{name}"
    RETURN a
    LIMIT {limit}
    """
    result = conn.query(query_string)
    return result

print(find_officer("Michael Sauer",1))
