# projeto-POO-sistema-juridico
Projeto de Programação Orientada a Objetos com a linguagem Python, desenvolvido durante a disciplina de POO do curso de Ciência da Computação da UFG em 2026.1.

# ⚖️ Sistema de Gestão de Processos Jurídicos

Um sistema de gerenciamento de processos judiciais construído em **Python**, desenvolvido para demonstrar a aplicação prática de Arquitetura de Software, princípios **SOLID** e o Design Pattern **State**.

## 📌 Sobre o Projeto

Em sistemas corporativos reais, entidades frequentemente passam por ciclos de vida complexos. Este projeto simula o fluxo de um processo jurídico no Brasil (Abertura ➡️ Julgamento ➡️ Arquivamento). O objetivo principal foi resolver o desafio de gerenciar diferentes permissões e regras de negócio sem poluir o código com longas cadeias de condicionais (`if/else`).

O sistema conta com uma interface via linha de comando (CLI), controle de acesso por perfis (Advogados, Juízes e Estagiários) e persistência de dados em disco utilizando o formato estruturado JSON.

## 🏗️ Arquitetura e Design Pattern (O Padrão State)

### O Problema

Normalmente, a validação de ações em um processo jurídico exigiria checagens constantes de status. Por exemplo: *Se a fase for "Aberto", o advogado pode anexar documentos; Se for "Em Julgamento", ninguém pode anexar nada.* Isso criaria um código acoplado, difícil de testar e propenso a falhas caso novas fases precisassem ser adicionadas no futuro.

### A Solução

Para garantir que o código seja manutenível e seguro, a arquitetura foi baseada no **Padrão Comportamental State (GoF)**.

No lugar de condicionais, cada fase do processo foi encapsulada em sua própria classe (`FaseAberto`, `FaseEmJulgamento`, `FaseArquivado`). O objeto principal (`ProcessoJuridico`) não toma decisões sobre regras de negócio; ele simplesmente delega a ação para a classe que representa o seu estado atual.

<img width="4186" height="3610" alt="Processo Juridico-2026-05-26-181416" src="https://github.com/user-attachments/assets/6ab92b47-567c-4aa2-860a-350ead47263e" />

### 🚀 Por que essa abordagem?

* **Responsabilidade Única (SRP):** Cada classe de estado gerencia apenas as regras da sua própria fase.
* **Aberto/Fechado (OCP):** Adicionar uma nova fase ao sistema no futuro (ex: "Fase de Recurso") exige apenas a criação de uma nova classe, sem necessidade de alterar o código já existente.
* **Segurança (Fail-Safe):** Ações inválidas, como um juiz tentar arquivar um processo sem petição inicial ou um advogado tentar anexar provas fora do prazo, são bloqueadas nativamente pela arquitetura do sistema.

## ✨ Funcionalidades Principais

* **Motor de Transição de Estados:** Mudança dinâmica de comportamento baseada na fase atual do processo.
* **Guardiões de Transição (Guards):** Bloqueios automatizados que impedem o avanço do processo se pré-requisitos (como a presença de documentos) não forem atendidos.
* **Controle de Acesso (RBAC):** Autorização baseada no papel do usuário (Juiz, Advogado).
* **Trilha de Auditoria (Audit Trail):** Registro histórico imutável com data e hora de todas as interações realizadas no processo.
* **Persistência de Dados (JSON):** Salvamento e recuperação de processos em disco de forma estruturada.

## ⚙️ Como executar o projeto

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/sistema-juridico.git

```


2. Navegue até a pasta do projeto:
```bash
cd sistema-juridico

```


3. Execute o arquivo principal para abrir o terminal interativo:
```bash
python main.py

```
