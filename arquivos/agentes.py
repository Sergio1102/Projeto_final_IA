import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from arquivos.estado import EstadoAula

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

def agente_tecnico(state: EstadoAula):
    print("🔧 [Técnico]: Analisando viabilidade e projetando o hardware...")
    
    prompt = f"""Você é um técnico de laboratório especialista em robótica educacional.
    O tema da aula é: {state['tema_aula']}.
    Crie uma proposta de atividade prática "mão na massa" utilizando componentes acessíveis (ex: Arduino, sensores básicos, materiais recicláveis).
    Liste os materiais necessários e o passo a passo da montagem em no máximo 3 parágrafos."""
    
    resposta = llm.invoke(prompt)
    return {"sugestao_pratica": resposta.content}

def agente_pedagogico(state: EstadoAula):
    print("📚 [Pedagógico]: Estruturando a dinâmica da aula...")
    
    prompt = f"""Você é um designer instrucional com foco em ensino médio profissionalizante.
    Baseado nesta atividade prática: {state['sugestao_pratica']}, 
    Crie um esboço de aula dinâmica contendo:
    1. Abertura e Contextualização (Problematização)
    2. Tempo estimado para a atividade prática.
    3. Fechamento e consolidação do conhecimento.
    Seja claro, engajador e direto."""
    
    resposta = llm.invoke(prompt)
    return {"esboco_aula": resposta.content}

def agente_revisor_final(state: EstadoAula):
    print("✨ [Revisor]: Consolidando o guia final com as diretrizes do professor...")
    
    feedback = state.get("feedback_professor", "Nenhuma alteração solicitada.")
    
    prompt = f"""Você é o coordenador final do projeto.
    Aqui está a proposta original da aula: {state['esboco_aula']}
    Aqui está o feedback/exigência do professor que deve ser aplicado obrigatoriamente: {feedback}
    
    Reescreva o guia da aula incorporando o feedback do professor. 
    Apresente um formato final polido, pronto para ser impresso ou entregue aos alunos."""
    
    resposta = llm.invoke(prompt)
    return {"guia_final": resposta.content}