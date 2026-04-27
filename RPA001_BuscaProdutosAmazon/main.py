from src.logger import setup_logger
import logging

from src.send_email import salvar_e_enviar
from src.navegation import buscar_produtos_amazon

logger = logging.getLogger(__name__)

setup_logger()

if __name__ == "__main__":
    logger.info(f"Solicitando o nome do produto para a busca ao usuário.")
    produto = input("Digite o produto que deseja buscar: ")
    logger.info(f"Produto informado: {produto}")
    logger.info(f"Solicitando o tipo de execução ao usuário.")
    modo = input("Executar em modo (1) Visual ou (2) Background? ")
    logger.info(f"Tipo de execução selecionada: {modo}")
    
    print(f"Iniciando robô para buscar '{produto}'...")
    logger.info(f"Iniciando robô para buscar '{produto}'...")
    lista_produtos = buscar_produtos_amazon(produto, visual=(modo == "1"))
    
    if lista_produtos:
        salvar_e_enviar(lista_produtos, produto)
    else:
        print("Nenhum dado foi coletado.")
        logger.info(f"Nenhum dado foi coletado.")