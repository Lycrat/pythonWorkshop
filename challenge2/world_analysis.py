import pymysql
import matplotlib.pyplot as plt


# Connect with the world database
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    db='world',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT Name, Population FROM country ORDER BY population DESC LIMIT 10"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()
        names = [row['Name'] for row in rows]
        population = [row['Population'] for row in rows]

        plt.xlabel("Country")
        plt.ylabel("Population")
        plt.bar(names,population)
        plt.show()


        
finally:
    conn.close()


# Bar graph of the populations in the top 10 countries
