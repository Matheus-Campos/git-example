dados = [{"id": 0, "nome": "Giovanni"}, {"id": 1, "nome": "Matheus"}]

def findById(registerId):
  registro = [dado for dado in dados if dado["id"] == registerId]
  return registro[0]

def deleteByIdAndName(registerId, name):
  global dados
  dados = [dado for dado in dados if (dado["id"] != registerId and dado["nome"] != name)]