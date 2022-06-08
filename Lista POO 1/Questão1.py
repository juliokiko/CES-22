# Livraria

# Aqui, definem-se os produtos que serão vendidos na livraria

class Produtos:

# Primeiramente, os produtos da cafeteria, que poderão ser adicionados ou retirados pelo dono da livraria como ele desejar

  class Produto_Cafeteria:
    def __init__(self, produto, preço):
      self.produto = produto
      self.preço = preço

    def deleta_produto(self):
      self.produto = None
      self.preço = None

    def ExibirProdutoCafeteria(self):
      print(self.produto)

# Aqui, os livros são definidos com suas características, incluindo as operações de adição, remoção e edição para cada livro

  class Livro:

    def __init__(self, título, edição, autor, gênero, editora, preço_de_venda, preço_de_compra, imposto_gênero):

      self.título = título
      self.edição = edição
      self.editora = editora
      self.autor = autor
      self.gênero = gênero
      self.preço_de_venda = preço_de_venda
      self.preço_de_compra = preço_de_compra
      self.imposto_gênero = imposto_gênero

    def deleta_livro(self):

      self.título = None
      self.edição = None
      self.editora = None
      self.autor = None
      self.gênero = None
      self.preço_de_venda = None
      self.preço_de_compra = None
      self.imposto_gênero = None
      

    def ExibirTítuloLivro(self):
      print(self.título)

    def ExibirEdiçãoLivro(self):
      print(self.edição)

    def ExibirEditoraLivro(self):
      print(self.editora)

    def ExibirAutorLivro(self):
      print(self.autor)

    def ExibirGêneroLivro(self):
      print(self.gênero)

    def ExibirPreçodeVendaLivro(self):
      print(self.preço_de_venda)

    def ExibirPreçodeCompraLivro(self):
      print(self.preço_de_compra)

    def ExibirImpostoGêneroLivro(self):
      print(self.imposto_gênero)

# Agora, definem-se o cadastro dos autores, com as principais características e uma lista de livros publicados para consulta, com sua possível exclusão

class Autor:

      def __init__(self, nome, email):
        self.nome = nome
        self.email = email

      def ExibirNomeAutor(self):
        print(self.nome)

      def ExibirEmailAutor(self):
        print(self.email)  

      class Livros_Publicados:
        def __init__(self, título):
          self.título = título

        def deleta_livro_publicado(self):
          self.título = None

        def ExibirTítuloLivroPublicado(self):
          print(self.título)

# O cadastro de clientes, com as principais informações de identificação e possibilidade de inserção, remoção e consulta, assim como uma lista de compra,
# pode ser manipulada da mesma forma

class Clientes:

      def __init__(self, nome, email):
        self.nome = nome
        self.email = email

      def deleta_cliente(self):
        self.nome = None
        self.email = None

      def ExibirNomeCliente(self):
        print(self.nome)

      def ExibirEmailCliente(self):
        print(self.email)  
      

      class Compras:

        def __init__(self, quantidade_produto, produto, preço):
          self.quantidade_produto = quantidade_produto
          self.produto = produto
          self.preço = preço

        def deleta_compra(self):
          self.quantidade_produto = None
          self.produto = None
          self.preço = None

        def ExibirQuantidadeCompra(self):
          print(self.quantidade_produto)
        
        def ExibirProdutosCompra(self):
          print(self.produto)

        def ExibirPreçoCompra(self):
          print(self.preço)
      
      
# Aqui, adiciona-se produtos, livros, autores, clientes e compras para compor a análise da livraria

produto_cafeteria_1 = Produtos.Produto_Cafeteria('Cafezinho','R$ 5,00')
produto_cafeteria_2 = Produtos.Produto_Cafeteria('Pão de Queijo','R$ 8,00')
produto_cafeteria_3 = Produtos.Produto_Cafeteria('Água','R$ 4,00')

livro1 = Produtos.Livro('As aventuras de um engenheiro', '3ª edição', 'Einstein', 'Terror', 'Scipione', 'R$ 50,00', 'R$ 40,00', 'R$ 10,00')
livro2 = Produtos.Livro('Como criar um jogo em um bimestre', '1ª edição', 'Marie Curie', 'Suspense', 'Ática', 'R$ 100,00', 'R$ 80,00', 'R$ 20,00')
livro3 = Produtos.Livro('Buracos negros existem?', '6ª edição', 'Einstein', 'Ficção Científica', 'Scipione', 'R$ 147,50', 'R$ 117,00', 'R$ 30,50')
livro4 = Produtos.Livro('A lenda de um ninja determinado', '10ª edição', 'Jiraya', 'Aventura', 'Konoha', 'R$ 230,00', 'R$ 130,00', 'R$ 100,00')
livro5 = Produtos.Livro('Desafios de criar um site em 2 meses', '8ª edição', 'Nikolas Tesla', 'Drama', 'Martin Claret', 'R$ 10,00', 'R$ 6,30', 'R$ 3,70')
livro6 = Produtos.Livro('Contos em um Paraíso Tropical', '23ª edição', 'Jiraya', 'Romance', 'Konoha', 'R$ 450,00', 'R$ 300,00', 'R$ 150,00')

autor1 = Autor('Einstein', 'einstein@relatividade.com')
autor1_livro1 = autor1.Livros_Publicados(livro1.título)
autor1_livro2 = autor1.Livros_Publicados(livro3.título)

autor2 = Autor('Marie Curie', 'mariecurie@nobel.com')
autor2_livro1 = autor2.Livros_Publicados(livro2.título)

autor3 = Autor('Jiraya', 'jiraya@konoha.com')
autor3_livro1 = autor3.Livros_Publicados(livro4.título)
autor3_livro2 = autor3.Livros_Publicados(livro6.título)
          
autor4 = Autor('Nikolas Tesla', 'nikolastesla@eletricidade.com')
autor4_livro1 = autor4.Livros_Publicados(livro5.título)

cliente1 = Clientes('Susane', 'susaninharebelde@hotmail.com')
cliente1_compra1 = cliente1.Compras(1, livro6.título, livro6.preço_de_venda)
cliente1_compra2 = cliente1.Compras(2, produto_cafeteria_1.produto, produto_cafeteria_1.preço)

cliente2 = Clientes('Mauro', 'maurohokage@gmail.com')
cliente2_compra1 = cliente2.Compras(3, livro4.título, livro4.preço_de_venda)

cliente3 = Clientes('Ariel', 'arielsapekinhe@yahoo.com')
cliente3_compra1 = cliente3.Compras(3, produto_cafeteria_2.produto, produto_cafeteria_2.preço)
cliente3_compra2 = cliente3.Compras(2, produto_cafeteria_3.produto, produto_cafeteria_3.preço)

print('Bem-vindo à Livraria!')