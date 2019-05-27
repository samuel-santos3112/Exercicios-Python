
usuario = input("Informe usuario: ")
senhaUsuario = input("Informe senha: ")

while senhaUsuario == usuario:
    print("Erro - Senha não pode ser igual nome de usuario.\nDigite novamente")
    senhaUsuario = input("Informe senha: ")
print("Usuário: ",usuario,"\nSenha: ",senhaUsuario)