

from num2words.lang_PL import prefixes
from win32comext.mapi.mapiutil import prTable

print('starting UserBot')
print('Importing LIBs')
from token import COMMA
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import ChatMemberUpdated
print('pyrogram imported')

from btgid import *
print('BTGID library imported')

import json
print('json imported')
from datetime import datetime
print("datetime imported")
from time import sleep
print('time imported')
import random
print('random imported')
import json
print('json imported')
import os
print('os imported')


print('all LIBs imported')

print('setting API')
api_id = 22660596
api_hash = '618ce57e693769bf31dfe48a7bc8b3c9'



Users = {}

app = Client("my_account", api_id=api_id, api_hash=api_hash)

i = 0

zmode = False


print('def settings')

def Turn_On():
    global Pc_Working
    Pc_Working = True


def Turn_Off():
    global  Pc_Working
    Pc_Working = False


def LoadDB():
    with open('UserbotDATA.txt', 'r') as file:
        global Database
        Database = file.read()

        Database = json.loads(Database)
        print('db loaded')
        print("in Database:", Database)

    return Database

def SaveDB():
    with open("UserbotDATA.txt", 'w', encoding='utf-8') as filer:
        filer.write('')
        filer.write(json.dumps(Database, ensure_ascii=False))

    return 1

LoadDB()

print('try-except construction ready')

