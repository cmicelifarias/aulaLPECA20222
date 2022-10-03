import sqlite3

conn = sqlite3.connect('pf.db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS alunos
          ([dre] STRING PRIMARY KEY, [nome] STRING, [senha] STRING );
          CREATE TABLE IF NOT EXISTS notas
          ([dre] STRING, [idcurso] STRING, [p1] INTEGER, [p2] INTEGER, [p3] INTEGER);
          ''')
          
                     
conn.commit()
