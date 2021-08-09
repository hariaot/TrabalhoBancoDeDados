import sqlite3  # importando biblioteca do sqlite

conn = sqlite3.connect('exemplodatabase.db')  # fazendo a conexao e criacao do o banco de dados

c = conn.cursor()  # criando o curso para a manipulacao de tabelas

# ('order_id', 'Product_id', 'Quantidade', 'ID_carrinho')
order = [('1', '1', '1', '5'),
         ('2', '3', '1', '4'),
         ('3', '4', '1', '3'),
         ('4', '2', '2', '2'),
         ('5', '5', '4', '1')
]

c.executemany(" INSERT INTO orders VALUES (?,?,?,?)", order)

# dando commit nas mudancas do banco
conn.commit()
# desligando a conexao com o banco de dados
conn.close()
