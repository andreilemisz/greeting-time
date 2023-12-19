# Programa para mostrar uma mensagem de Bom dia, Boa tarde ou Boa noite #
# dependendo do input do usuário #
# Calibrado para reconhecer dois pontos e impedir minutos acima de 60 #
import os
horario_usuario = ""
horario_tornou_float = None
programa_ativado = True
sair_programa = ""

""" Programa ativado para rodar várias vezes. Input do usuário no final para encerrar """

while programa_ativado:

    """ Input do usuário já converte dois pontos em ponto para futuramente virar float """

    horario_usuario = input("Forneça um horário: ").replace(":", ".")
    
    """ Verificação dos minutos para evitar algo além de 59 """
    
    if horario_usuario.find("."):
        minutos = horario_usuario.find(".") + 1
        try:
            float(horario_usuario)
            if int(horario_usuario[minutos]) >= 6:
                horario_usuario = ""
        except:
            pass
    
    """ Tranformação do input em float sem quebrar o programa"""
    """ Se houver qualquer caracter indevido inserido será barrado aqui """
    
    try:
        horario_usuario = float(horario_usuario)
        horario_tornou_float = True
    except:
        horario_tornou_float = False       
    
    """ Usar o float final para definir qual mensagem aparecer ao usuário """
    """ Se a hora inserida for maior do que 24 aparecerá a mensagem de erro """
        
    if horario_tornou_float == True and horario_usuario <= 11:
        print("Bom dia!")
    elif horario_tornou_float == True and (horario_usuario >= 12 and horario_usuario <= 17):
        print("Boa tarde!")
    elif horario_tornou_float == True and (horario_usuario >= 18 and horario_usuario < 24):
        print("Boa noite!")
    else:
        print("Você não digitou um horário válido.")
            
    """ Input do usuário para encerrar o programa ou inserir novo horário """
    
    sair_programa = input("Você gostaria de encerrar o programa? Digite [s] para sair: ").lower()
    if sair_programa == "s":
        programa_ativado = False
        print("Você encerrou o programa.")
    else:
        horario_usuario = ""
        horario_tornou_float = None
        sair_programa = ""
        os.system("cls")