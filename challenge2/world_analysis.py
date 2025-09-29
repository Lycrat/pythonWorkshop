import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    db='world',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = "SELECT * FROM country LIMIT 10"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        for row in rows:
            print(row)
finally:
    conn.close()