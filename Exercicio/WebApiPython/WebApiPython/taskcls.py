class taskcls:
    def __init__(self,id,nome,data,utilizador):
        self.Id = id
        self.Nome = nome
        self.Data = data
        self.Utilizador = utilizador

    def toDictionary(self):
        return {
                "id":self.Id,
                "nome":self.Nome,
                "data":self.Data,
                "utilizador":self.Utilizador
            }