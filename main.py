import psycopg2
import json
import spacy

# Connect to the database
nlp = spacy.load("en_core_web_sm")
conn = psycopg2.connect(
    host="database-1.cip6dyjtjole.us-east-1.rds.amazonaws.com",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="7zDXiDUkYct8nZV"
)
class Member:
    def __init__(self, id, firstname, lastname, fullname, constituency, results, keywords):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = fullname
        self.constituency = constituency
        self.results = results
        self.keywords = keywords
    def printResults(self):
        print(self.results)
# Create a cursor object
cur = conn.cursor()

# Execute a SELECT statement
cur.execute("SELECT id, firstname, lastname, fullname, constituency, results, keywords FROM fmembers")

# Fetch all rows
rows = cur.fetchall()

# Convert rows to a list of Member objects
members = []
for row in rows:
    if row[5] is not None:
        member = Member(*row)
        members.append(member)
    else:
        pass
    


cur.close()
conn.close()
"""
objects = []
for row in rows:
    id, firstname, lastname, fullname, constituency, results, keywords = row
    data = {
        "id": id,
        "firstname": firstname,
        "lastname": lastname,
        "fullname": fullname,
        "constituency": constituency
    }
    if results is not None:
        try:
            data["results"] = json.loads(results)
            print(data["results"])
        except json.decoder.JSONDecodeError:
            data["results"] = {}
    else:
        data["results"] = {}
    if keywords is not None:
        try:
            data["keywords"] = json.loads(keywords)
        except json.decoder.JSONDecodeError:
            data["keywords"] = []
    else:
        data["keywords"] = []
    objects.append(data)
    if data["results"] is not None:
        for result in data["results"]:
            doc = nlp(result["headline"])
            nouns = [token.text for token in doc if token.pos_ == "NOUN"]
            adjectives = [token.text for token in doc if token.pos_ == "ADJ"]
            verbs = [token.text for token in doc if token.pos_ == "VERB"]
            data["keywords"].extend(nouns[:3])
            data["keywords"].extend(adjectives[:3])
            data["keywords"].extend(verbs[:3])
            cur.execute(f"UPDATE fmembers SET keywords = '{json.dumps(data['keywords'])}' WHERE id = {id}")
            conn.commit()
    print(results)
    """
# Close the cursor and connection

