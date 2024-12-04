from database import Database

class Query:
    def __init__(self, database):
        self.db = database
        

    def create_relacionamento_protagonist_game(self, protagonist, game):
        query = """
        MATCH (protagonist:Protagonist {nome: $nomeProtagonista}), (game:Game {nome: $nomeGame})
        MERGE (protagonist)-[:PROTAGONISTA_DE]->(game)
        """
        parameters = {"nomeProtagonista": protagonist.nome, "nomeGame": game.nome}
        return self.db.execute_query(query, parameters)
    
    def create_relacionamento_secondary_character_game(self, secondary_character, game):
        query = """
        MATCH (secondary_character:SecondaryCharacter {nome: $secondary_character_nome}), (game:Game {nome: $game_nome})
        MERGE (secondary_character)-[:SECUNDARIO_DE]->(game)
        """
        parameters = {"secondary_character_nome": secondary_character.nome, "game_nome": game.nome}
        return self.db.execute_query(query, parameters)
    
    def get_all_games(self):
        query = """
        MATCH (game:Game)
        RETURN game
        """
        return self.db.execute_query(query)
    
    def get_all_protagonists(self):
        query = """
        MATCH (protagonist:Protagonist)
        RETURN protagonist
        """
        return self.db.execute_query(query)
    
    def get_all_secondary_characters(self):
        query = """
        MATCH (secondary_character:SecondaryCharacter)
        RETURN secondary_character
        """
        return self.db.execute_query(query)
    
    def get_game_protagonists(self, game):
        query = """
        MATCH (game:Game {nome: $game})<-[:PROTAGONISTA_DE]-(protagonist:Protagonist)
        RETURN protagonist
        """
        return self.db.execute_query(query, game)
    
    def get_game_secondary_characters(self, game):
        query = """
        MATCH (game:Game {nome: $game})<-[:SECUNDARIO_DE]-(secondary_character:SecondaryCharacter)
        RETURN secondary_character
        """
        return self.db.execute_query(query, game)
    
    def get_protagonist_games(self, protagonist):
        query = """
        MATCH (protagonist:Protagonist {nome: $protagonist})-[:PROTAGONISTA_DE]->(game:Game)
        RETURN game
        """
        return self.db.execute_query(query, protagonist)
    
    def get_secondary_character_games(self, secondary_character):
        query = """
        MATCH (secondary_character:SecondaryCharacter {nome: $secondary_character})-[:SECUNDARIO_DE]->(game:Game)
        RETURN game
        """
        return self.db.execute_query(query, secondary_character)
    
    def game_that_starts_with(self, letter):
        query = """
        MATCH (game:Game)
        WHERE game.nome STARTS WITH $letter
        RETURN game
        """
        return self.db.execute_query(query, letter)
    
    def get_game_by_genre(self, genre):
        query = """
        MATCH (game:Game {genero: $genero})
        RETURN game
        """
        return self.db.execute_query(query, genre)