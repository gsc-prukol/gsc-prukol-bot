class Messages:
    firstPhrase = 'А пошук не працює? @gsc_prukol'
    printing = """Друкують в:
1) 2-37 t.me/muzykaKsenia 1 грн/А4
2) 3-04 t.me/Alkaaaaaaaa, 1 грн/А4
3) 4-39 t.me/Baron439, 1 грн/А4
4) 4-01 не друкують 😢
5) 3-19 t.me/Evgennyy, 1 грн/А4 (лише чб)"""
    clinic = "Номери реєстратури: (044) 204-95-93 і (044) 204-85-62. Телефонуй їм."
    fullNameManager = 'Олена Вікторівна (в телеграмі підписана як "Елена")'
    fullNameCastellansha = 'Зоя Анатоліївна'
    helloReply = 'Hello world!'
    helloNewMembers = 'Привіт) Вітаю в нашому неламповому чатіку'


class Regexp:
    printing = '.*(где|кто|де|хто|(в|у) кого).*(печат|друк|принт).*'
    clinic = "(.*(?:телефон|номер|работает).*(поліклінік|поликлиник|регистрат|реєстрат).*)|(.*(поліклінік|поликлиник|регистратур|реєстр).*(?:телефон|номер|работает).*)"
    numberManager = '(який|какой|підскажіть|подскажите) номер зав(и|ы|(і|е)дую\w{0,4})'
    numberTA = '(який|какой|підскажіть|подскажите) номер (ТА|т(е|а)ть?ян(и|ы) Андр(ії|ее)вн(и|ы))\??'
    fullNameManager = "(яке?|как) (звати|звуть|ім'я|имя|фио)( (в|у))? зав(у|(і|е)дую\w{0,4})"
    fullNameCastellansha = "(яке?|как) (звати|звуть|ім'я|имя|фио)( (в|у))? кастелянш(у|и|ы)"
    hello = '(прив(і|е)т|ха(й|юшк(и|і))?|(з)?д(а|о)рова?),? бот'
