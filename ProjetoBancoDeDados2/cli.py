from game import Game
from protagonist import Protagonist
from sec_character import Secondary_Character
class SimpleCLI:
    def __init__(self):
        self.commands = {}
        
    def add_command(self, name, function):
        self.commands[name] = function
        
    def run(self):
        while True:
            command = input("Escreva um comando: ")
            if command == "sair":
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido")
                
class GameCLI(SimpleCLI):
    def __init__(self, game_crud):
        super().__init__()
        self.game_crud = game_crud
        self.add_command("criar", self.create_game)
        self.add_command("ler", self.read_game)
        self.add_command("atualizar", self.update_game)
        self.add_command("deletar", self.delete_game)
        
    def create_game(self):
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo: ")
        game = Game(nome, genero)
        self.game_crud.create_game(game)
        
    def read_game(self):
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo: ")
        game = Game(nome, genero)
        self.game_crud.read_game(game)
        
    def update_game(self):
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo: ")
        game = Game(nome, genero)
        self.game_crud.update_game(game)
        
    def delete_game(self):
        nome = input("Nome do jogo: ")
        genero = input("Gênero do jogo: ")
        game = Game(nome, genero)
        self.game_crud.delete_game(game)
        
    def run(self):
        print("Bem-vindo ao CLI de jogos")
        print("Digite 'criar' para criar um jogo")
        print("Digite 'ler' para ler um jogo")
        print("Digite 'atualizar' para atualizar um jogo")
        print("Digite 'deletar' para deletar um jogo")
        print("Digite 'sair' para sair")
        super().run()
        
class ProtagonistCLI(SimpleCLI):
    def __init__(self, protagonist_crud):
        super().__init__()
        self.protagonist_crud = protagonist_crud
        self.add_command("criar", self.create_protagonist)
        self.add_command("ler", self.read_protagonist)
        self.add_command("atualizar", self.update_protagonist)
        self.add_command("deletar", self.delete_protagonist)
        
    def create_protagonist(self):
        nome = input("Nome do protagonista: ")
        genero = input("Gênero do protagonista: ")
        protagonist = Protagonist(nome, genero)
        self.protagonist_crud.create_protagonist(protagonist)
        
    def read_protagonist(self):
        nome = input("Nome do protagonista: ")
        sexo = input("Gênero do protagonista: ")
        protagonist = Protagonist(nome, sexo)
        print(self.protagonist_crud.read_protagonist(protagonist))
        
        
    def update_protagonist(self):
        nome = input("Nome do protagonista: ")
        genero = input("Gênero do protagonista: ")
        protagonist = Protagonist(nome, genero)
        self.protagonist_crud.update_protagonist(protagonist)
        
    def delete_protagonist(self):
        nome = input("Nome do protagonista: ")
        sexo = input("Gênero do protagonista: ")
        protagonist = Protagonist(nome, sexo)
        self.protagonist_crud.delete_protagonist(protagonist)
        
    def run(self):
        print("Bem-vindo ao CLI de protagonistas")
        print("Digite 'criar' para criar um protagonista")
        print("Digite 'ler' para ler um protagonista")
        print("Digite 'atualizar' para atualizar um protagonista")
        print("Digite 'deletar' para deletar um protagonista")
        print("Digite 'sair' para sair")
        super().run()
        
class SecondaryCharacterCLI(SimpleCLI):
    def __init__(self, sec_character_crud):
        super().__init__()
        self.sec_character_crud = sec_character_crud
        self.add_command("criar", self.create_sec_character)
        self.add_command("ler", self.read_sec_character)
        self.add_command("atualizar", self.update_sec_character)
        self.add_command("deletar", self.delete_sec_character)
        
    def create_sec_character(self):
        nome = input("Nome do personagem secundário: ")
        genero = input("Gênero do personagem secundário: ")
        sec_character = Secondary_Character(nome, genero)
        self.sec_character_crud.create_character(sec_character)
        
    def read_sec_character(self):
        nome = input("Nome do personagem secundário: ")
        sexo = input("Gênero do personagem secundário: ")
        sec_character = Secondary_Character(nome, sexo)
        self.sec_character_crud.read_character(sec_character)
        
    def update_sec_character(self):
        nome = input("Nome do personagem secundário: ")
        genero = input("Gênero do personagem secundário: ")
        sec_character = Secondary_Character(nome, genero)
        self.sec_character_crud.update_character(sec_character)
        
    def delete_sec_character(self):
        nome = input("Nome do personagem secundário: ")
        sexo = input("Gênero do personagem secundário: ")
        sec_character = Secondary_Character(nome, sexo)
        self.sec_character_crud.delete_character(sec_character)
        
    def run(self):
        print("Bem-vindo ao CLI de personagens secundários")
        print("Digite 'criar' para criar um personagem secundário")
        print("Digite 'ler' para ler um personagem secundário")
        print("Digite 'atualizar' para atualizar um personagem secundário")
        print("Digite 'deletar' para deletar um personagem secundário")
        print("Digite 'sair' para sair")
        super().run()