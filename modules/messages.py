from modules.const import __version__
from modules.db import dataBaseMethods

DBMethods = dataBaseMethods( )

def scheduleInformation ( ):
    scheduleList = DBMethods.getScheduleList( )
    weekList = [ 'Понедельник: ', 'Вторник: ', 'Среда: ', 'Четверг: ', 'Пятница: ', 'Суббота: ' ]
    scheduled, schedule = [ ], [ ]
    for row in scheduleList:
        scheduled.append( schedule )
        schedule = [ ]
        for col in row:
            schedule.append( col )
    del scheduled[ 0 ]
    score = 0
    out = 'Рассписание 11Б\n'
    for dayAWeek in weekList:
        out += '\n' + str( dayAWeek ) + '\n'
        numOfLesson = 0
        for day in scheduled:
            numOfLesson += 1
            if day[ score ] == None:
                pass
            else:
                out += str( numOfLesson ) + '. ' + str( day[ score ] ) + '\n'
        score += 1
    return out


def scheduleCallsInformation ( ):
    scheduleList = DBMethods.getScheduleCallsList( )
    weekList = [ 'Расписание звонков: ', 'Время перемен: ' ]
    scheduled, schedule = [ ], [ ]
    for row in scheduleList:
        scheduled.append( schedule )
        schedule = [ ]
        for col in row:
            schedule.append( col )
    del scheduled[ 0 ]
    score = 0
    out = 'Рассписание звонков МАОУ СОШ №5 г.Туапсе\n'
    for dayAWeek in weekList:
        out += '\n' + str( dayAWeek ) + '\n'
        numOfLesson = 0
        for day in scheduled:
            numOfLesson += 1
            if day[ score ] == None:
                pass
            else:
                out += str( numOfLesson ) + '. ' + str( day[ score ] ) + '\n'
        score += 1
    return out


firstHello_1, firstHello_2 = "Ой, привет ", "! Вижу Ты тут в первые."
dev = "Функция уже в разработке, скоро станет доступна, осталось совсем чуть чуть :)"
whoMe = f"Привет🖐!\nЯ бот помощник 🤖, созданный специально для облегчения твоей жизни 😜❤\n\n✌ Бот-помощник SchoolSchedule\n✅ Версия -> {__version__}\n📑 Source code available on https://github.com/denbingon/schoolschedule\n📑 Автор -> https://vk.com/denbingon"
dontKnow = 'Не понимаю о чем Ты... Воспользуйся коммандой "помощь" и я расскажу Тебе что я умею!'

# [ "КТО ТЫ", "ДОБАВИТЬ", "УДАЛИТЬ", "РАСПИСАНИЕ УРОКОВ", "ЧТО НА ЗАВТРА", "ЧТО НА", "НАЧАТЬ", "ПОМОЩЬ", "РАСПИСАНИЕ ЗВОНКОВ" ]

help = '''Виу, виу, виу... Нужна помощь!

Тут описаны основные команды для управления мной :)

Для обычных пользователей:
"Кто ты" -> напиши мне эту команду и я расскажу Тебе о себе
"Расписание уроков" -> после этой команды я Тебе покажу расписание для 11Б класса МАОУ СОШ№5 г.Туапсе
"Расписание звонков" -> тоже еще одно расписание, но теперь звонков для всех классов школы
"Начать" -> выполняя эту команду я запоминаю как тебя зовут, если Ты по каким то не известным причинам изменишь имя то используй данную команду
"Что на завтра" -> тут все предельно легко, я Тебе скажу какую домашнюю работу задали на завтра и какие ожидаются мероприятия
"Что на" -> такая же как и предыдущая команда только теперь я буду ждать от тебя число на которое Ты хочешь узнать информацию
"Помощь" -> ну собственно функционал данной команды Ты наблюдаешь прямо сейчас


Для супер-пользователей:
//Выполнение данных команд имеет возможность ограниченный круг лиц 
Системные:
"Выполнить SQL запрос" -> после выполнения ожидает любой правильно составленный SQL запрос, если вывода нету то возвращает Done! 
"Получить данные о загруженности системы" -> возвращает данные о работе машины на которой установлен бот
"Время работы без сбоев" -> выводит время работы скрипта от последнего перезапуска

Редактирующие:
"Добавить" -> данная команда позволяет добавить Д/З или событие
"Удалить" -> данная команда позволяет удалить Д/З или событие

//Все запросы ниже пишутся слитно
Для добавления следует составить запрос следующего содержания: дата фомата чч.мм.гггг / предмет или событие / подробности
Для удаления следует составить запрос следующего содержания: номер записи

Ну что ж... Вот и все, краткий гайд по мне подошел к концу, надеюсь я смог разъяснить твою проблему, если же нет то обращайся к https://vk.com/denbingon/, он то Тебе точно поможет!
Приятного пользования мной! Хорошего дня!
'''
