import sqlite3

conn = sqlite3.connect('movies.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE MOVIES
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         ACTOR           TEXT    NOT NULL,
         ACTRESS           TEXT    NOT NULL,
         DIRECTOR           TEXT    NOT NULL,
         YEAR_OF_RELEASE            TEXT     NOT NULL);''')

conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (1, 'Sandesham', 'Sreenivasan', 'Mathu', 'Sathyan Anthikad' ,1991)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (2, 'Manichitrathazhu', 'Mohanlal', 'Shobana', 'Fazil' ,1993)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (3, 'Nadodikkattu', 'Mohanlal', 'Shobana', 'Sathyan Anthikad' ,1987)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (4, 'Kumbalangi Nights', 'Fahad Fasil', 'Anna Ben', 'Madhu C. Narayanan' ,2019)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (5, 'Devasuram', 'Mohanlal', 'Revathi', 'I.V. Sasi' ,1993)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (6, 'Chithram', 'Mohanlal', 'Renjini', 'Priyadarshan' ,1988)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (7, 'Drishyam 2', 'Mohanlal', 'Meena', 'Jeethu Joseph' ,2021)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (8, 'Drishyam', 'Mohanlal', 'Meena', 'Jeethu Joseph' ,2013)");
conn.execute("INSERT INTO MOVIES (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
      VALUES (9, 'Pathemari', 'Mammootty', 'Jewel Mary', 'Salim Ahmed' ,2015)");

cursor = conn.execute("SELECT ID, NAME, ACTOR, ACTRESS,DIRECTOR,YEAR_OF_RELEASE from MOVIES")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ACTOR = ", row[2])
    print("ACTRESS = ", row[3])
    print("DIRECTOR = ", row[4])
    print("YEAR OF RELEASE = ", row[5], "\n")

print("Movies Of Mohanlal \n")

actorname = conn.execute("SELECT ID, NAME, ACTOR, ACTRESS,DIRECTOR,YEAR_OF_RELEASE from MOVIES WHERE ACTOR = 'Mohanlal' ")
for row in actorname:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ACTOR = ", row[2])
    print("ACTRESS = ", row[3])
    print("DIRECTOR = ", row[4])
    print("YEAR OF RELEASE = ", row[5], "\n")

print("Operation done successfully")
conn.close()
