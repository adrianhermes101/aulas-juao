class Celular():
    bateria = 'Infinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'Cinza'
    modelo = 'Tijolão'

    def ligacao():
        print('Ligando...')

    def mensagem():
        print('Enviando Mensagem...')

    def jogo_cobrinha():
        print('Ligando...')

print(Celular.bateria)
print(Celular.jogo_cobrinha())