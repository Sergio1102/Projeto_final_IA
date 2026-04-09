from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from estado import EstadoAula
from agentes import agente_tecnico, agente_pedagogico, agente_revisor_final

fluxo = StateGraph(EstadoAula)

fluxo.add_node("tecnico", agente_tecnico)
fluxo.add_node("pedagogico", agente_pedagogico)
fluxo.add_node("revisor", agente_revisor_final)

fluxo.add_edge(START, "tecnico")
fluxo.add_edge("tecnico", "pedagogico")
fluxo.add_edge("pedagogico", "revisor")
fluxo.add_edge("revisor", END)

memoria = MemorySaver()
sistema = fluxo.compile(checkpointer=memoria, interrupt_before=["revisor"])

def executar_sistema():
    configuracao = {"configurable": {"thread_id": "projeto_apresentacao_01"}}
    tema = input("Digite o tema da aula de robótica: ")

    print("\n--- INICIANDO GERAÇÃO DA AULA ---")
    eventos = sistema.stream({"tema_aula": tema}, configuracao)

    for evento in eventos:
        print(f"✅ Nó concluído: {list(evento.keys())[0]}")

    estado_atual = sistema.get_state(configuracao)
    print("\n" + "="*40)
    print("⏸️ SISTEMA PAUSADO PARA REVISÃO HUMANA")
    print("="*40)
    
    esboco = estado_atual.values.get("esboco_aula", "Nenhum esboço gerado.")
    print("\n📄 ESBOÇO GERADO PELO AGENTE PEDAGÓGICO:\n")
    print(esboco)
    print("-" * 40)
    
    feedback = input("\n👨‍🏫 Avalie o esboço acima. Digite suas alterações (ou 'ok' para aprovar como está): ")

    sistema.update_state(configuracao, {"feedback_professor": feedback})
    
    print("\n▶️ RETOMANDO EXECUÇÃO E GERANDO GUIA FINAL...")
    eventos_finais = sistema.stream(None, configuracao)
    
    for evento in eventos_finais:
        pass

    estado_final = sistema.get_state(configuracao)
    print("\n" + "="*40)
    print("✅ GUIA DE AULA FINALIZADO")
    print("="*40 + "\n")
    print(estado_final.values.get("guia_final"))

if __name__ == "__main__":
    executar_sistema()