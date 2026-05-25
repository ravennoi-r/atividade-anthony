class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def adicionar_estoque(self, qtd):
        self.quantidade += qtd

    def remover_estoque(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd


produto1 = Produto("Mouse", 50, 10)
produto2 = Produto("Teclado", 100, 5)

produtos = [produto1, produto2]

total = 0

for produto in produtos:
    total += produto.valor_total()

print(f"Valor total em estoque: R$ {total:.2f}")