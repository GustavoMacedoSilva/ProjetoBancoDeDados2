from database import Database
from query import Query
from gameCRUD import GameCRUD
from protagonistCRUD import ProtagonistCRUD
from sec_characterCRUD import CharacterCRUD
from game import Game
from protagonist import Protagonist
from sec_character import Secondary_Character
from cli import *


db = Database("bolt://3.92.251.45:7687", "neo4j", "brother-organs-maples")

game_crud = GameCRUD(db)
protagonist_crud = ProtagonistCRUD(db)
character_crud = CharacterCRUD(db)
query = Query(db)
game_cli = GameCLI(game_crud)
protagonist_cli = ProtagonistCLI(protagonist_crud)
sec_character_cli = SecondaryCharacterCLI(character_crud)

protagonist_cli.run()
game_cli.run()
sec_character_cli.run()
#db.drop_all()

# yakuza_0 = Game("Yakuza 0", "Ação")
# yakuza_kiwami = Game("Yakuza Kiwami", "Ação")
# yakuza_kiwami_2 = Game("Yakuza Kiwami 2", "Ação")
# yakuza_3 = Game("Yakuza 3", "Ação")
# yakuza_4 = Game("Yakuza 4", "Ação")
# yakuza_5 = Game("Yakuza 5", "Ação")
# yakuza_6 = Game("Yakuza 6", "Ação")
# yakuza_like_a_dragon = Game("Yakuza: Like a Dragon", "Ação")
# like_a_dragon_infinite_wealth = Game("Like a Dragon: Infinite Wealth", "Ação")
# like_a_dragon_gaiden_the_man_who_erased_his_name = Game("Like a Dragon Gaiden: The Man Who Ereased His Name", "Ação")
# like_a_dragon_ishin = Game("Like a Dragon: Ishin", "Ação")

# game_crud.create_game(yakuza_0)
# game_crud.create_game(yakuza_kiwami)
# game_crud.create_game(yakuza_kiwami_2)
# game_crud.create_game(yakuza_3)
# game_crud.create_game(yakuza_4)
# game_crud.create_game(yakuza_5)
# game_crud.create_game(yakuza_6)
# game_crud.create_game(yakuza_like_a_dragon)
# game_crud.create_game(like_a_dragon_infinite_wealth)
# game_crud.create_game(like_a_dragon_gaiden_the_man_who_erased_his_name)
# game_crud.create_game(like_a_dragon_ishin)


# kiryu_kazuma = Protagonist("Kazuma Kiryu", "Masculino")
# goro_majima = Protagonist("Goro Majima", "Masculino")
# ichiban_kasuga = Protagonist("Ichiban Kasuga", "Masculino")
# tatsuo_shinada = Protagonist("Tatsuo Shinada", "Masculino")
# masayoshi_tanimura = Protagonist("Masayoshi Tanimura", "Masculino")
# haruka_sawamura = Protagonist("Haruka Sawamura", "Feminino")
# taiga_saejima = Protagonist("Taiga Saejima", "Masculino")
# shun_akiyama = Protagonist("Shun Akiyama", "Masculino")
# koichi_adachi = Protagonist("Koichi Adachi", "Masculino")
# saeko_mukoda = Protagonist("Saeko Mukoda", "Feminino")
# joon_gi_han = Protagonist("Joon-gi Han", "Masculino")
# tianyou_zhao = Protagonist("Tianyou Zhao", "Masculino")
# yu_nanba = Protagonist("Yu Nanba", "Masculino")

# protagonist_crud.create_protagonist(kiryu_kazuma)
# protagonist_crud.create_protagonist(goro_majima)
# protagonist_crud.create_protagonist(ichiban_kasuga)
# protagonist_crud.create_protagonist(tatsuo_shinada)
# protagonist_crud.create_protagonist(masayoshi_tanimura)
# protagonist_crud.create_protagonist(haruka_sawamura)
# protagonist_crud.create_protagonist(taiga_saejima)
# protagonist_crud.create_protagonist(shun_akiyama)
# protagonist_crud.create_protagonist(koichi_adachi)
# protagonist_crud.create_protagonist(saeko_mukoda)
# protagonist_crud.create_protagonist(joon_gi_han)
# protagonist_crud.create_protagonist(tianyou_zhao)
# protagonist_crud.create_protagonist(yu_nanba)

# sec_haruka_sawamura = Secondary_Character("Haruka Sawamura", "Feminino")
# sec_tacchibana = Secondary_Character("Tacchibana", "Masculino")
# sec_kashiwagi = Secondary_Character("Kashiwagi", "Masculino")
# sec_makoto_makimura = Secondary_Character("Makoto Makimura", "Feminino")
# sec_makoto_date = Secondary_Character("Makoto Date", "Masculino")
# sec_shintaro_kazama = Secondary_Character("Shintaro Kazama", "Masculino")
# sec_kaoru_sayama = Secondary_Character("Kaoru Sayama", "Feminino")
# sec_daigo_dojima = Secondary_Character("Daigo Dojima", "Masculino")
# sec_taiga_saejima = Secondary_Character("Taiga Saejima", "Masculino")
# sec_goro_majima = Secondary_Character("Goro Majima", "Masculino")
# sec_shun_akiyama = Secondary_Character("Shun Akiyama", "Masculino")
# sec_kiryu_kazuma = Secondary_Character("Kiryu Kazuma", "Masculino")

