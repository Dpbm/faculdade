"""
Aqui, definimos 3 classes representando os subsistemas usados pelo FACADE.
Esses, são partes externas que realizam operações complexas que nossa classe
Facade vai utilizar para abstrair a complexidade.
"""

class CatalogManager:
    def __init__(self):
       self.books = {}

    def add_book(self, book_id, details):
        self.books[book_id] = details
        print(f"Book added: {details}")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book {book_id} removed")
        else:
            print("Book not found")
    
    def find_book(self, book_id):
        return self.books.get(book_id, "Book not found")
    
class OrderManager:
    def create_order(self, book_id, user_id):
        print(f"Order created for book {book_id} by user {user_id}")
    
class PaymentProcessor:
    def __init__(self, method):
        self._method = method

    def process_payment(self, user_id, book):
        print(f"Processed payment ({self._method})\nbook: {book['title']}\nprice: ${book['price']}\nuser id: {user_id}")

"""
A classe Facade apresentada abaixo, é a classe responsável por gerenciar 
as instâncias das classes de subsistema e expor ao usuário uma interface simple e amigável que
realiza as operação que ele precisa.
"""

class BookstoreFacade:
    def __init__(self):
        self.catalog = CatalogManager()
        self.orders = OrderManager()

    def place_order(self, book_id, user_id, payment_method):
        book = self.catalog.find_book(book_id)
        if book != "Book not found":
            payment_processor = PaymentProcessor(payment_method)
            self.orders.create_order(book_id, user_id)
            payment_processor.process_payment(user_id, book)
            print("Order placed successfully")
        else:
            print(f"Book {book_id} not available")


"""
Aqui, utilizamos a classe Facade para processa o pedido dos livros, sem a necessidade de interagir 
com classes adicionais.
"""
if __name__ == "__main__":
    facade = BookstoreFacade()
    user_id = 101

    # encontra o livro e faz o pedido
    facade.catalog.add_book(1, {"title":"The Great Gatsby", "price":15.99})
    
    print(end="\n\n")
    
    facade.place_order(1, user_id, "pix")

    print(end="\n\n")

    # livro não encontrado
    facade.place_order(2, user_id, "boleto")
    
    print(end="\n\n")
    
    # encontra o livro e faz o segundo pedido
    facade.catalog.add_book(2, {"title":"The Hobbit", "price":140.3})
    
    print(end="\n\n")
    
    facade.place_order(2, user_id, "paypal")