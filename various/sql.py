# import of the driver, different dipending on the dbms
import psycopg2
import pandas as pd
from matplotlib import pyplot as plt

# opening the connection
conn = psycopg2.connect(user="read-only",
                        password="read-only",
                        host="35.184.200.74",
                        port="5432",
                        database="states")

# getting a cursor to make query
cursor = conn.cursor()

# making a query
cursor.execute('''
                SELECT * 
                FROM   countries
                ''')
print(cursor.fetchone())

cursor.execute('''
                SELECT indicator_code, indicator_value 
                FROM  records
                limit 100
                ''')

for row in cursor.fetchall():
    print(f"{row[0]}:{row[1]}")

# using pandas directly
df = pd.read_sql_query('''
                        SELECT c.short_name as country, i.indicator_code as indicator, indicator_value as average
                        FROM records
                                 JOIN countries c on c.country_code = records.country_code
                                 JOIN indicators i on i.indicator_code = records.indicator_code
                        where year > 1990
                           and (c.country_code = 'ITA' or c.country_code = 'USA')
                        LIMIT 1000;
                ''', conn)
print(df.head())

s = '''pippo    
        pippo
        '''

df = pd.read_sql_query('''
                SELECT records.indicator_code,count(*) as c
                from records
                WHERE country_code = 'ITA'
                group by records.country_code,records.indicator_code
                order by c desc
                ''', conn)
df.plot.hist()
plt.show()

df = pd.read_sql_query('''
                        SELECT year,indicator_value as value
                        FROM records
                        WHERE indicator_code = 'SP.POP.TOTL' and country_code = 'ITA'
                        ORDER BY year;
                ''', conn)
df = df.set_index("year")
df.plot()
plt.show()

# closing the connection
conn.close()
