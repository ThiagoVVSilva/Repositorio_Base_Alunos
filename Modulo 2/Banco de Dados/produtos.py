#importacao da biblioteca sqlite
import sqlite3



#criar o BD
produto = 'produtos.db'

script_produtos = '''CREATE TABLE IF NOT EXISTS produtos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        preco REAL NOT NULL,
                        categoria TEXT NOT NULL,
                        estoque INTEGER NOT NULL
                        );'''
try:
    with sqlite3.connect(produto) as con:
        #criar um cursor
        cur = con.cursor()

        #executar o script
        cur.execute(script_produtos)

        #save
        con.commit()
        print('tabela criada com sucesso')
except sqlite3.OperationalError as e:
    print('Erro:', e)

res = cur.execute('SELECT name FROM sqlite_master')
print(res.fetchall()) 


#consultar tabelas 
sql = 'SELECT * FROM produtos'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql)
        res = cur.fetchall() #retorna uma lista de lista
    
except sqlite3.OperationalError as e:
    print('ERROR:', e)

sql = 'INSERT INTO produtos(nome,preco,categoria,estoque) VALUES(?,?,?,?)'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,('Notebook Dell', 2500.00,'Eletronicos', 15))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro', e)

    # inserir varios dados

    #Lista de produtos para inserir

itens = [
        ('Notebook', 3500.00, 'Eletronicos', 10),
        ('Smartphone', 2200.00, 'Eletronicos', 15),
        ('Geladeira', 4800.00,'Eletrodomésticos', 15),
        ('Camiseta', 59.90, 'Vestuario', 50),
        ('Cafeteira',320.00, 'Eletrodomesticos', 8),
]
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.executemany('INSERT INTO produtos(nome,preco,categoria,estoque) VALUES(?,?,?,?)', itens)
        con.commit()
        print('produtos inseridos com sucesso')
except sqlite3.OperationalError as e:
    print('Erro:', e)

res = cur.execute('SELECT nome FROM produtos')
print(res.fetchall()) # este comando busca tds os registros)
 
#atualizar um registro

sql = 'UPDATE produtos SET preco = ? WHERE id = ?'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(7000,1))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro', e)

#deletar registros 

sql = 'DELETE FROM produtos WHERE id = ?'

try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()
        cur.execute(sql,(1,))
        con.commit()
except sqlite3.OperationalError as e:
    print('Erro', e)

# fechar a conexao. apos concluir precisamos fechar a conexao com o bd 

con.close()