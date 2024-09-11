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

"""
#Rota / -> Listar os endpoints disponíveis
@app.route('/', methods=['GET'])
def inicial():
    return '''- /devs - Método GET -> LISTAR todos os desenvolvedores cadastrados<br>
	      - /devs/[linguagem de programação] - Método GET -> LISTAR desenvolvedores POR ling. programação<br>
	      - /devs/[id] - Método GET -> LISTAR desenvolvedor POR ID<br>
	      - /devs/[id] - Método PUT -> ATUALIZAR desenvolvedor POR ID<br>
	      - /devs/[id] - Método DELETE -> Exclui desenvolvedor por id<br>
	      - /devs - Método POST -> INSERIR desenvolvedor<br>
''', 200
"""

#Rota / -> Listar os endpoints disponíveis
@app.route('/', methods=['GET'])
def inicial():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Uso da API Devs</title>
            <style>
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                table, th, td {
                    border: 1px solid black;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
            </style>
        </head>
        <body>
            <h1> API Desenvolvedores </h1>
            <table>
                <thead>
                    <tr>
                        <th>Rotas</th>
                        <th>Método HTTP</th>
                        <th>Função</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>/devs</td>
                        <td>GET</td>
                        <td>LISTAR todos os desenvolvedores cadastrados</td>
                    </tr>
                    <tr>
                        <td>/devs/[linguagem de programação]</td>
                        <td>GET</td>
                        <td>LISTAR desenvolvedores POR ling. programação</td>
                    </tr>
                    <tr>
                        <td>/devs/[id]</td>
                        <td>GET</td>
                        <td>LISTAR desenvolvedor POR ID</td>
                    </tr>
                    <tr>
                        <td>/devs/[id]</td>
                        <td>PUT</td>
                        <td>ATUALIZAR desenvolvedor POR ID</td>
                    </tr>
                    <tr>
                        <td>/devs/[id]</td>
                        <td>DELETE</td>
                        <td>EXCLUIR desenvolvedor por id</td>
                    </tr>
                    <tr>
                        <td>/devs</td>
                        <td>POST</td>
                        <td>INSERIR desenvolvedor</td>
                    </tr>
                </tbody>
            </table>
        </body>
        </html>
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