try:
    LoadBTGID()
    #Эхо
    '''@app.on_message(filters.me)
    def echo(client, message):
        message.reply_text(message.text)'''



    

    '''@app.on_message(filters.command('ставка', prefixes='.') & filters.me)
    def stavka(_, msg):
        userid = str(msg.from_user.id)
        UserInfo = Users.get(userid)
        print(UserInfo)
        UserCash = UserInfo.get("cash")
        print(UserCash)

        stavnum = msg.text.split('.ставка ', maxsplit=1)[1]
        x = random.randint(0.0, 10.0)
        print(x)
        xdiv = x / 10
        print(xdiv)
        for i in range(x+1):
            sleep(0.3)
            i + xdiv
            print(i)
            msg.edit(f'Ваш ИКС - x{i}. Ставка: {stavnum}')
            result = i
        win = UserCash * result
        print(win)
        msg.edit(f'Финальный икс - {result}\nСтавка: {stavnum}\nВыигрыш: {win}')

        UserInfo["cash"] = win
        print(UserCash)'''

    @app.on_message(filters.command('любовь', prefixes='.') & filters.me)
    def iloveu(_, msg):
        times = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        sleep(random.choice(times))
        msg.edit('👨‍💻|❤️🖤🖤🖤🖤|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|❤️❤️🖤🖤🖤|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|❤️❤️❤️🖤🖤|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|❤️❤️❤️❤️🖤|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|❤️❤️❤️❤️❤️|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('🔍|🖤🖤🖤🖤🖤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|❤️🖤🖤🖤🖤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|❤️❤️🖤🖤🖤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|❤️❤❤️🖤🖤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|❤️❤️❤❤🖤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|❤️❤❤️❤️❤|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('✅|🖤🖤🖤🖤🖤|Информация найдена!')
        sleep(random.choice(times))
        msg.edit('✅|❤️🖤🖤🖤🖤|Готовлюсь к отправке...')
        sleep(random.choice(times))
        msg.edit('✅|❤️❤🖤🖤🖤|Собираю архивы...')
        sleep(random.choice(times))
        msg.edit('✅|❤️❤️❤🖤🖤|Жую жвачку...')
        sleep(random.choice(times))
        msg.edit('✅|❤️❤❤️❤🖤|Запечатываю письмо...')
        sleep(random.choice(times))
        msg.edit('✅|❤️❤️❤❤️❤|Отправляю...')
        sleep(2)
        msg.edit('я тебя люблю!')


    
    @app.on_message(filters.command('пентагон', prefixes='.') & filters.me)
    def pentagon(_, msg):
        times = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        sleep(random.choice(times))
        msg.edit('👨‍💻|🟢🔴🔴🔴🔴|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|🟢🟢🔴🔴🔴|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|🟢🟢🟢🔴🔴|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|🟢🟢🟢🟢🔴|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('👨‍💻|🟢🟢🟢🟢🟢|Взлом пентагона')
        sleep(random.choice(times))
        msg.edit('🔍|🔴🔴🔴🔴🔴|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|🟢🔴🔴🔴🔴|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|🟢🟢🔴🔴🔴|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|🟢🟢🟢🔴🔴|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|🟢🟢🟢🟢🔴|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('🔍|🟢🟢🟢🟢🟢|Поиск информации о тебе')
        sleep(random.choice(times))
        msg.edit('✅|🔴🔴🔴🔴🔴|Информация найдена!')
        sleep(random.choice(times))
        msg.edit('✅|🟢🔴🔴🔴🔴|Готовлюсь к отправке...')
        sleep(random.choice(times))
        msg.edit('✅|🟢🟢🔴🔴🔴|Собираю архивы...')
        sleep(random.choice(times))
        msg.edit('✅|🟢🟢🟢🔴🔴|Жую жвачку...')
        sleep(random.choice(times))
        msg.edit('✅|🟢🟢🟢🟢🔴|Запечатываю письмо...')
        sleep(random.choice(times))
        msg.edit('✅|🟢🟢🟢🟢🟢|Отправляю...')
        sleep(2)
        msg.edit('я хз че сюда написать, тут пентагон был')


    @app.on_message(filters.command('меняобидели', prefixes='.') & filters.all)
    def obid(_, msg):
        app.send_message(chat_id=msg.chat.id, text='не обижайся, возьми шоколадку 👉🍫')

    @app.on_message(filters.command('type', prefixes='.') & filters.me)
    def type(_, msg):
        orig_text = msg.text.split('.type ', maxsplit=1)[1]
        print(orig_text)
        text = orig_text
        ToBePrinted = ""
        typing_symbols = ['-', '!', '#', '*', '+']
        while(ToBePrinted != orig_text):
            try:
                msg.edit(ToBePrinted + random.choice(typing_symbols))
                sleep(0.1)

                ToBePrinted = ToBePrinted + text[0]
                text = text[1:]

                msg.edit(ToBePrinted)
                sleep(0.1)
            except FloodWait as e:
                sleep(e.x)

    @app.on_message(filters.command('арсен', prefixes='.') & filters.all)
    def arsen(_, msg):
        app.send_photo(chat_id=msg.chat.id, photo='arsen.jpg')

    @app.on_message(filters.command('btgid'.lower(), prefixes='.') & filters.all)
    def btgidinfo(_, msg):
        app.send_photo(chat_id=msg.chat.id, photo='BTGIDlogo.PNG', caption='BTGID - встроенная система ID в юзербота.\nдля того чтобы узнать ваш BTGID или создать его отправьте .myBTG')

    @app.on_message(filters.command('updatebordid'.lower(), prefixes='-') & filters.me)
    def update_bordid(_, msg):
        UpdateBordID()

    @app.on_message(filters.command('ban'.lower(), prefixes='.') & filters.me)
    def ban(_, msg):
        ban_target = msg.text.split()[1]

        LoadBTGID()
        User = BTGIDs.get(str(ban_target))
        User['status'] = "Banned"
        UserName = User.get('name')
        app.send_message(chat_id=msg.chat.id,
                             text=f'Пользователь {UserName}, забанен.')
        SaveBTGID()


    @app.on_message(filters.command('unban'.lower(), prefixes='.') & filters.me)
    def ban(_, msg):
        ban_target = msg.text.split()[1]

        LoadBTGID()
        User = BTGIDs.get(str(ban_target))
        User['status'] = "Active"
        UserName = User.get('name')
        app.send_message(chat_id=msg.chat.id,
                         text=f'Пользователь {UserName}, разбанен.')
        SaveBTGID()


    @app.on_message(filters.command('mybtg'.lower(), prefixes='.') & filters.all)
    def UserBTG(_, msg):
        global BTGIDs, Status_msg

        mybtg_com = msg.text.split(maxsplit=2)
        print(mybtg_com)
        usertgid = msg.from_user.id
        print("mybtg_com0:", mybtg_com[0])
        try:
            if mybtg_com[1] == 'help':
                app.send_message(chat_id=msg.chat.id, text=f'.mybtg name "Имя" - изменить ваш никнейм\n.\nmybtg help - вызвать помощь по .mybtg\n\n.mybtg transactions - помощь в транзакциях BordCoins')

            if mybtg_com[1] == 'transactions':
                app.send_message(chat_id=msg.chat.id,
                                     text=f'BordCoins - внутренняя валюта ЮзерБота, используемая для покупки предметов внутри бота.\n\nBordCoins начисляются один раз в сутки по команде .Ферма (Сейчас недоступно)')

            if mybtg_com[1] == 'name':
                if mybtg_com[2] == '':
                    app.send_message(chat_id=msg.chat.id,
                                     text=f'[MYBTG-NAME-ERROR] Поле <ИМЯ> отсутствует')
                else:
                    BTGIDs = LoadBTGID()
                    User = GetUser(usertgid)
                    User['name'] = mybtg_com[2]
                    SaveBTGID()
                    app.send_message(chat_id=msg.chat.id,
                                     text=f'Ваше имя изменено на "{mybtg_com[2]}"')

                    
        except IndexError:

            usertgid = msg.from_user.id
            BTGIDs = LoadBTGID()
            user = GetUser(usertgid)
            if user == None:
                userbtgid = msg.from_user.id
                name = msg.from_user.first_name
                CreateUser(usertgid, name, userbtgid)
                SaveBTGID()
                app.send_message(chat_id=msg.chat.id, text=f'Ваш BTGID создан успешно! чтобы узнать его, пропиши еще раз .mybtg')

            else:
                Awards_String = ""
                User = GetUser(usertgid)
                Name = User.get('name')
                btgid = User.get('BTGID')
                AccountStatus = User.get('status')
                Awards = User.get('Awards')
                Coins = User.get('BordCoins')
                if AccountStatus == 'Active':
                    Status_msg = 'Активен'
                if AccountStatus == 'Banned':
                    Status_msg = 'ЗАБАНЕН.'
                SplittedAwards = Awards.split()
                AwardsCount = len(SplittedAwards)
                for i in range(AwardsCount):
                    if SplittedAwards[i] == 'Bashmaaward1':
                        Awards_String = Awards_String + "🥇 Участник Башмачишек 1 сезон\n"
                    if SplittedAwards[i] == 'Bashmaaward2':
                        Awards_String = Awards_String + "🥇 Участник Башмачишек 2 сезон\n"
                    if SplittedAwards[i] == 'Bashmaaward3':
                        Awards_String = Awards_String + "🥇 Участник Башмачишек 3 сезон\n"
                    if SplittedAwards[i] == 'Father':
                        Awards_String = Awards_String + "🥇 Отец владельца ЮзерБота <3\n"
                
                app.send_message(chat_id=msg.chat.id, text=f'Ваш BTGID:\n\nИмя: {Name}\nСтатус вашего аккаунта: {Status_msg}\nВаш BTGID: {btgid}\n\nВаши BordCoins: {Coins}\n\nВаши награды:\n{Awards_String}\n\nдля уточнения полноценной ветки команд mybtg - пропишите ".mybtg help"')

    @app.on_message(filters.command('Reward', prefixes='.') & filters.me)
    def Reward(_, msg):
        reward_com = msg.text.split(maxsplit=3)
        print(reward_com)
        BTGIDs = LoadBTGID()
        usertgid = reward_com[1]
        user = GetUser(usertgid)
        print(user)
        if reward_com[2] == 'Башмачишки':
            if reward_com[3] == '1':
                Awards = user.get('Awards')
                AwardEdit = Awards + "Bashmaaward1 "
                user['Awards'] = AwardEdit
                SaveBTGID()
                app.send_message(chat_id=msg.chat.id, text=f"{user.get('name')} награжден(-a) наградой\nУчастник Башмачишек 1 сезон!\n\nПоздавляем! Наши апплодисменты!")
                
            if reward_com[3] == '2':
                Awards = user.get('Awards')
                print("User OLD Awards:", Awards)
                AwardEdit = Awards + "Bashmaaward2 "
                user['Awards'] = AwardEdit
                SaveBTGID()
                print(AwardEdit)
                app.send_message(chat_id=msg.chat.id, text=f'{user.get("name")} награжден(-a) наградой\nУчастник Башмачишек 2 сезон!\n\nПоздавляем! Наши апплодисменты!')
            if reward_com[3] == '3':
                Awards = user.get('Awards')
                print("User OLD Awards:", Awards)
                AwardEdit = Awards + "Bashmaaward3 "
                user['Awards'] = AwardEdit
                SaveBTGID()
                print(AwardEdit)
                app.send_message(chat_id=msg.chat.id, text=f'{user.get("name")} награжден(-a) наградой\nУчастник Башмачишек 3 сезон!\n\nПоздавляем! Наши апплодисменты!')
        if reward_com[2] == 'Папа':
            Awards = user.get('Awards')
            print("User OLD Awards:", Awards)
            AwardEdit = Awards + "Father "
            user['Awards'] = AwardEdit
            SaveBTGID()
            print(AwardEdit)
            app.send_message(chat_id=msg.chat.id, text=f'{user.get("name")} награжден(-a) наградой\nОтец владельца ЮзерБота <3!\n\nПоздавляем! Наши апплодисменты!')


    @app.on_message(filters.command('мяу', prefixes='.') & filters.all)
    def asjdokas(_, msg):
        print(msg)


    @app.on_message(filters.command('stop', prefixes='-') & filters.me)
    def stop(_, msg):
        msg.edit('-stop\nSaving data...')
        saving = SaveDB()
        if saving == 1:
            msg.edit('-stop\nSaving data...ok\nStopping code...')
            msg.edit('-stop\nSaving data...ok\nStopping code...ok')
            exit()
        else:
            msg.edit('-stop\nSaving data...ERROR\nCode cant save Database. please exit from code at your PC!')
            

    @app.on_message(filters.command('котенок', prefixes='.') & filters.all)
    def cat1(_, msg):
        global i
        if i == 9:
            i = 0
        cat = ['https://fanibani.ru/wp-content/uploads/2022/12/407444-svetik.jpg',
               'https://funik.ru/wp-content/uploads/2018/10/f1fda080713507f02387.jpg',
               'https://wdorogu.ru/images/wp-content/uploads/2020/10/feda8bbd51ff950-scaled.jpg',
               'https://ferret-pet.ru/wp-content/uploads/c/1/2/c12c20199d1c00a5a3be6e0112c1cc7e.jpeg',
               'https://damion.club/uploads/posts/2022-01/1642765171_46-damion-club-p-zhivie-kotyata-47.jpg',
               'https://krasivosti.pro/uploads/posts/2021-03/1616455815_23-p-kotiki-milashki-foto-koshka-26.jpg',
               'https://gas-kvas.com/grafic/uploads/posts/2023-10/1696601499_gas-kvas-com-p-kartinki-s-kotenkom-17.jpg',
               'https://masyamba.ru/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BA%D0%BE%D1%82%D1%8F%D1%82/72-%D0%BC%D0%B8%D0%BB%D1%8B%D0%B9-%D0%BA%D0%BE%D1%82%D0%B5%D0%BD%D0%BE%D0%BA.jpg',
               'https://chudo-prirody.com/uploads/posts/2021-08/1628637685_144-p-kotyata-milie-foto-155.jpg']
        cat_num = cat[i]
        if cat_num == cat[0]:
            print('HE IS!!')
        print(cat_num)
        app.send_photo(chat_id=msg.chat.id, photo=cat_num)
        i += 1

    @app.on_message(filters.command('котёнок', prefixes='.') & filters.all)
    def cat2(_, msg):
        global i
        if i == 9:
            i = 0
        cat = ['https://fanibani.ru/wp-content/uploads/2022/12/407444-svetik.jpg',
               'https://funik.ru/wp-content/uploads/2018/10/f1fda080713507f02387.jpg',
               'https://wdorogu.ru/images/wp-content/uploads/2020/10/feda8bbd51ff950-scaled.jpg',
               'https://ferret-pet.ru/wp-content/uploads/c/1/2/c12c20199d1c00a5a3be6e0112c1cc7e.jpeg',
               'https://damion.club/uploads/posts/2022-01/1642765171_46-damion-club-p-zhivie-kotyata-47.jpg',
               'https://krasivosti.pro/uploads/posts/2021-03/1616455815_23-p-kotiki-milashki-foto-koshka-26.jpg',
               'https://gas-kvas.com/grafic/uploads/posts/2023-10/1696601499_gas-kvas-com-p-kartinki-s-kotenkom-17.jpg',
               'https://masyamba.ru/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BA%D0%BE%D1%82%D1%8F%D1%82/72-%D0%BC%D0%B8%D0%BB%D1%8B%D0%B9-%D0%BA%D0%BE%D1%82%D0%B5%D0%BD%D0%BE%D0%BA.jpg',
               'https://chudo-prirody.com/uploads/posts/2021-08/1628637685_144-p-kotyata-milie-foto-155.jpg']
        cat_num = cat[i]
        if cat_num == cat[0]:
            print('HE IS!!')
        print(cat_num)
        app.send_photo(chat_id=msg.chat.id, photo=cat_num)
        i += 1

    @app.on_message(filters.command('командыЮБ', prefixes='.') & filters.all)
    def commands(_, message):
        app.send_message(chat_id=message.chat.id, text='Команды Юзер Бота:\n\nОбщедоступные:\n\n.котенок (или котёнок) - показывает картинку случайного котенка\n ?ЮзерБот - отправляет инфу о боте.\n.BTGID - встроенная система ID в юзербота. Находится в бета тесте!\n\nТолько для владельца ЮзерБота:\n\n.пентагон - просто анимация\n.type - красиво выводит текст\n.спам <Число сообщений> <текст> - спам')

    @app.on_message(filters.command('спам', prefixes='.') & filters.me)
    def spam(_, message):
        spam_com = message.text.split('.спам ', maxsplit=1)[1]
        spam_command = spam_com.split(maxsplit=1)
        print(spam_command)
        spam_strnum = spam_command[0]
        spam_num = int(spam_strnum)
        spam_text = spam_command[1]
        for i in range(0, spam_num):
            app.send_message(chat_id=message.chat.id, text=f'{spam_text}')

    @app.on_message(filters.command('console', prefixes='-') & filters.me)
    def console(_, msg):
        msg.edit('-console\n\nconsole started.')
        cons_inp = input('console >>')
        cons_inp_spl = cons_inp.split()
        if cons_inp_spl[0] == 'Status':
            if cons_inp_spl[1] == 'code-edit':
                Database["status"] = 'Code_Edit'
                SaveDB()
                print('sucess')
                
            if cons_inp_spl[1] == 'work':
                Database["status"] = 'Working'
                SaveDB()
                print('sucess')

        msg.edit('-console\n\nconsole closed.')


    @app.on_message(filters.command('Юзербот', prefixes='?') & filters.all)
    def info(_, message):
        DB = LoadDB()
        print(DB)
        stat = DB.get('status')
        version = DB.get('version')
        print(stat)
        if stat == 'Code_Edit':
            result = 'Сейчас над кодом Юзербота ведутся работы. могут наблюдатся небольшие сбои'
        if stat == 'Working':
            result = 'Бот работает в штатном режиме.'
        app.send_message(message.chat.id, text=f'ЮзерБот Швабадабаду.'
                                               '\nЮзербот написан на языке Python'
                                               f'\nВерсия бота: {version}'
                                               '\nКоманды Юзербота вы можете узнать по команде .КомандыЮБ'
                                               f'\n\nСтатус работы: {result}')

        
    @app.on_message(filters.linked_channel & filters.chat(-1001700202759))
    def camel_channel(_, msg):
        kamel_msgs = ['ого камиль пост выкатил', 'Камиль, ждем тебя в РФ на сходку', 'Камиль, как дела?', 'Камиль, дай ссылку на веб кирюше', 'Камиль, это ты?']
        ready = random.choice(kamel_msgs)
        app.send_message(msg.chat.id, text=ready, reply_to_message_id=msg.id)



except:
    None

else:


    @app.on_message(filters.text)
    def auto(_, message):

        if message.text.lower() == 'бот':
            app.send_message(chat_id=message.chat.id, text='ЮзерБот Швабадабаду на месте! 💥')

        if message.text.lower() == 'press f':
            app.send_message(chat_id=message.chat.id, text='F')







print('bot started!')

app.run()
