# main.py

import sys
from usuario import Usuario
from processo import ProcessoJuridico

def limpar_tela():
    # Apenas para deixar o menu mais limpo no terminal (funciona no Windows e Linux/Mac)
    print("\n" * 2)

def iniciar_sistema():
    print("==================================================")
    print("SISTEMA DE GESTÃO DE PROCESSOS JURÍDICOS")
    print("==================================================")
    
    # 1. Cadastro do Usuário que vai operar o sistema
    print("\n--- IDENTIFICAÇÃO DO USUÁRIO ---")
    nome = input("Digite o seu nome: ")
    
    print("Qual é o seu cargo?")
    print("[ 1 ] Advogado")
    print("[ 2 ] Juiz")
    print("[ 3 ] Estagiário")
    
    opcao_cargo = input("Escolha a opção (1/2/3): ")
    cargos = {"1": "Advogado", "2": "Juiz", "3": "Estagiario"}
    cargo = cargos.get(opcao_cargo, "Estagiario") # Default para estagiário se digitar errado
    
    usuario_logado = Usuario(nome, cargo)
    processo_atual = None
    
    limpar_tela()
    print(f"Bem-vindo(a), {usuario_logado.nome} ({usuario_logado.papel}).")

    # 2. O Menu Interativo
    while True:
        print("\n================ MENU PRINCIPAL ================")
        if processo_atual:
            print(f"Processo Ativo: {processo_atual.numero} | Fase: {processo_atual.estado_atual.__class__.__name__}")
        else:
            print("Processo Ativo: Nenhum")
        print("================================================")
        print("[ 1 ] Criar Novo Processo")
        print("[ 2 ] Carregar Processo Salvo (JSON)")
        print("[ 3 ] Anexar Documento")
        print("[ 4 ] Avançar Fase do Processo")
        print("[ 5 ] Ver Histórico de Auditoria")
        print("[ 6 ] Salvar Processo (JSON)")
        print("[ 7 ] Trocar de Usuário (Logout)")
        print("[ 0 ] Sair do Sistema")
        print("================================================")
        
        opcao = input("Escolha uma ação: ")
        
        try:
            if opcao == "1":
                numero = input("Digite o número do novo processo: ")
                processo_atual = ProcessoJuridico(numero)
                print(f"Processo {numero} autuado com sucesso!")

            elif opcao == "2":
                numero = input("Digite o número do processo que deseja carregar: ")
                processo_atual = ProcessoJuridico.carregar_dados(numero)

            elif opcao == "3":
                if not processo_atual:
                    print("Erro: Nenhum processo selecionado. Crie ou carregue um processo primeiro.")
                    continue
                nome_doc = input("Digite o nome ou tipo do documento (ex: Petição Inicial): ")
                processo_atual.anexar_documento(usuario_logado, nome_doc)
                print(f"Documento '{nome_doc}' enviado com sucesso!")

            elif opcao == "4":
                if not processo_atual:
                    print("Erro: Nenhum processo selecionado.")
                    continue
                processo_atual.avancar_fase(usuario_logado)
                print("Fase avançada com sucesso!")

            elif opcao == "5":
                if not processo_atual:
                    print("Erro: Nenhum processo selecionado.")
                    continue
                processo_atual.exibir_auditoria()

            elif opcao == "6":
                if not processo_atual:
                    print("Erro: Nenhum processo selecionado.")
                    continue
                processo_atual.salvar_dados()

            elif opcao == "7":
                print("\nDeslogando...\n")
                return iniciar_sistema() # Reinicia a função para cadastrar outro usuário

            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                sys.exit()

            else:
                print("Opção inválida. Tente novamente.")

        # Aqui pegamos os bloqueios do nosso Padrão State e exibimos amigavelmente
        except (PermissionError, ValueError) as e:
            print(f"\nAÇÃO BLOQUEADA: {e}")
        except FileNotFoundError as e:
            print(f"\nARQUIVO NÃO ENCONTRADO: {e}")
        except Exception as e:
            print(f"\nERRO INESPERADO: {e}")

if __name__ == "__main__":
    iniciar_sistema()