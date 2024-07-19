import re
import sys

class ValidaCpf:
    def cpf_enviado_usuario(self):
        self.entrada = re.sub(r'\D', '', self.entrada) 
        self.cpf_enviado_usuario = re.sub(
            r'[^0-9]',
            '',
                self.entrada 
            ) 
        

    def entrada_e_sequencial(self):
        self.entrada == self.entrada[0] * len(self.entrada)       
        if self.entrada_e_sequencial:
            print('Você enviou dados sequenciais.')
            sys.exit()
        print(self.entrada)


    def calcular_digito(self, digitos, contador_regressivo):       
        resultado = 0
        for digito in digitos:   
            resultado += int(digito) * contador_regressivo
            contador_regressivo -= 1

        digito = (resultado * 10) % 11
        digito = digito if digito <= 9 else 0
        return digito
                

    def validar(self):
        digito_1 = self.calcular_digito(self.entrada, 10)
        dez_digitos = self.entrada[:9]+ str(digito_1)
        digito_2 = self.calcular_digito(dez_digitos, 11)
        cpf_calculado = self.entrada[:9] + str(digito_1) + str(digito_2)
        if cpf_calculado == self.entrada:
            return True 
        else:
            return False


    def print_entrada(self):
        print(self.entrada)


    def run(self, dados):
        self.entrada = dados  
        response = self.validar() 
        return [response, self.entrada]