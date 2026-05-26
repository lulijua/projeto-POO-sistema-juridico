#Esse arquivo é responsável por fazer o controle de acesso do sistema.
# usuario.py

class Usuario:
    def __init__(self, nome: str, papel: str):
        self.nome = nome
        self.papel = papel

    def __str__(self):
        return f"{self.nome} ({self.papel})"