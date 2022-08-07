from app import app
from flask import render_template, request, redirect, url_for
from app.models import Pokemon

# Rota de início da aplicação
@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Rota de busca de pokemons
@app.route('/buscar', methods=['POST', 'GET'])
def buscar():
    if request.method == 'POST':
        # Pegando o nome do pokemon
        opcao = 'pikachu' if request.form['pesquisa'] == ' ' else request.form['pesquisa']
        
        # Criando um objeto do tipo Pokemon
        pokemon = Pokemon.Pokemon(opcao)

        # Buscando o pokemon
        dados = pokemon.buscar_pokemon()

        # Verificando se o pokemon existe
        if type(dados) == int:
            return render_template('erro.html', codigo=dados)
        else:
            # Retornando os dados do pokemon
            return render_template('resultado.html', nome=dados['nome'], id=dados['id'],
                                    gif=dados['gif'], altura=dados['altura'],
                                    peso=dados['peso'], tipo=dados['tipo'],
                                    habilidade1=dados['habilidade_1'], habilidade2=dados['habilidade_2'])
    else:
        return redirect(url_for('index'), code=302)
