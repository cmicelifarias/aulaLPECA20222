import sqlite3

conn = sqlite3.connect('pf.db') 
c = conn.cursor()

a = input("Me diga seu DRE: ")
b = input ("Me diga seu nome: ")

c.execute("INSERT INTO alunos VALUES ('"+a+"','"+b+"')")
          
                     
conn.commit()
