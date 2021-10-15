# CÓDIGO SIMPLES BOT DO TELEGRAM
# FEITO POR: MATHEUS MAIA ALVAREZ
# GITHUB: https://github.com/MatheusAlvarez
# CONTATO: (11)99423-7418


#Biblioteca que ajuda a gente a criar um bot (PRECISA INSTALAR O "pytelegrambotapi")
import telebot

# Chave API que o BotFather do telegram te envia
cv_api = "SUA CHAVE API"

bot = telebot.TeleBot(cv_api)

# Seção comando selecionado: carne
@bot.message_handler(commands=["carne"])
def carne(mensagem):
    # Mensagem que o bot vai enviar para o usuário      
    bot.send_message(mensagem.chat.id, "SÓ TEM PICANHA!: Tempo de espera em 20min")

# Seção comando selecionado: frango
@bot.message_handler(commands=["frango"])
def frango(mensagem):
    bot.send_message(mensagem.chat.id, "MELHOR FRANGO DA CIDADE: Tempo de espera em 20min")

# Seção comando selecionado: linguiça
@bot.message_handler(commands=["linguica"])
def linguica(mensagem):
    bot.send_message(mensagem.chat.id, "DEMOROU PARCEIRO, a linguiça acabou")

# Seção comando selecionado: opção1
@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    #Texto que o bot vai enviar parar o usuário     
    texto = """
    O que você quer? (Clique em uma opção)
    /carne Carne
    /frango Frango
    /linguica Linguiça"""
    bot.send_message(mensagem.chat.id, texto)

# Seção comando selecionado: opção2
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para contato@geek.com")

# Seção comando selecionado: opção3
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado! ❤")


# Função para retornar o valor: True
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Ver o nosso cardápio
     /opcao2 Reclamação de um pedido
     /opcao3 Mandar elogio para o bot"""
    bot.reply_to(mensagem, texto)

bot.polling()
