# fases.py

from abc import ABC, abstractmethod
from usuario import Usuario

# ==========================================
# 1. A INTERFACE DO ESTADO
# ==========================================
class FaseDoProcesso(ABC):
    @abstractmethod
    def anexar_documento(self, processo, usuario: Usuario, documento: str):
        pass

    @abstractmethod
    def avancar_fase(self, processo, usuario: Usuario):
        pass

# ==========================================
# 2. OS ESTADOS CONCRETOS (Fases Reais)
# ==========================================
class FaseAberto(FaseDoProcesso):
    def anexar_documento(self, processo, usuario: Usuario, documento: str):
        # Controle de Acesso
        if usuario.papel not in ['Advogado', 'Juiz']:
            raise PermissionError("Apenas Advogados ou Juízes podem anexar documentos na fase inicial.")
        
        processo.documentos.append(documento)
        processo.registrar_historico(f"Anexo adicionado: '{documento}' por {usuario}")

    def avancar_fase(self, processo, usuario: Usuario):
        # Controle de Acesso
        if usuario.papel != 'Juiz':
            raise PermissionError("Apenas um Juiz pode iniciar o julgamento do processo.")
        
        # Guardião de Transição: Precisa ter documento para virar réu/ir a julgamento
        if len(processo.documentos) == 0:
            raise ValueError("Guardião bloqueou: O processo precisa de pelo menos uma petição para ir a julgamento.")

        processo.estado_atual = FaseEmJulgamento()
        processo.registrar_historico(f"Fase alterada para 'Em Julgamento' pelo {usuario}")


class FaseEmJulgamento(FaseDoProcesso):
    def anexar_documento(self, processo, usuario: Usuario, documento: str):
        raise ValueError("Bloqueado: Não é possível anexar documentos durante a fase de julgamento.")

    def avancar_fase(self, processo, usuario: Usuario):
        if usuario.papel != 'Juiz':
            raise PermissionError("Apenas um Juiz pode emitir a sentença e arquivar o processo.")

        processo.estado_atual = FaseArquivado()
        processo.registrar_historico(f"Sentença proferida. Processo 'Arquivado' pelo {usuario}")


class FaseArquivado(FaseDoProcesso):
    def anexar_documento(self, processo, usuario: Usuario, documento: str):
        raise ValueError("Bloqueado: Processo arquivado com trânsito em julgado. Nenhuma alteração permitida.")

    def avancar_fase(self, processo, usuario: Usuario):
        raise ValueError("Bloqueado: O processo já está finalizado e não pode avançar.")