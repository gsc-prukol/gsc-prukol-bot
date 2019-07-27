class Messages:
    firstPhrase = 'А пошук не працює?'
    printing = "Друкують в 4-01 t.me/Froooger, t.me/Drectar, 0,75 грн/А4 (лише чб)"
    clinic = "Номери реєстратури: (044) 204-95-93 і (044) 204-85-62. Телефонуй їм."
    fullNameManager = 'Бушило Людмила Вікторівна'
    fullNameCastellansha = 'Білоцька Ірина Валентинівна'
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