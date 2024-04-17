from django.db import models
# bejo que nomes esta sem sentido ou sej primeiro passo ajsurta isso
class Produto(models.Model):
    nome_do_produto = models.CharField(max_length=100)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_disponivel = models.IntegerField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome_da_verdura
class Verduras(Produto):
    class Meta:
        verbose_name_plural = "Verduras"
    

class Frutas(Produto):
    class Meta:
        verbose_name_plural = "Produtos"

class Entrega(models.Model):
    nome_do_cliente = models.CharField(max_length=255)
    endereco_de_entrega = models.TextField()
    data_de_entrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')
    def __str__(self):
        return self.nome_do_cliente

class Pagamento(models.Model):
    metodo_de_pagamento = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.metodo_de_pagamento


class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nome_do_produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return  f"{self.entrega}"
