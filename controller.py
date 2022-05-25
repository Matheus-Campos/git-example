import db

def procurarEstudante(id):
  estudante = db.findById(id)
  estudante["nota"] = 10
  return estudante

def deletarEstudante(id):
  db.deleteById(id)
  return "Estudante deletado com sucesso"