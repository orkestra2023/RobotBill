import datetime
import wikipedia
import requests
import socket

from Arduino.ControlaArduino import Arduino
from util.Ordem_Comando import executa_comando, maquina
from util.extenso_numero import numero_por_extenso, data_por_extenso
from util.Sistema_IA import executa_IA

def verificar_conexao_internet():
    try:
        # Tenta estabelecer uma conexão com um servidor remoto
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def abrir_YouTube(descricao):

    if verificar_conexao_internet():
        import pywhatkit
        pywhatkit.playonyt(descricao)
    try:
        return 'Tocando música: ' + descricao
    except Exception as e:
        return 'Erro ao tentar Tocar Música. Verifique sua Conexão.'

def analisa_Pesquisa(resp):

    if len(resp) > 2500:
        maquina.say('Minha resposta é um pouco extensa, deseja escuta-la?')
        maquina.runAndWait()

        comando = executa_comando()
        if 'sim' in comando:
            return True
        else:
            return False

def comando_voz_usuario():

    # Inicializa o contexto da conversa
    context = ""
    comando = executa_comando()
    comando_anterior = ""

    if 'pesquise por' in comando:
        procurar = comando.replace('pesquise por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()

    elif 'toque' in comando:
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        musica = comando.replace('toque','')
        msn = abrir_YouTube(musica)
        #maquina.say('Tocando música: ' + musica)
        maquina.say(msn)
        maquina.runAndWait()

    elif 'quem é você' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'quem és tu' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'como se chamas' in comando:
        maquina.say('Eu me chamo Bill.')
        maquina.runAndWait()
    elif 'como se chama-se' in comando:
        maquina.say('Eu me chamo Bill.')
        maquina.runAndWait()
    elif 'qual o seu nome' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'qual o teu nome' in comando:
        maquina.say('Eu sou a Bill.')
        maquina.runAndWait()
    elif 'error' in comando:
        maquina.say('Pode repetir, por favor?')
        maquina.runAndWait()

    elif 'bill' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bill','')
        maquina.say(ordem)
        maquina.runAndWait()
        #Arduino.ComandaNerf(ordem)
        Arduino.SistemasArduino(ordem)

    elif 'bil' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bil','')
        maquina.say(ordem)
        maquina.runAndWait()
        #Arduino.ComandaNerf(ordem)
        Arduino.SistemasArduino(ordem)

    elif 'bio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('bio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'viu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('viu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'eu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('eu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'vi o' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('vi o','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'dio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('dio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'tio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('tio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'deu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('deu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'meu' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('meu','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'mio' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('mio','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'digo' in comando.lower():
        # Só funciona on-line. Corrigir o erro quando o PC estiver off-line.
        ordem = comando.replace('digo','')
        maquina.say(ordem)
        maquina.runAndWait()
        Arduino.SistemasArduino(ordem)

    elif 'comando' in comando.lower():

        while True:
            #comando = executa_comando()
            #comando = input(comando)
            comando = input("Você: ")

            if 'sair' in comando:
                break

            resposta = executa_IA(comando).replace('*', '')
            print("Gemini: ", resposta, "\n")

            maquina.say(resposta)
            maquina.runAndWait()
    else:
        # Gera a resposta utilizando o contexto atual
        # resposta = executa_IA(comando).replace('*', '')
        # print("Gemini: ", resposta, "\n")
        # maquina.say(resposta)
        # maquina.runAndWait()
        while True:
            # Recebe o comando de voz da função "executa_comando()"
            comando_voz = executa_comando()

            # Processa o comando e gera a resposta
            resposta = executa_IA(comando_voz).replace('*', '')
            print("Gemini: ", resposta, "\n")

            # Fala a resposta para o usuário
            maquina.say(resposta)
            maquina.runAndWait()

            # Verifica se o comando foi "sair" para finalizar o loop
            if 'sair' in comando_voz:
                break

while True:
    comando_voz_usuario()

#maquina.say("Olá, eu sou um modelo de linguagem treinado pelo OpenAI.")

#maquina.runAndWait()