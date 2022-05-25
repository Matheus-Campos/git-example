import db

def procurarEstudante(id, name):
  estudante = db.findById(id, name)
  estudante["nota"] = 10
  return estudante

def deletarEstudante(id, name):
  db.deleteByIdAndName(id, name)
  return "Estudante deletado com sucesso"