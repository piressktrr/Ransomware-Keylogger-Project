from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
        ## abre o arquivo em modo binario, armazena os dados
    dados_descriptografados = f.decrypt(dados_encriptados)
    ## cria uma variavel que descriptografa os dados usando a chave fornecida e depois os retorna
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
        ## abre o arquivo em modo de escrita binaria e o substituti pelos dados descriptografados

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("testfiles")
    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    print("Arquivos descriptografados com sucesso!")

if __name__ == "__main__":
    main()