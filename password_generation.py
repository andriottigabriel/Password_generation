
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#============================================ - X
#||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||Site          |||||                 ||||
#||||||||E-mail/Usuário|||||                 ||||
#Quantidade de caracteres:||    |||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||
#||||                                        ||||
#||||                                        ||||
#||||                                        ||||
#||||                                        ||||
#||||||||||||||||||||||||||||||||||||||||||||||||
#||||GERAR SENHA|||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import random  #Importa a biblioteca random, que é usada para gerar senhas aleatórias.
import PySimpleGUI as sg #Importa a biblioteca PySimpleGUI com um alias sg, que é usada para criar a interface gráfica.
import os # Importa a biblioteca os, que será usada para criar arquivos.
from playsound import playsound #Importa a função playsound da biblioteca playsound, que é usada para reproduzir um som.


class PassGen:  #Define uma classe chamada PassGen para encapsular o programa
    def __init__(self): #Define o método construtor da classe PassGen. Esse método é executado quando um objeto da classe é criado.

        #LAYOUT
        sg.theme('Black') #Define o tema da interface gráfica como "Black".
        playsound('6OZh916QF8XNunWaP97WEZ218 - Jonas Blue, Dakota - Fast Car.temp.mp3', block=False) #Reproduz um som
        layout = [ #Define a estrutura da interface gráfica usando uma lista de elementos, como rótulos de texto, campos de entrada, botões etc.
            [sg.Text('Site', size=(12,1)), #nome da caixa e tamanho do espaçamento
            sg.Input(key='site', size=(20,1))], #tamanho da caixa do site
            [sg.Text('E-mail/Usuário', size=(12,1)),#nome da caixa e tamanho do espaçamento
            sg.Input(key='usuario',size=(20,1))], #tamanho da caixa do site
            [sg.Text('Quantidade de caracteres:'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=1, size = (3,1))],
            [sg.Output(size=(34,5))],
            [sg.Button('Gerar senha')] # botão gerar senha
        ]

        #DECLARAR JANELA
        self.janela = sg.Window('Password Generator', layout)

        
    def Iniciar (self): #Define um método chamado Iniciar que é responsável por iniciar o programa.
        while True: #Inicia um loop infinito.
            evento, valores = self.janela.read() #Lê um evento da janela da interface gráfica e os valores dos elementos da interface.
            if evento == sg.WINDOW_CLOSED: #Verifica se o evento é o fechamento da janela.
                break # Encerra o loop se a janela for fechada.
            if evento == 'Gerar senha': #Verifica se o evento é o clique no botão "Gerar senha".
                nova_senha = self.gerar_senha(valores)  #Chama o método gerar_senha para criar uma nova senha com base nos valores fornecidos na interface.
                print(nova_senha) #Exibe a nova senha no console.
                self.salvar_senha(nova_senha, valores) #Chama o método salvar_senha para salvar a senha em um arquivo de texto.
            


    def gerar_senha (self, valores): #Define o método gerar_senha, que gera uma senha aleatória com base nos valores fornecidos.
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*' #Define uma lista de caracteres que podem ser usados na senha.
        chars = random.choices(char_list, k=int(valores['total_chars']))  #random permite gerar valores aleatórios(num. letra. listas)
        new_pass = ''.join(chars) #Converte a lista de caracteres em uma string para representar a senha.
        return new_pass #Retorna a senha gerada.

    def salvar_senha (self, nova_senha, valores): # Define o método salvar_senha, que salva as informações da senha em um arquivo de texto.
        with open ('senhas.txt', 'a', newline='') as arquivo: #Abre o arquivo 'senhas.txt' em modo de escrita ('a' para adicionar conteúdo ao arquivo) e atribui ao arquivo uma referência de contexto.
            arquivo.write( #Escreve as informações da senha no arquivo de texto.
                f"site: {valores['site']},usuario:{valores['usuario']},nova senha:{nova_senha}")
            
        print('Arquivo salvo') 


gen = PassGen() #Cria um objeto da classe PassGen.
gen.Iniciar() #Chama o método Iniciar para iniciar o programa e exibir a interface gráfica.