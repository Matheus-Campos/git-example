dados = [{"id": 0, "nome": "Giovanni"}, {"id": 1, "nome": "Matheus"}]

def findById(registerId, name):
  registro = [dado for dado in dados if (dado["id"] == registerId and dado["nome"] == name)]
  return registro[0]

def deleteByIdAndName(registerId):
  global dados
  dados = [dado for dado in dados if (dado["id"] != registerId)]