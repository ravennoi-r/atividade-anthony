class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def apresentar(self):
        print(
            f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e meu e-mail é {self.email}."
        )


pessoa = Pessoa("Ana", 20, "ana@email.com")
pessoa.apresentar()