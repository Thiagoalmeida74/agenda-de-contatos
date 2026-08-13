import json

def salvar_contato(contatos):
    # Salva a lista atual de contatos no arquivo JSON
    with open("contatos.json", "w") as arquivo:
        json.dump(contatos,arquivo)
        
def carregar_contatos():
     # Carrega os contatos salvos quando o programa inicia
    with open("contatos.json", "r") as arquivo:
        contatos = json.load(arquivo)
            
        return contatos