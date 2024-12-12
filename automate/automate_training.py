import os
import requests
import shutil
import time

# Definir o caminho para o diretório do projeto Rasa
project_path = "C:/Users/Project/Desktop/lhama"

# Função para verificar logs de fallback
def verificar_fallbacks(log_path):
    """
    Verifica logs de fallback para identificar frases que a IA não entendeu.
    """
    # Abra o arquivo de logs ou acesse o banco de dados para coletar falhas
    falhas = []
    with open(log_path, "r") as log_file:
        for line in log_file:
            if "utter_fallback" in line:
                # Coletar a frase que gerou o fallback
                falha = line.split("texto_usuario:")[1]
                falhas.append(falha.strip())
    return falhas

# Função para adicionar exemplos ao NLU e Stories
def atualizar_dados(falhas, nlu_file, stories_file):
    """
    Atualiza os arquivos NLU e Stories com novos exemplos.
    """
    with open(nlu_file, "a") as nlu, open(stories_file, "a") as stories:
        for falha in falhas:
            # Adicionar exemplo de fallback corrigido ao NLU
            nlu.write(f"\n- intent: novo_intento\n  examples: |\n    - {falha}")
            # Criar uma nova história com base no exemplo de fallback
            stories.write(f"\n- story: novo_caminho\n  steps:\n  - intent: novo_intento\n  - action: utter_nova_resposta")

# Função para treinar o modelo
def treinar_modelo():
    """
    Roda o comando para treinar o modelo.
    """
    os.chdir(project_path)
    os.system("rasa train")

# Função para fazer o deploy do novo modelo
def fazer_deploy():
    """
    Copia o novo modelo treinado para o diretório de produção.
    """
    model_source = os.path.join(project_path, "models", "modelo_novo.tar.gz")
    deploy_path = "C:/Users/Project/Desktop/lhama/models"
    
    if os.path.exists(model_source):
        shutil.copy(model_source, deploy_path)
        print("Novo modelo implantado com sucesso!")

    else:
        print("Modelo não encontrado. Verifique se o treinamento foi concluído com sucesso.")


# Automação completa
def automacao_treinamento():
    # Etapa 1: Verificar logs para coletar novas falhas
    log_path = os.path.join(project_path, "logs", "rasa_logs.log")
    falhas = verificar_fallbacks(log_path)
    
    if falhas:
        # Etapa 2: Atualizar os dados de treinamento
        nlu_file = os.path.join(project_path, "data", "nlu.yml")
        stories_file = os.path.join(project_path, "data", "stories.yml")
        atualizar_dados(falhas, nlu_file, stories_file)
        
        # Etapa 3: Treinar o modelo
        treinar_modelo()
        
        # Etapa 4: Fazer o deploy do novo modelo
        fazer_deploy()

if __name__ == "__main__":
    # Rodar a automação uma vez ou configurar para rodar periodicamente
    while True:
        automacao_treinamento()
        # Aguardar um tempo antes de rodar novamente (exemplo: a cada 5 minutos)
        time.sleep(600)