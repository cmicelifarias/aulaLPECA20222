import sqlite3

conn = sqlite3.connect('pf.db') 
c = conn.cursor()

a = input("Diga quem roda: ")

c.execute("DELETE from alunos where nome = '"+a+"'")
#"DELETE from alunos where nome = ?, (a,)"          
                     
conn.commit()
