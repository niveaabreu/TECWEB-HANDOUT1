import json

def extract_route(requisiçao):
    requisiçao = requisiçao.split(" HTTP/")[0]
    return requisiçao.split(" /")[1]

def read_file(caminho):
    with open(caminho,"r+b") as arquivo:
        return arquivo.read()

def load_data(nome):
    jsonfile = read_file("data/"+nome)
    nome=json.loads(jsonfile)
    return nome

def load_template(nome_arquivo):
    with open("templates/"+nome_arquivo,"r") as arquivo:
        return arquivo.read()
    # carregar = read_file("templates/"+nome_arquivo)
    # return carregar
    
def salvar_dados(nomedojson,dicionario):
    in_file = load_data(nomedojson)  #carregando um arquivo json em uma lista em python.
    in_file.append(dicionario)   #adc nova notação na lista.
    with open("data/notes.json", "w", encoding="utf-8") as dados:  #pegando o arquivo python e transformando em json.
        salvando = json.dump(in_file, dados, indent=2, separators=(",", ": "), sort_keys=True)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers=="":
        return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode() #isso transforma de string pra bytes
    return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()