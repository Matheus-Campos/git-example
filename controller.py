import db

def procurarEstudante(id):
  estudante = db.findById(id)
  estudante["nota"] = 10
  return estudante

def deletarEstudante(id, name):
  db.deleteByIdAndName(id, name)
  return "Estudante deletado com sucesso"