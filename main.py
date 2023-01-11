import psycopg2
import json

# Connect to the database
conn = psycopg2.connect(
    host="database-1.cip6dyjtjole.us-east-1.rds.amazonaws.com",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="7zDXiDUkYct8nZV"
)

# Create a cursor object
cur = conn.cursor()

# Execute a SELECT statement
cur.execute("SELECT * FROM fmembers")

# Fetch all rows
rows = cur.fetchall()

# Create an object for each row of data
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
        data["results"] = json.loads(results)
    else:
        data["results"] = {}
    if keywords is not None:
        data["keywords"] = json.loads(keywords)
    else:
        data["keywords"] = {}
    objects.append(data)

# Print the objects
print(objects)

# Close the cursor and connection
cur.close()
conn.close()
