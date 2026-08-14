def validar_campo(mensagem):
    campo = input(mensagem).strip()
    
    while campo =="":
        print("este campo não pode ficar vazio.")
        campo = input(mensagem).strip()
        
    return campo

def validar_telefone(mensagem):
    telefone = input(mensagem).strip()
    
    while telefone == "" or not telefone.isdigit():
        print("telefone invalido. Digite apenas números")
        telefone = input(mensagem).strip()
        
    return telefone

def validar_email(mensagem):
    email = input(mensagem).strip().lower()
    
    while email == "" or "@" not in email or "." not in email.split("@")[-1]:
        print("E-mail invalido")
        email = input(mensagem).strip().lower()
        
    return email

def validar_opcao(mensagem):
    opcao = input(mensagem).strip()
    
    while opcao not in ["1","2","3","4","5","6"]:
        print("opção invalida. tente novamente")
        opcao = input(mensagem).strip()
        
    return opcao
        