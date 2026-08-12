contatos = []

def mostrar_menu():
    print ("=== Agenda de contatos ===")
    print ("1 - adicionar contato")
    print ("2 - Listar contato")
    print ("3 - Buscar contato")
    print ("4 - Editar contato")
    print ("5 - Excluir contato")
    print ("6 - Sair")
    opcao= input("escolha uma opcao: ")
    return opcao

def adicionar_contato():
    nome = input("Qual é seu nome?: ")
    telefone =input("qual é seu telefone?: ")
    email =input("qual é seu email?: ")
    contato= {
        "nome":nome,
        "telefone": telefone,
        "email": email
        }
    contatos.append(contato)
    print("\n Contato adicionado com sucesso! \n")
    
def listar_contatos():
    print("===Lista de contatos===")
    for contato in contatos:
        print(f"nome: {contato["nome"]}")
        print(f"telefone: {contato["telefone"]}")
        print(f"e-mail: {contato["email"]}")
        print()

def buscar_contato():
        busca = input("qual nome deseja buscar?")
        
        encontrado = False

        for contato in contatos:
            if contato ["nome"] == busca:
                print(f"nome: {contato["nome"]}")
                print(f"telefone: {contato["telefone"]}")
                print(f"e-mail: {contato["email"]}")
                encontrado = True
                
        if encontrado == False:
            print("usuario não encontrado")
                
def editar_contato():
    edita = input("qual nome deseja buscar? ")
    encontrado = False

    for contato in contatos:
        if contato ["nome"] == edita:
            
            novo_telefone= input("qual será o novo numero de telefone? ")
            contato["telefone"] = novo_telefone
            print ("telefone alterado!")
            
            
            novo_email= input("qual será o novo email? ")
            contato["email"] = novo_email
            print("email alterado!")
            encontrado = True
            
    if encontrado == False:
        print("usuario nao encontrado")

            
            

def main():
    opcao = mostrar_menu()
    while opcao != "6":
        if opcao == "1":
            adicionar_contato()
        
        elif opcao == "2":
            listar_contatos()
       
        elif opcao == "3":
            buscar_contato()
            
        elif opcao == "4":
            editar_contato()
        
        
            
              
            
        opcao = mostrar_menu()
    print("até logo!")
        
main()
