from database import Database

class ProtagonistCRUD:
    def __init__(self, database):
        self.db = database
    
    def create_protagonist(self, protagonist):
        query = """
        CREATE (protagonist:Protagonist {nome: $nome, genero: $genero})
        RETURN protagonist
        """
        parameters = {"nome": protagonist.nome, "genero": protagonist.sexo}
        return self.db.execute_query(query, parameters)
    
    def read_protagonist(self, protagonista):
        query = """
        MATCH (protagonist:Protagonist {nome: $nome})
        RETURN protagonist
        """
        parameters = {"nome": protagonista.nome}
        return self.db.execute_query(query, parameters)
    
    def update_protagonist(self, protagonist, sexo):
        query = """
        MATCH (protagonist:Protagonist {nome: $nome})
        SET protagonist.sexo = {sexo: $sexo}
        RETURN protagonist
        """
        return self.db.execute_query(query, parameters={"nome": protagonist.nome, "sexo": sexo})
    
    def delete_protagonist(self, protagonist):
        query = """
        MATCH (protagonist:Protagonist {nome: $nome})
        DETACH DELETE protagonist
        """
        return self.db.execute_query(query, parameters={"nome": protagonist.nome})