import controller

comando = int(input("Digite uma operação: 1 para procurar e 2 para deletar"))

if comando == 1:
  idEstudante = int(input("digite o id do estudante a ser procurado: "))
  estudante = controller.procurarEstudante(idEstudante)
  print(estudante)
elif comando == 2:
  idEstudante = int(input("digite o id do estudante a ser deletado: "))
  mensagem = controller.deletarEstudante(idEstudante)
  print(mensagem)