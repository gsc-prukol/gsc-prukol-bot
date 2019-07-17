import os


class WebHook:
    host = 'https://telogram-bot.herokuapp.com'  # name your app
    path = '/webhook/'
    webapp_host = '0.0.0.0'
    webapp_port = os.environ.get('PORT')
    url = f"{host}{path}"


class BotConfig:
    token = os.environ['TOKEN']


class Messages:
    firstPhrase = 'А пошук не працює?'
    printing = "Друкують в 4-01 t.me/Froooger, t.me/Drectar, 0,75 грн/А4 (лише чб)"
    clinic = "Номери реєстратури: (044) 204-95-93 і (044) 204-85-62. Телефонуй їм."


class Regexp:
    printing = '.*(где|кто|де|хто|(в|у) кого).*(печат|друк|принт).*'
    clinic = "(.*(?:телефон|номер|работает).*(поліклінік|поликлиник|регистрат|реєстрат).*)|" \
             "(.*(поліклінік|поликлиник|регистратур|реєстр).*(?:телефон|номер|работает).*)"
