import sqlite3  # importando biblioteca do sqlite

# fazendo a conexao e criacao do o banco de dados
conn = sqlite3.connect('exemplodatabase.db')

# criando o curso para a manipulacao de tabelas por meio de comandos sqlite
c = conn.cursor()

# criando as tuplas para inserir nas tabelas
users = [('28150800801', 'Diego', 'diego.bolinha@gmail.com', '12345', '18998176211'),
         ('12345678910', 'Fernanda Montenegro',
          'fernanda.montenegro@gmail.com', '123456', '18991685421'),
         ('13246587902', 'Billie Elish',
          'bellichelinda@uol.com.br', 'abcd1234', '18997613214'),
         ('14440987617', 'Jonas Brothers',
          'irmaosjoao@hotmail.com.br', 'efg54321', '18996271833'),
         ('37176287123', 'Michael Johson',
          'johson.michael@hotmail.com.br', 'hijk1234', '18992317786'),
         ]
# criando as tuplas para inserir nas tabelas
categories = [('1', 'Baterias'),
              ('2', 'Baquetas'),
              ('3', 'Pratos'),
              ('4', 'Peles'),
              ('5', 'Ferragens')
              ]
# criando as tuplas para inserir nas tabelas
produtos = [('1', 'Bateria Azul', '1', '6200.00', 'Bateria nova no mercado na cor Azul'),
            ('2', 'Baqueta Zaia', '2', '50.00',
             'Baqueta usada pelo famoso baterista Zaia'),
            ('3', 'Prato Amarelo', '3', '230.00', 'Prato generico amarelo'),
            ('4', 'Bateria Roxa', '1', '7800.00',
             'Bateria old-school na cor roxa'),
            ('5', 'Baqueta Fominha', '2', '27.00',
             'Baqueta usada pelo gaiteiro baterista da encrusilhada'),
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
         ('12345677652', 'Joaquina Barberi',
          'joaquina_barberi@gmail.com', '_*^%@!OET', '18993416216'),
         ('23248583902', 'Heitor Felipe',
          'heitor_felipe77@gmail.com', '123qwaszsxzx', '67993172148'),
         ('34440237607', 'Thiago Nunes',
          'thiago.nunes02@outlook.com.br', '/.9;[p09', '43995118239'),
         ('32146297103', 'Ricardo Portaluppi', 'ricardoportaluppi@gmail.com',
          '76213qwz1235qwdxzxz', '67998176211'),
         ]
# criando as tuplas para inserir nas tabelas
carrinho = [('1', '12345678910'),
            ('2', '28150800801'),
            ('3', '14440987617'),
            ('4', '37176287123'),
            ('5', '13246587902')
            ]
# criando as tuplas para inserir nas tabelas
order = [('1', '1', '1', '5'),
         ('2', '3', '1', '4'),
         ('3', '4', '1', '3'),
         ('4', '2', '2', '2'),
         ('5', '5', '4', '1')
         ]

# criando a tabela de users
c.execute("""CREATE TABLE users(
        cpf INTEGER PRIMARY KEY,      
        nome TEXT,
        email TEXT,
        senha TEXT,
         tel TEXT
 )""")

# criando tabela de categorias dos produtos
c.execute("""CREATE TABLE categories(
       category_id INTEGER PRIMARY KEY,
       category TEXT
)""")

# criando a tabela de produtos
c.execute("""CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        nome TEXT,
        category TEXT,
        preco REAL,
        descricao TEXT,
        FOREIGN KEY (category) REFERENCES categories(category)
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

# criando tabela de carrinho que contem os pedidos do usr
c.execute("""CREATE TABLE cart(
        cart_id INTEGER PRIMARY KEY,
        cpf_usr,
        FOREIGN KEY (cpf_usr) REFERENCES users(cpf)
)""")

# criando tabela de pedidos que contem o produto e a quantidade
c.execute("""CREATE TABLE order(
        order_id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER,
        cart_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (cart_id) REFERENCES cart(cart_id)

)""")

# populando as tabelas com as duplas preiamente criadas
# a funcao executemany faz com que o cursor execute varias vezes o comando sqlite enquanto for possivel
# Nesse caso passei uma lista de tuplas como parametro para os comandos
# o (?) eh um placeholder para que funcione bem o comandos e os parametros passados
c.executemany(" INSERT INTO users VALUES (?,?,?,?,?)", users)
c.executemany(" INSERT INTO categories VALUES (?,?)", categories)
c.executemany(" INSERT INTO products VALUES (?,?,?,?,?)", produtos)
c.executemany(" INSERT INTO orders VALUES (?,?,?,?)", order)
c.executemany(" INSERT INTO address VALUES (?,?)", address)
c.executemany(" INSERT INTO admin VALUES (?,?,?,?,?)", admin)

# dando commit nas mudancas do banco
conn.commit()
# desligando a conexao com o banco de dados
conn.close()
