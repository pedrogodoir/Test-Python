nome = (input("Qual seu nome? "))
print("olá, " + nome + "!")
from datetime import date
data = date.today()
def pergunta_idade():
    idade = (input("Qual o ano que você nasceu? (digite quatro numeros) "))
    numeroIdade = int(idade)
    if len(idade) == 4:
        resultado = data.year - numeroIdade
        strResultado = str(resultado)
        print("Você tem " + strResultado + " anos.")
    elif not idade.isdigit():
        print("Digite apenas numeros!")
        pergunta_idade()
    elif len(idade) < 4:
        print("Você digitou menos numeros!")
        pergunta_idade()
    else:
        print("Você digitou mais numeros!")
        pergunta_idade()
pergunta_idade()