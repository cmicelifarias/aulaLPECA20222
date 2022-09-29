import sqlite3

conn = sqlite3.connect('pf.db') 
c = conn.cursor()

j = c.execute("SELECT * FROM alunos").fetchall()
                     
conn.commit()

print(j)
