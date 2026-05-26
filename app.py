# app.py
import streamlit as st
from usuario import Usuario
from processo import ProcessoJuridico

# 1. Configuração da Página
st.set_page_config(page_title="Sistema Jurídico", page_icon="⚖️", layout="centered")

# 2. Gerenciamento de Estado (Memória do site)
if 'processo' not in st.session_state:
    st.session_state.processo = None
if 'usuario' not in st.session_state:
    st.session_state.usuario = Usuario("Visitante", "Estagiario") # Usuário padrão

# 3. Barra Lateral (Sidebar) para Login
with st.sidebar:
    st.header("👤 Login do Sistema")
    nome = st.text_input("Seu Nome:")
    cargo = st.selectbox("Seu Cargo:", ["Estagiario", "Advogado", "Juiz"])
    
    if st.button("Entrar"):
        st.session_state.usuario = Usuario(nome, cargo)
        st.success(f"Logado como {nome} ({cargo})")

# 4. Tela Principal
st.title("⚖️ Gestão de Processos Jurídicos")
st.write(f"**Usuário logado:** {st.session_state.usuario.nome} | **Cargo:** {st.session_state.usuario.papel}")
st.divider()

# 5. Controles do Processo
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Abertura")
    novo_numero = st.text_input("Número do Novo Processo:")
    if st.button("Autuar Processo"):
        if novo_numero:
            st.session_state.processo = ProcessoJuridico(novo_numero)
            st.success(f"Processo {novo_numero} autuado!")
        else:
            st.warning("Digite um número para o processo.")

with col2:
    st.subheader("💾 Persistência")
    num_carregar = st.text_input("Número para Carregar (JSON):")
    if st.button("Carregar do Disco"):
        try:
            st.session_state.processo = ProcessoJuridico.carregar_dados(num_carregar)
            st.success("Processo carregado com sucesso!")
        except Exception as e:
            st.error(e)

st.divider()

# 6. Interagindo com o Processo Ativo
if st.session_state.processo:
    st.subheader(f"📌 Processo Ativo: {st.session_state.processo.numero}")
    st.info(f"Fase Atual: **{st.session_state.processo.estado_atual.__class__.__name__}**")
    
    col_acao1, col_acao2 = st.columns(2)
    
    with col_acao1:
        doc_nome = st.text_input("Nome do Documento:")
        if st.button("📎 Anexar Documento"):
            try:
                st.session_state.processo.anexar_documento(st.session_state.usuario, doc_nome)
                st.success(f"'{doc_nome}' anexado com sucesso!")
            except Exception as e:
                st.error(f"🚫 BLOQUEADO: {e}")

    with col_acao2:
        st.write("") # Espaço para alinhar os botões
        st.write("")
        if st.button("➡️ Avançar Fase do Processo", use_container_width=True):
            try:
                st.session_state.processo.avancar_fase(st.session_state.usuario)
                st.success("Fase avançada com sucesso!")
                # Força a tela a recarregar para atualizar a fase visualmente
                st.rerun() 
            except Exception as e:
                st.error(f"🚫 BLOQUEADO: {e}")

    # Exibindo o Histórico (Auditoria)
    st.divider()
    st.subheader("📜 Histórico de Auditoria")
    for linha in st.session_state.processo.historico:
        st.code(linha)
        
    if st.button("Salvar Processo no Disco (JSON)"):
        st.session_state.processo.salvar_dados()
        st.success("Processo salvo no arquivo JSON!")
else:
    st.warning("Nenhum processo ativo. Crie ou carregue um processo para começar.")