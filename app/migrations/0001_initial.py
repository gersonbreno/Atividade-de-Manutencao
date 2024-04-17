# Generated by Django 4.2.3 on 2024-04-17 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_cliente', models.CharField(max_length=255)),
                ('endereco_de_entrega', models.TextField()),
                ('data_de_Entrega', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Frutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_fruta', models.CharField(max_length=100)),
                ('preco_da_fruta', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidadeDisponivel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtPgto', models.CharField(max_length=50)),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Verduras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_verdura', models.CharField(max_length=100)),
                ('preco_da_vedura', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade_disponivel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_item', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('prcUnit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='app.entrega')),
            ],
        ),
        migrations.AddField(
            model_name='entrega',
            name='pagamento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='entrega', to='app.pagamento'),
        ),
    ]
