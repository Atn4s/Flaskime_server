import sqlite3, os, sys, requests, traceback
from flask import Flask, app, jsonify, request
from flask_cors import CORS

app = Flask('Flaskime') 
CORS(app, resources={r"/*": {"origins": "*"}})  

def verifyData():
    if not os.path.exists('listaanime.db'):
        os.system('python3 banco.py')

for number in range(2):
    verifyData()

@app.route('/buscar/<nome_anime>', methods=['GET']) 
def jikanAPI(nome_anime):
    url = f'https://api.jikan.moe/v4/anime?q={nome_anime}'
    response = requests.get(url) 
     
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
    elif response.status_code == 404:
        return jsonify({"Anime não encontrado"},404)
    
@app.route('/buscar', methods=['POST'])
def inserirAnime():
    try:
        data = request.get_json()
        if anime_existe_no_banco(data.get('title')):
            return jsonify({'message': 'Anime: ' + data.get('title') + ' já existe no banco de dados.'}, 400)

        inserir_dados_no_banco(data)
        return jsonify({'message': 'Anime: ' + data.get('title') +  ' adicionado com sucesso ao banco de dados!'}, 200)
    except sqlite3.Error as e:
        print(f"Erro SQLite: {e}")
    except Exception as e:
        print(f'Erro ao processar a requisição: {str(e)}')
        traceback.print_exc() 
        return jsonify({'error': f'Erro interno: {str(e)}'}, 400)
    
def anime_existe_no_banco(titulo_anime):
    try:
        with sqlite3.connect('listaanime.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM Anime WHERE title = ?', (titulo_anime,))
            resultado = cursor.fetchone()        
        return resultado is not None
    except sqlite3.Error as e:
        print(f"Erro SQLite: {e}")
    except Exception as e:
        print(f"Erro ao verificar se o anime existe no banco: {e}")
        return False

def inserir_dados_no_banco(anime_data):
    try:
        colunas_presentes = list(anime_data.keys()) + ['is_watched']
        valores_presentes = list(anime_data.values()) + [anime_data.get('is_watched',0)]  

        with sqlite3.connect('listaanime.db') as conn:
            cursor = conn.cursor()
            columns = ", ".join(colunas_presentes)
            placeholders = ", ".join("?" for _ in colunas_presentes)
            query = f"INSERT INTO Anime ({columns}) VALUES ({placeholders})"
            valores_convertidos = []
            for valor in valores_presentes:
                if isinstance(valor, list) or isinstance(valor, dict):
                    valores_convertidos.append(str(valor))
                else:
                    valores_convertidos.append(valor)
            cursor.execute(query, tuple(valores_convertidos))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Erro SQLite ao inserir dados: {e}")
    except Exception as e:
        print(f"Erro ao inserir dados no banco. Tipo de exceção: {type(e)}, Mensagem: {str(e)}")

@app.route('/editar', methods=['GET']) 
def listaranime():
    with sqlite3.connect('listaanime.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Anime")
        data = cursor.fetchall()        
    response = {"data": data}
    return jsonify(response), 200

@app.route('/editar', methods=['PUT']) 
def editaranime():
    data = request.get_json()
    name=data.get('id') 
    watched = data.get('watched')
    with sqlite3.connect('listaanime.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE Anime SET is_watched=? WHERE title=?",[watched,name])
        data = cursor.fetchone()
        conn.commit()  
    return jsonify({"message": "Atualização bem-sucedida"}), 200

@app.route('/editar', methods=['DELETE'])
def deletaranime():
    data = request.get_json()      
    name=data.get('id') 
    with sqlite3.connect('listaanime.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Anime WHERE title=?",[name])
        data = cursor.fetchone()
        conn.commit()  
    return jsonify({"message": "Exclusão bem-sucedida"}), 200

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    app.run(debug=True, port=port, host='0.0.0.0')