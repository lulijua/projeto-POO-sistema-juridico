# projeto-POO-sistema-juridico
Projeto de Programação Orientada a Objetos com a linguagem Python, desenvolvido durante a disciplina de POO do curso de Ciência da Computação da UFG em 2026.1.

# ⚖️ Sistema de Gestão de Processos Jurídicos

Um sistema de gerenciamento de processos judiciais construído em **Python**, desenvolvido para demonstrar a aplicação prática de Arquitetura de Software, princípios **SOLID** e o Design Pattern **State**.

O projeto conta agora com uma **Interface Web Interativa** completa, permitindo visualizar a mudança de estados e os bloqueios de regras de negócio operando em tempo real diretamente no navegador.

## 📌 Sobre o Projeto

Em sistemas corporativos reais, entidades frequentemente passam por ciclos de vida complexos. Este projeto simula o fluxo de um processo jurídico no Brasil (Abertura ➡️ Julgamento ➡️ Arquivamento). O objetivo principal foi resolver o desafio de gerenciar diferentes permissões e regras de negócio sem poluir o código com longas cadeias de condicionais (`if/else`).

## 🏗️ Arquitetura e Design Pattern (O Padrão State)

### O Problema

Normalmente, a validação de ações em um processo jurídico exigiria checagens constantes de status. Por exemplo: *Se a fase for "Aberto", o advogado pode anexar documentos; Se for "Em Julgamento", ninguém pode anexar nada.* Isso criaria um código altamente acoplado, difícil de testar e propenso a falhas caso novas fases precisassem ser adicionadas no futuro.

### A Solução

Para garantir que o código seja manutenível e seguro, a arquitetura foi baseada no **Padrão Comportamental State (GoF)**.

No lugar de condicionais, cada fase do processo foi encapsulada em sua própria classe (`FaseAberto`, `FaseEmJulgamento`, `FaseArquivado`). O objeto principal (`ProcessoJuridico`) não toma decisões sobre regras de negócio; ele simplesmente delega a ação para a classe que representa o seu estado atual.

<img width="4186" height="3610" alt="Processo Juridico-2026-05-26-181416" src="https://github.com/user-attachments/assets/b2298b22-d957-4180-b39f-7687a997a99b" />

### 🚀 Por que essa abordagem?

* **Responsabilidade Única (SRP):** Cada classe de estado gerencia apenas as regras da sua própria fase.
* **Aberto/Fechado (OCP):** Adicionar uma nova fase ao sistema no futuro exige apenas a criação de uma nova classe, sem necessidade de alterar o motor central.
* **Segurança (Fail-Safe):** Ações inválidas, como um juiz tentar arquivar um processo sem petição inicial ou um advogado tentar anexar provas fora do prazo, são bloqueadas nativamente pela arquitetura.

## ✨ Funcionalidades Principais

* **Interface Web (Streamlit):** Aplicação visual interativa e responsiva rodando no navegador (`localhost`).
* **Motor de Transição de Estados:** Mudança dinâmica de comportamento baseada na fase atual do processo.
* **Guardiões de Transição (Guards):** Bloqueios automatizados que impedem o avanço do processo se pré-requisitos não forem atendidos.
* **Controle de Acesso (RBAC):** Autorização baseada no papel do usuário logado (Juiz, Advogado, Estagiário).
* **Trilha de Auditoria (Audit Trail):** Registro histórico imutável com data e hora de todas as interações.
* **Persistência de Dados (JSON):** Salvamento e recuperação de processos em disco de forma estruturada.

## ⚙️ Como executar o projeto

Certifique-se de ter o Python instalado na sua máquina.

**1. Clone este repositório:**

```bash
git clone https://github.com/seu-usuario/sistema-juridico.git
cd sistema-juridico

```

**2. Instale as dependências (Streamlit):**

```bash
pip install streamlit

```

**3. Execute a Interface Web:**

```bash
python -m streamlit run app.py

```

> O seu navegador abrirá automaticamente em `http://localhost:8501` contendo a interface gráfica do sistema.

**Alternativa (Modo Terminal):**
Caso queira testar a versão em linha de comando (CLI) focada apenas no backend, execute:

```bash
python main.py

```

3. Execute o arquivo principal para abrir o terminal interativo:
```bash
python main.py

```

**Interface criada via Streamlit**

Aqui estão alguns exemplos de ações possíveis na interface web do sistema, que facilita a visualização e entendimento do mesmo.

Interface Web | Login e escolha de cargo.
<img width="1831" height="861" alt="image" src="https://github.com/user-attachments/assets/29bcc233-e89f-4d31-a1f0-0e44609220e1" />

Autuação de novo processo.
<img width="1831" height="861" alt="image" src="https://github.com/user-attachments/assets/3a1c43b1-f92d-4fd8-9253-d03d88c263b3" />

Tentativa de anexar documento ao processo com o cargo "Estágiario", ação bloqueada com sucesso.
<img width="1852" height="901" alt="image" src="https://github.com/user-attachments/assets/33a833ea-f5a0-4fd5-9bd3-936e2992992b" />

Anexação de documentos com o cargo "Juiz" realizada com sucesso.
<img width="1811" height="855" alt="image" src="https://github.com/user-attachments/assets/ef28602a-a1d4-4c9c-a3fb-c5516e9d3bbe" />

