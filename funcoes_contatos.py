from persistencia import salvar_contato
from validacao import validar_campo,validar_telefone,validar_email

def adicionar_contatos(contatos):
    nome = validar_campo("Qual é seu nome?: ").title()
    telefone =validar_telefone("qual é seu telefone?: ")
    email =validar_email("qual é seu email?: ")
    contato= {
        "nome":nome,
        "telefone": telefone,
        "email": email
        }
    contatos.append(contato)
    salvar_contato(contatos)
    print("\n Contato adicionado com sucesso! \n")
    
    
def listar_contatos(contatos):
    print("===Lista de contatos===")
    for contato in contatos:
        print(f"nome: {contato["nome"]}")
        print(f"telefone: {contato["telefone"]}")
        print(f"e-mail: {contato["email"]}")
        print()
        
        
def buscar_contatos(contatos):
        busca = validar_campo("qual nome deseja buscar?").title()
        
         # Controla se algum contato foi encontrado na busca
        encontrado = False

        for contato in contatos:
            if contato ["nome"] == busca:
                print(f"nome: {contato["nome"]}")
                print(f"telefone: {contato["telefone"]}")
                print(f"e-mail: {contato["email"]}")
                encontrado = True
                
        if not encontrado:
            print("usuario não encontrado")
 
                
def editar_contatos(contatos):
    edita = validar_campo("qual nome deseja buscar? ").title()
    encontrado = False

# Procura o contato pelo nome para alterar os dados
    for contato in contatos:
        if contato ["nome"] == edita:
            
            novo_telefone= validar_telefone("qual será o novo numero de telefone? ")
            contato["telefone"] = novo_telefone
            print ("telefone alterado!")
            
            
            novo_email= validar_email("qual será o novo email? ")
            contato["email"] = novo_email
            salvar_contato(contatos)
            print("email alterado!")
            encontrado = True
            
    if not encontrado:
        print("usuario nao encontrado")
        
        
def excluir_contatos(contatos):
    excluir = validar_campo("qual contato deseja excluir?").title()
    encontrado = False

    for contato  in contatos:
        if contato ["nome"] == excluir:
            contatos.remove(contato)
            salvar_contato(contatos)
            print("contato excluido")  
            encontrado = True
    if not encontrado:
        print("Usuario não encontrado")
                               