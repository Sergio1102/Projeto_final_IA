import streamlit as st
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from arquivos.estado import EstadoAula
from arquivos.agentes import agente_tecnico, agente_pedagogico, agente_revisor_final

st.set_page_config(page_title="Gerador de Aulas de Robótica", page_icon="🤖", layout="centered")
st.title("🤖 Gerador de Aulas de Robótica")
st.write("Crie planos de aula práticos com o apoio de uma equipe de agentes de IA.")

@st.cache_resource
def carregar_sistema():
    fluxo = StateGraph(EstadoAula)
    fluxo.add_node("tecnico", agente_tecnico)
    fluxo.add_node("pedagogico", agente_pedagogico)
    fluxo.add_node("revisor", agente_revisor_final)
    
    fluxo.add_edge(START, "tecnico")
    fluxo.add_edge("tecnico", "pedagogico")
    fluxo.add_edge("pedagogico", "revisor")
    fluxo.add_edge("revisor", END)
    
    memoria = MemorySaver()
    return fluxo.compile(checkpointer=memoria, interrupt_before=["revisor"])

sistema = carregar_sistema()

configuracao = {"configurable": {"thread_id": "sessao_web_01"}}

if "etapa" not in st.session_state:
    st.session_state.etapa = "inicio"

if st.session_state.etapa == "inicio":
    tema = st.text_input("Qual o tema da atividade prática?", placeholder="Ex: Semáforo com Arduino...")
    
    if st.button("Gerar Proposta de Aula", type="primary"):
        if tema:
            with st.spinner("Os agentes estão pesquisando e planejando..."):
                for evento in sistema.stream({"tema_aula": tema}, configuracao):
                    pass 
            st.session_state.etapa = "revisao"
            st.rerun()
        else:
            st.warning("Por favor, digite um tema.")

elif st.session_state.etapa == "revisao":
    estado_atual = sistema.get_state(configuracao)
    esboco = estado_atual.values.get("esboco_aula", "")
    
    st.info("⏸️ O sistema pausou. Revise o esboço pedagógico gerado abaixo.")
    
    st.markdown("### 📄 Esboço da Aula")
    st.markdown(esboco) 
    
    st.divider()
    
    st.markdown("### 👨‍🏫 Sua Avaliação")
    feedback = st.text_area("O que precisa ser alterado para a versão final?", placeholder="Ex: Diminua o tempo da abertura, troque o componente X por Y...")
    
    if st.button("Aprovar e Finalizar Aula", type="primary"):
        with st.spinner("Aplicando seu feedback e gerando o guia final..."):
            sistema.update_state(configuracao, {"feedback_professor": feedback})
            for evento in sistema.stream(None, configuracao):
                pass
        st.session_state.etapa = "finalizado"
        st.rerun()

elif st.session_state.etapa == "finalizado":
    estado_final = sistema.get_state(configuracao)
    guia = estado_final.values.get("guia_final", "")
    
    st.success("✅ Guia de Aula Finalizado com Sucesso!")
    
    st.markdown(guia)
    
    st.divider()
    
    if st.button("Criar Nova Aula"):
        st.session_state.etapa = "inicio"
        import uuid
        configuracao["configurable"]["thread_id"] = str(uuid.uuid4())
        st.rerun()