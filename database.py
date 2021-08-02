import sqlite3  # importando biblioteca do sqlite

conn = sqlite3.connect(r'./projeto/exemplodatabase.db')  # fazendo a conexao e criacao do o banco de dados

c = conn.cursor()  # criando o curso para a manipulacao de tabelas

# criando as tuplas para inserir nas tabelas
users = [('28150800801', 'Diego', 'diego.bolinha@gmail.com', '12345', '18998176211'),
         ('12345678910', 'Fernanda Montenegro', 'fernanda.montenegro@gmail.com', '123456', '18991685421'),
         ('13246587902', 'Billie Elish', 'bellichelinda@uol.com.br', 'abcd1234', '18997613214'),
         ('14440987617', 'Jonas Brothers', 'irmaosjoao@hotmail.com.br', 'efg54321', '18996271833'),
         ('37176287123', 'Michael Johson', 'johson.michael@hotmail.com.br', 'hijk1234', '18992317786'),
         ]
# criando as tuplas para inserir nas tabelas
produtos = [('1', 'Bateria Azul', 'baterias', '6200.00', 'Bateria nova no mercado na cor Azul'),
            ('2', 'Baqueta Zaia', 'baquetas', '50.00', 'Baqueta usada pelo famoso baterista Zaia'),
            ('3', 'Prato Amarelo', 'pratos', '230.00', 'Prato generico amarelo'),
            ('4', 'Bateria Roxa', 'baterias', '7800.00', 'Bateria old-school na cor roxa'),
            ('5', 'Baqueta Fominha', 'baquetas', '27.00', 'Baqueta usada pelo gaiteiro baterista da encrusilhada'),
            ]
# criando as tuplas para inserir nas tabelas
address = [('Rua Bela, numero 120, Vila Nova. Presidente Prudente-SP', '28150800801'),
           ('Rua Feia, numero 21, Watal Ishibashi. Presidente Prudente-SP', '12345678910'),
           ('Rua Holmes, numero 99, Sherlock. Presidente Prudente-SP ', '13246587902'),
           ('Avenida Brasil, numero 1620, Centro. Presidente Prudente-SP', '14440987617'),
           ('Avenida Coronel Marcondes, numero 51, Centro. Presidente Prudente-SP', '37176287123'),
           ]
# criando as tuplas para inserir nas tabelas
admin = [('28870800801', 'Natalia Abuquerque', 'nat.abuquerque@hotmail.com.br', '@&!HolycraCe', '11988136241'),
         ('12345677652', 'Joaquina Barberi', 'joaquina_barberi@gmail.com', '_*^%@!OET', '18993416216'),
         ('23248583902', 'Heitor Felipe', 'heitor_felipe77@gmail.com', '123qwaszsxzx', '67993172148'),
         ('34440237607', 'Thiago Nunes', 'thiago.nunes02@outlook.com.br', '/.9;[p09', '43995118239'),
         ('32146297103', 'Ricardo Portaluppi', 'ricardoportaluppi@gmail.com', '76213qwz1235qwdxzxz', '67998176211'),
         ]

# criando a tabela de users
c.execute("""CREATE TABLE users(
        cpf INTEGER PRIMARY KEY,        
        nome TEXT,
        email TEXT,
        senha TEXT,
        tel TEXT
)""")

# criando as tabelas de produtos
c.execute("""CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        nome TEXT,
        categoria TEXT,
        preco REAL,
        descricao TEXT
)""")

# criando a tabela de enderecos
c.execute("""CREATE TABLE address(
        addres TEXT,
        cpf_usr,
        FOREIGN KEY (cpf_usr) REFERENCES users(cpf)
) """)

# criando a tabela de admin
c.execute("""CREATE TABLE admin(
        cpf INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT,
        senha TEXT,
        tel TEXT
    )""")

# populando as tabelas com as duplas preiamente criadas
c.executemany(" INSERT INTO users VALUES (?,?,?,?,?)", users)
c.executemany(" INSERT INTO products VALUES (?,?,?,?,?)", produtos)
c.executemany(" INSERT INTO address VALUES (?,?)", address)
c.executemany(" INSERT INTO admin VALUES (?,?,?,?,?)", admin)

# dando commit nas mudancas do banco
conn.commit()
# desligando a conexao com o banco de dados
conn.close()
