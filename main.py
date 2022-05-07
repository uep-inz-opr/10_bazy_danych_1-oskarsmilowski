import sqlite3
import csv


def main():
    nazwa_pliku = input()
    con = sqlite3.connect("baza.db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS CALLS")

    with open(nazwa_pliku, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        table = """ CREATE TABLE IF NOT EXISTS CALLS(
            from_sub TEXTNOT NULL,
            to_sub  TEXT NOT NULL,
            datetime NUMERIC,
            duration INT,
            celltower INT
        ); """  
        cur.execute(table)
        for row in reader:
            if len(row) > 1:
                cur.execute("INSERT INTO CALLS VALUES (?, ?, ?, ?, ?)", row)


        cur.execute("SELECT SUM(duration) FROM CALLS")
        print(cur.fetchone()[0])
        con.commit()
        con.close()
        return

if __name__ == "__main__":
    main()
