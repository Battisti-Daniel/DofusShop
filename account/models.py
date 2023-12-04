from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    stars = models.PositiveIntegerField(default=0)
    authenticated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["-created_at"]


class AccountAmount(models.Model):
    account_create = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Gear(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="coverGear/")

    def __str__(self):
        return f"{self.name}"


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="coverItem/")
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class ItemAmount(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    total_item = models.IntegerField()


class Transacao(models.Model):
    STATUS_CHOICES = [
        ("em_andamento", "Em Andamento"),
        ("concluida", "Concluída"),
        ("cancelada", "Cancelada"),
    ]

    ESTAGIO_CHOICES = [
        ("negociacao", "Negociação"),
        ("pagamento", "Pagamento"),
        ("entrega", "Entrega"),
    ]

    comprador = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transacoes_como_comprador"
    )
    vendedor = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transacoes_como_vendedor"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="em_andamento"
    )
    estagio = models.CharField(
        max_length=20, choices=ESTAGIO_CHOICES, default="negociacao"
    )
    descricao = models.TextField()

    def __str__(self):
        return f"Transação {self.pk}"


class Conjunto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    itens = models.ManyToManyField(Item)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

"""
CREATE SCHEMA dofusshop;
USE dofusshop;

CREATE TABLE account (
    id BINARY(16) PRIMARY KEY,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(128),
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    stars INT DEFAULT 0,
    authenticated BOOLEAN DEFAULT FALSE,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

CREATE TABLE accountamount (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_create INT NOT NULL,
    created_at DATETIME NOT NULL
);

CREATE TABLE gear (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    cover VARCHAR(100) NOT NULL
);

CREATE TABLE server (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE item (
    id BINARY(16) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    value FLOAT NOT NULL,
    gear_id BINARY(16),
    cover VARCHAR(100) NOT NULL,
    account_id BINARY(16),
    server_id BINARY(16),
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (gear_id) REFERENCES gear(id),
    FOREIGN KEY (account_id) REFERENCES account(id),
    FOREIGN KEY (server_id) REFERENCES server(id)
);

CREATE TABLE itemamount (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    total_amount FLOAT NOT NULL,
    total_item INT NOT NULL
);

CREATE TABLE transacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comprador_id BINARY(16),
    vendedor_id BINARY(16),
    status VARCHAR(20) DEFAULT 'em_andamento',
    estagio VARCHAR(20) DEFAULT 'negociacao',
    descricao TEXT,
    FOREIGN KEY (comprador_id) REFERENCES account(id),
    FOREIGN KEY (vendedor_id) REFERENCES account(id)
);

CREATE TABLE conjunto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    user_id BINARY(16),
    FOREIGN KEY (user_id) REFERENCES account(id)
);

CREATE TABLE conjunto_itens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conjunto_id INT,
    item_id BINARY(16),
    FOREIGN KEY (conjunto_id) REFERENCES conjunto(id),
    FOREIGN KEY (item_id) REFERENCES item(id)
); 


Criacao

INSERT INTO account (id, email, stars, authenticated, created_at, updated_at)
VALUES ('UUID_HERE', 'example@email.com', 0, false, '2023-11-27 00:00:00', '2023-11-27 00:00:00');

INSERT INTO gear (id, name, cover)
VALUES ('UUID_HERE', 'Gear Name', 'path/to/cover.jpg');

INSERT INTO server (id, name)
VALUES ('UUID_HERE', 'Server Name');

INSERT INTO item (id, name, value, gear_id, cover, account_id, server_id, created_at, updated_at)
VALUES ('UUID_HERE', 'Item Name', 10.0, 'Gear_UUID', 'path/to/item_cover.jpg', 'Account_UUID', 'Server_UUID', '2023-11-27 00:00:00', '2023-11-27 00:00:00');

INSERT INTO transacao (comprador_id, vendedor_id, status, estagio, descricao)
VALUES ('Comprador_Account_UUID', 'Vendedor_Account_UUID', 'em_andamento', 'negociacao', 'Descrição da transação');

INSERT INTO conjunto (nome, descricao, user_id)
VALUES ('Conjunto Name', 'Descrição do conjunto', 'Account_UUID');

Leitura

SELECT * FROM account;

SELECT * FROM gear;

SELECT * FROM server;

SELECT * FROM item;

SELECT * FROM transacao;

SELECT * FROM conjunto;

Update

UPDATE account SET email = 'new_email@example.com', stars = 5 WHERE id = 'Account_UUID';

UPDATE gear SET name = 'New Gear Name' WHERE id = 'Gear_UUID';

UPDATE server SET name = 'New Server Name' WHERE id = 'Server_UUID';

UPDATE item SET name = 'New Item Name', value = 15.0 WHERE id = 'Item_UUID';

UPDATE transacao SET status = 'concluida' WHERE id = 'Transaction_UUID';

UPDATE conjunto SET descricao = 'Nova descrição do conjunto' WHERE id = 'Conjunto_UUID';

DELETE FROM account WHERE id = 'Account_UUID';

DELETE FROM gear WHERE id = 'Gear_UUID';

DELETE FROM server WHERE id = 'Server_UUID';

DELETE FROM item WHERE id = 'Item_UUID';

DELETE FROM transacao WHERE id = 'Transaction_UUID';

DELETE FROM conjunto WHERE id = 'Conjunto_UUID';

"""
