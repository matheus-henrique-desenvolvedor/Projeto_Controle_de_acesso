import pandas as pd
import uuid
import qrcode

class Cadastro:
    def __init__(self):
        self.cd = pd.read_excel("C:\\Users\\Mathusa\\Desktop\\Controle de acesso\\dataset.xlsx")        
        self.cpf = None
        self.nome = None
        self.data = None
        self.cep_atual = None
        self.telefone = None
        self.genero = None
        self.imagem= None
        self.id = uuid.uuid1()
        self.id = str(self.id)
        

    def validiCpf(self, dados):
        self.cpf = dados['CPF']
        print(self.cpf)       
    
        
    def full_name(self, dados):
        self.nome = dados['Nome']
        print(self.nome)
        

    def birth_data(self, dados):
        self.data = dados['Data de Nascimento']
        print(self.data)


    def CEP(self, dados):
        cep = dados['Endereço']
        if cep:
            cep= str(cep)
            regiao = cep[0:5]
            identificador = cep[5:]
            self.cep_atual = f'{regiao}-{identificador}'
            print(self.cep_atual)


    def numero_fone(self, dados):
        self.telefone = dados['Telefone']
        print(self.telefone)


    def natureza(self, dados):
        self.genero = dados['Gênero']
        print(self.genero)
        

    def gera_qrcode(self):
        imagem = qrcode.make(self.nova_linha["id"][0])
        self.nome = str(self.nova_linha["nome"][0])
        imagem.save(f"qrcode_{self.nome}.png")


    def nova_linha(self, dados):
        self.nova_linha = pd.DataFrame({
            "id":[self.id],
            "nome": [self.nome],
            "CPF":[self.cpf],
            "data_de_nascimento": [self.data],
            "genero":[self.genero],
            "cep":[self.cep_atual],
            "fone":[self.telefone]
    })
        print(self.nova_linha)

        f1 = pd.concat([self.cd,self.nova_linha], ignore_index=True)
        print(f1)
        f1.to_excel("C:\\Users\\Mathusa\\Desktop\\Controle de acesso\\dataset.xlsx", index=False)


    def run(self, dados): 
        self.validiCpf(dados)
        self.full_name(dados)
        self.birth_data(dados)
        self.CEP(dados)
        self.numero_fone(dados)
        self.natureza(dados)
        self.nova_linha(dados)
        self.gera_qrcode()