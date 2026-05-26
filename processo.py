# processo.py

import json
import os
from datetime import datetime

# Precisamos importar todas as fases para poder recriá-las ao carregar o arquivo
from fases import FaseAberto, FaseEmJulgamento, FaseArquivado
from usuario import Usuario

class ProcessoJuridico:
    def __init__(self, numero: str):
        self.numero = numero
        self.documentos = []
        self.historico = []  
        
        self.estado_atual = FaseAberto()
        self.registrar_historico("Processo autuado e cadastrado no sistema.")

    def registrar_historico(self, mensagem: str):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        registro = f"[{agora}] {mensagem}"
        self.historico.append(registro)

    def anexar_documento(self, usuario: Usuario, documento: str):
        self.estado_atual.anexar_documento(self, usuario, documento)

    def avancar_fase(self, usuario: Usuario):
        self.estado_atual.avancar_fase(self, usuario)

    def exibir_auditoria(self):
        print(f"\n=== HISTÓRICO DO PROCESSO {self.numero} ===")
        for linha in self.historico:
            print(linha)
        print("======================================\n")

    # ==========================================
    # NOVAS FUNÇÕES DE PERSISTÊNCIA (JSON)
    # ==========================================
    def salvar_dados(self):
        """Salva o estado atual do objeto em um arquivo JSON no disco rígido."""
        dados_para_salvar = {
            "numero": self.numero,
            "documentos": self.documentos,
            "historico": self.historico,
            "fase_atual": self.estado_atual.__class__.__name__  # Salva apenas o nome da fase
        }
        
        nome_arquivo = f"processo_{self.numero}.json"
        
        # ensure_ascii=False garante que os acentos do português fiquem corretos no arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados_para_salvar, arquivo, indent=4, ensure_ascii=False)
            
        print(f"Sucesso: Dados salvos com segurança no arquivo '{nome_arquivo}'.")

    @classmethod
    def carregar_dados(cls, numero_processo: str):
        """Lê um arquivo JSON do disco e remonta o objeto ProcessoJuridico."""
        nome_arquivo = f"processo_{numero_processo}.json"
        
        if not os.path.exists(nome_arquivo):
            raise FileNotFoundError(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
            
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            
        # 1. Cria um processo base
        processo_recuperado = cls(dados["numero"])
        
        # 2. Sobrescreve as listas com os dados que vieram do JSON
        processo_recuperado.documentos = dados["documentos"]
        processo_recuperado.historico = dados["historico"]
        
        # 3. O Truque do State: Analisa o texto e "pluga" a classe correta
        nome_fase = dados["fase_atual"]
        if nome_fase == "FaseAberto":
            processo_recuperado.estado_atual = FaseAberto()
        elif nome_fase == "FaseEmJulgamento":
            processo_recuperado.estado_atual = FaseEmJulgamento()
        elif nome_fase == "FaseArquivado":
            processo_recuperado.estado_atual = FaseArquivado()
            
        print(f"Sucesso: Processo {numero_processo} carregado do disco e remontado na memória.")
        return processo_recuperado