from database import Database

class GameCRUD:
    def __init__(self, database):
        self.db = database
    
    def create_game(self, game):
        query = """
        CREATE (game:Game {nome: $nome, genero: $genero})
        RETURN game
        """
        parameters = {"nome": game.nome, "genero": game.genero}
        return self.db.execute_query(query, parameters)
    
    def read_game(self, game):
        query = """
        MATCH (game:Game {nome: $nome})
        RETURN game
        """
        return self.db.execute_query(query, parameters={"nome": game.nome})
    
    def update_game(self, game):
        query = """
        MATCH (game:Game {nome: $nome})
        SET game.genero = $genero
        RETURN game
        """
        return self.db.execute_query(query, parameters={"nome": game.nome, "genero": game.genero})
    
    def delete_game(self, game):
        query = """
        MATCH (game:Game {nome: $nome})
        DETACH DELETE game
        """
        return self.db.execute_query(query, game)