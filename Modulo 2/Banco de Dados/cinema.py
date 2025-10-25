#
import sqlite3

con= sqlite3.connect('cinema.db') # cria ou se connect com um banco existente

# criar um objeto cursor 
cur = con.cursor()

#criar tabelas
cur.execute('CREATE TABLE  IF NOT EXISTS filme(titulo, ano, duracao)')
# retorna com o endereço de memoria da tabela 

#verificar se a tabela foi criada
res = cur.execute('SELECT name FROM sqlite_master')
print(res.fetchall())

# # inserir dados
# cur.execute('''INSERT INTO filme VALUES
#             ('O Senhor dos Anéis: A Sociedade do Anel',2001,178),
#             ('Cona, O Barbaro',1982,129)''')
# con.commit() #isto é para salvar, e sempre salve seu burro

#para verificar os dados foram inseridos corretamente
res = cur.execute('SELECT titulo FROM filme')
print(res.fetchall())

# dados_filme = [
#     ('Indiana Jones e a Ultima Cruzada', 1989,127),
#     ('O Nome da Rosa', 1986, 126),
#     ('Deus e o Diabo na Terra do Sol', 1964,120),
#     ('De Volta Para o Futuro', 1985,116)
# ]

# cur.executemany('INSERT INTO filme (titulo, ano, duracao) VALUES(?,?,?)',dados_filme)
# con.commit()

# RES = cur.execute('SELECT titulo FROM filme')
# print(res.fetchall())

#outra forma de verificar os dados inseridos 
for linha in cur.execute('SELECT ano, titulo FROM filme ORDER BY ano'):
    print(linha)

con.close() # para fechar a conexão