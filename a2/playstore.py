import json
import csv
import sqlite3
import sys

db_file = 'googleplaystore.db'
conn = sqlite3.connect(db_file)


def create_google_table():
    """
    Here i am creating the table for my data.
    """
    c = conn.cursor()
    sql_str = """
        create table if not exists googleplay (
        id integer primary key autoincrement,
        datetime datetime,
        App text,
        Category text,
        Rating text,
        Reviews float,
        Size float,
        Installs int,
        Price float
        );
        """
    c.execute(sql_str)
    conn.commit()


def process_csv_file():

    c = conn.cursor()

    with open('googleplaystore.csv', 'r') as csvfile:

        # parse csv file pointer into hero_stream
        playstore = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        # interate over hero_stream to process. 
        for r_ct, playstore_row in enumerate(playstore):

            g_app = playstore_row['App']
            g_category = playstore_row['Category']
            g_rating = playstore_row['Rating']
            g_size = playstore_row['Size']
            g_installs = playstore_row['Installs']


            # only show the first 20 rows. 
            if r_ct <= 200:
                strsql = """
                    insert into googleplay ( App, Category, Rating, Size, Installs) values (
                    '{g_app}',
                    '{g_category}',
                    '{g_rating}',
                    '{g_size}',
                    '{g_installs}'
                    );
                """.format(
                    g_app=g_app,
                    g_category=g_category,
                    g_rating=g_rating,
                    g_size=g_size,
                    g_installs=g_installs
                )
                c.execute(strsql)
                conn.commit()

            # only show the first 20 rows. 
            if r_ct <= 20:
                print(r_ct, g_app, g_category, g_rating, g_size, g_installs)


def main():
    print('Creating a DB from a csv file.')
    create_google_table()
    process_csv_file()

if __name__ == "__main__":
	main()
