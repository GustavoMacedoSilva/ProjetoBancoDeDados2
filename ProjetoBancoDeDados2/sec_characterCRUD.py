from database import Database

class CharacterCRUD:
    def __init__(self, database):
        self.db = database
    
    def create_character(self, sec_character):
        query = """
        CREATE (secondary_character:SecondaryCharacter {nome: $nome, sexo: $sexo})
        RETURN secondary_character
        """
        parameters = {"nome": sec_character.nome, "sexo": sec_character.sexo}
        return self.db.execute_query(query, parameters)
    
    def read_character(self, sec_character):
        query = """
        MATCH (secondary_character:SecondaryCharacter {nome: $nome})
        RETURN secondary_character
        """
        return self.db.execute_query(query, parameters={"nome": sec_character.nome})
    
    def update_character(self, sec_character, sexo):
        query = """
        MATCH (secondary_character:SecondaryCharacter {nome: $nome})
        SET secondary_character.sexo = $sexo
        RETURN secondary_character
        """
        return self.db.execute_query(query, parameters={"nome": sec_character.nome, "sexo": sexo})
    
    def delete_character(self, sec_character):
        query = """
        MATCH (secondary_character:SecondaryCharacter {nome: $nome})
        DETACH DELETE secondary_character
        """
        return self.db.execute_query(query, parameters={"nome": sec_character.nome})