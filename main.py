import json 
from funcoes_contatos import adicionar_contatos, listar_contatos, buscar_contatos, editar_contatos,excluir_contatos 
from persistencia import carregar_contatos

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

def main():# controla o menu e chama as funções
    contatos = carregar_contatos()
    opcao = mostrar_menu()
    while opcao != "6":
        if opcao == "1":
            adicionar_contatos(contatos)
        
        elif opcao == "2":
            listar_contatos(contatos)
       
        elif opcao == "3":
            buscar_contatos(contatos)
            
        elif opcao == "4":
            editar_contatos(contatos)
        
        elif opcao == "5":
            excluir_contatos(contatos)
            
        elif opcao == "6":
            break
            print("ate logo!")
        
        else:
            print("opcao invalida")
          
        opcao = mostrar_menu()
    print("até logo!")
        
main()
