from flask import Flask, jsonify, request

app = Flask(__name__)

# Cadastro de desenvolvedores por linguagem de programação
devs = [
    {
        'id': 1,
        'name': 'Consuelo',
        'lang': 'C++'
    },
    {
        'id': 2,
        'name': 'Pedro',
        'lang': 'Python'
    },
    {
        'id': 3,
        'name': 'Jose Silva',
        'lang': 'JavaScript'
    },
    {
        'id': 4,
        'name': 'Tenorio Salvador',
        'lang': 'TypeScript'
    },
    {
        'id': 5,
        'name': 'Claudio Costa',
        'lang': 'C++'
    },
    {
        'id': 6,
        'name': 'Cristiano Couto',
        'lang': 'C++'
    },
    {
        'id': 7,
        'name': 'Carmem Cristina',
        'lang': 'C++'
    },
    {
        'id': 8,
        'name': 'Tadeu Santos',
        'lang': 'TypeScript'
    },
    {
        'id': 9,
        'name': 'Janete Santana',
        'lang': 'JavaScript'
    },
    {
        'id': 10,
        'name': 'Paulo',
        'lang': 'Python'
    }
]

#Rota / -> Listar os endpoints disponíveis
@app.route('/', methods=['GET'])
def inicial():
    return '''Rota /devs -> LISTAR todos os desenvolvedores cadastrados<br>
	      Rota /devs/[linguagem de programação] -> LISTAR desenvolvedores POR ling. programação<br>
	      Rota /devs/[id] -> LISTAR desenvolvedor POR ID<br>
	      <HR> 
	      Rota /devs/[id] - Método PUT -> ATUALIZAR desenvolvedor POR ID<br>
	      Rota /devs/[id] - Método DELETE -> Exclui desenvolvedor por id<br>
	      Rota /devs - Método POST -> INSERIR desenvolvedor<br>
''', 200

# Rota /devs -> LISTAR todos os desenvolvedores cadastrados
@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200

# Rota /devs/<linguagem de programação> -> LISTAR desenvolvedores POR ling. programação
@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'].lower() == lang]
    return jsonify(devs_per_lang), 200

# Rota /devs/<id> Método PUT -> ATUALIZAR desenvolvedor POR ID
@app.route('/devs/<int:id>', methods=['PUT'])
def change_lang(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            return jsonify(dev), 200
    return jsonify({'error': 'dev not found'}), 404

# Rota /devs/<id> -> LISTAR desenvolvedor por ID
@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error': 'not found'}), 404

# Rota /devs método POST -> INSERIR desenvolvedor 
@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201

# Rota /devs/<id> método DELETE -> Exclui desenvolvedor por id 
@app.route('/devs/<int:id>', methods=['DELETE'])
def remove_dev(id):
    index = id - 1
    del devs[index]
    return jsonify({'message': 'Dev is no longer alive'}), 200

# Inicializa app
if __name__ == '__main__':
    app.run(debug=True)