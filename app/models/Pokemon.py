# Importando a biblioteca requests
import requests

# Criando a classe para os métodos de busca
class Pokemon:
    def __init__(self, opcao: str) -> None:
        self.opcao = opcao
        self.URL_APR = f'https://pokeapi.co/api/v2/pokemon/{self.opcao}/'
    
    def buscar_pokemon(self) -> int or dict:
        response = requests.get(self.URL_APR)

        if response.status_code == 200:
            json_dados = response.json()

            hab_2  = json_dados['abilities'][1]['ability']['name'] if len(json_dados['abilities']) > 1 else 'Não possui'
            
            dados: dict = {
                'nome': json_dados['name'],
                'id': json_dados['game_indices'][3]['game_index'],
                'imagem': json_dados['sprites']['front_default'],
                'gif': json_dados['sprites']['versions']['generation-v']['black-white']['animated']['front_default'],
                'altura': json_dados['height'],
                'peso': json_dados['weight'],
                'tipo': json_dados['types'][0]['type']['name'],
                'habilidade_1': json_dados['abilities'][0]['ability']['name'],
                'habilidade_2': hab_2
            }
            return dados
        else: 
            return response.status_code