# character_crud.create_character(sec_haruka_sawamura)
# character_crud.create_character(sec_tacchibana)
# character_crud.create_character(sec_kashiwagi)
# character_crud.create_character(sec_makoto_makimura)
# character_crud.create_character(sec_makoto_date)
# character_crud.create_character(sec_shintaro_kazama)
# character_crud.create_character(sec_kaoru_sayama)
# character_crud.create_character(sec_daigo_dojima)
# character_crud.create_character(sec_taiga_saejima)
# character_crud.create_character(sec_goro_majima)
# character_crud.create_character(sec_shun_akiyama)

# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_0)
# query.create_relacionamento_protagonist_game(goro_majima,yakuza_0)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_kiwami)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_kiwami_2)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_3)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_4)
# query.create_relacionamento_protagonist_game(shun_akiyama,yakuza_4)
# query.create_relacionamento_protagonist_game(masayoshi_tanimura,yakuza_4)
# query.create_relacionamento_protagonist_game(taiga_saejima,yakuza_4)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_5)
# query.create_relacionamento_protagonist_game(shun_akiyama,yakuza_5)
# query.create_relacionamento_protagonist_game(tatsuo_shinada,yakuza_5)
# query.create_relacionamento_protagonist_game(haruka_sawamura,yakuza_5)
# query.create_relacionamento_protagonist_game(taiga_saejima,yakuza_5)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,yakuza_6)
# query.create_relacionamento_protagonist_game(ichiban_kasuga,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(koichi_adachi,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(saeko_mukoda,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(joon_gi_han,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(tianyou_zhao,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(yu_nanba,yakuza_like_a_dragon)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,like_a_dragon_infinite_wealth)
# query.create_relacionamento_protagonist_game(ichiban_kasuga,like_a_dragon_infinite_wealth)
# query.create_relacionamento_protagonist_game(kiryu_kazuma,like_a_dragon_gaiden_the_man_who_erased_his_name)
# query.create_relacionamento_protagonist_game(kiryu_kazuma, like_a_dragon_ishin)

# query.create_relacionamento_secondary_character_game(sec_haruka_sawamura, yakuza_0)
# query.create_relacionamento_secondary_character_game(sec_tacchibana, yakuza_0)
# query.create_relacionamento_secondary_character_game(sec_kashiwagi, yakuza_0)
# query.create_relacionamento_secondary_character_game(sec_makoto_makimura, yakuza_0)
# query.create_relacionamento_secondary_character_game(sec_makoto_date, yakuza_kiwami)
# query.create_relacionamento_secondary_character_game(sec_haruka_sawamura, yakuza_kiwami)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_kiwami)
# query.create_relacionamento_secondary_character_game(sec_shintaro_kazama, yakuza_kiwami)
# query.create_relacionamento_secondary_character_game(sec_kashiwagi, yakuza_kiwami)
# query.create_relacionamento_secondary_character_game(sec_makoto_date, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_kashiwagi, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_kaoru_sayama, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_haruka_sawamura, yakuza_kiwami_2)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_3)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, yakuza_3)
# query.create_relacionamento_secondary_character_game(sec_kashiwagi, yakuza_3)
# query.create_relacionamento_secondary_character_game(sec_makoto_date, yakuza_3)
# query.create_relacionamento_secondary_character_game(sec_haruka_sawamura, yakuza_3)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_4)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, yakuza_4)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_5)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, yakuza_5)
# query.create_relacionamento_secondary_character_game(sec_haruka_sawamura, yakuza_6)
# query.create_relacionamento_secondary_character_game(sec_shun_akiyama, yakuza_6)
# query.create_relacionamento_secondary_character_game(sec_kiryu_kazuma, yakuza_like_a_dragon)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, yakuza_like_a_dragon)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, yakuza_like_a_dragon)
# query.create_relacionamento_secondary_character_game(sec_taiga_saejima, yakuza_like_a_dragon)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, like_a_dragon_infinite_wealth)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, like_a_dragon_infinite_wealth)
# query.create_relacionamento_secondary_character_game(sec_taiga_saejima, like_a_dragon_infinite_wealth)
# query.create_relacionamento_secondary_character_game(sec_goro_majima, like_a_dragon_gaiden_the_man_who_erased_his_name)
# query.create_relacionamento_secondary_character_game(sec_daigo_dojima, like_a_dragon_gaiden_the_man_who_erased_his_name)
# query.create_relacionamento_secondary_character_game(sec_taiga_saejima, like_a_dragon_gaiden_the_man_who_erased_his_name)

