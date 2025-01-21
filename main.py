from flask import Flask, jsonify, request
from conect import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/barbeiros', methods=['GET'])
def buscarBarbeiros():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM barbeiros")
  lista_de_barbeiros = cursor.fetchall()
  lista_pro_json = []
  for barbeiro_da_vez in lista_de_barbeiros:
    novo_dicionario = {
      "id": barbeiro_da_vez[0],
      "nome": barbeiro_da_vez[1],
      "cpf": barbeiro_da_vez[2],
      "telefone": barbeiro_da_vez[3]
    }
    lista_pro_json.append(novo_dicionario)
  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)


@app.route("/barbeiros", methods=['POST'])
def adicionarBarbeiro():
  data = request.get_json()
  nome = data['nome']
  cpf = data['cpf']
  telefone = data['telefone']
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                INSERT INTO barbeiros (nome, cpf, telefone) VALUES 
                  (%s, %s, %s)
                 """, (nome, cpf, telefone))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Barbeiro Cadastrado com Sucesso"})




@app.route("/barbeiros/<int:id>", methods=['PUT'])
def atualizarBarbeiro(id):
  data = request.get_json()
  nome = data['nome']
  cpf = data['cpf']
  telefone = data['telefone']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                UPDATE barbeiros SET nome = %s, cpf = %s, telefone = %s WHERE id = %s
                 """, (nome, cpf, telefone, id))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Barbeiro Atualizado com Sucesso"})




@app.route("/barbeiros/<int:id>", methods=['DELETE'])
def deletarBarbeiro(id):
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                DELETE FROM barbeiros WHERE id = %s
                 """, (id))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Barbeiro Deletado com Sucesso"})










@app.route('/servicos', methods=['GET'])
def buscarServicos():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM servicos")
  lista_de_servicos = cursor.fetchall()
  lista_pro_json = []
  for servico_da_vez in lista_de_servicos:
    novo_dicionario = {
      "id": servico_da_vez[0],
      "nome": servico_da_vez[1],
      "descricao": servico_da_vez[2],
      "valor": servico_da_vez[3],
      "porcentagem_barbeiro": servico_da_vez[4],
    }
    lista_pro_json.append(novo_dicionario)
  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)




@app.route("/servicos", methods=['POST'])
def adicionarServico():
  data = request.get_json()
  nome = data['nome']
  descricao = data['descricao']
  valor = data['valor']
  porcentagem_barbeiro = data['porcentagem_barbeiro']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                INSERT INTO servicos (nome, descricao, valor, porcentagem_barbeiro) VALUES 
                  (%s, %s, %s, %s)
                 """, (nome, descricao, valor, porcentagem_barbeiro))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Serviço Cadastrado com Sucesso"})




@app.route("/servicos/<int:id>", methods=['PUT'])
def atualizarServico(id):
  data = request.get_json()
  nome = data['nome']
  descricao = data['descricao']
  valor = data['valor']
  porcentagem_barbeiro = data['porcentagem_barbeiro']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                UPDATE servicos SET nome = %s, descricao = %s, valor = %s, porcetagem_barbeiro = %s WHERE id = %s
                 """, (nome, descricao, valor, porcentagem_barbeiro, id))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Serviço Atualizado com Sucesso"})




@app.route("/servicos/<int:id>", methods=['DELETE'])
def deletarServico(id):
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                DELETE FROM servicos WHERE id = %s
                 """, (id))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Serviço Deletado com Sucesso"})








@app.route('/atendimentos', methods=['GET'])
def buscarAtendimentos():
  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("SELECT * FROM atendimentos")
  lista_de_atendimentos = cursor.fetchall()
  lista_pro_json = []
  for atendimento_da_vez in lista_de_atendimentos:
    novo_dicionario = {
      "id": atendimento_da_vez[0],
      "data_atendimento": atendimento_da_vez[1],
      "id_barbeiro": atendimento_da_vez[2],
      "id_servico": atendimento_da_vez[3],
    }
    lista_pro_json.append(novo_dicionario)
  cursor.close()
  conexao.close()
  return jsonify(lista_pro_json)



@app.route("/atendimentos", methods=['POST'])
def adicionarAtendimento():
  data = request.get_json()
  data_atendimento = data['data_atendimento']
  id_barbeiro = data['id_barbeiro']
  id_servico = data['id_servico']

  conexao = fazerConexao()
  cursor = conexao.cursor()
  cursor.execute("""
                INSERT INTO servicos (data_atendimento, id_barbeiro, id_servico) VALUES 
                  (%s, %s, %s)
                 """, (data_atendimento, id_barbeiro, id_servico))
  conexao.commit()
  cursor.close()
  conexao.close()
  return jsonify({"mensagem": "Atendimento Realizado com Sucesso"})




if __name__ == "__main__":
  app.run(debug=True)