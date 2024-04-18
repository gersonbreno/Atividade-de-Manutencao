from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nome_do_produto', 'preco_unitario', 'quantidade_disponivel']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nome_do_produto', 'preco_unitario', 'quantidade_disponivel']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nome_do_cliente', 'endereco_de_entrega', 'data_de_entrega', 'itens', 'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['metodo_de_pagamento', 'valor_total']

class ItemSerializer(serializers.ModelSerializer):
    entrega = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['nome_do_item', 'quantidade_de_item', 'preco_unitario_do_item', 'entrega']
