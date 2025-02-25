import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('7443989414:AAHK5IfIeQurGfoSiRJc4-HpcIfMbh4FGdQ')
conn=sqlite3.connect("C:/BD/theater.db", check_same_thread=False)
cur = conn.cursor()

@bot.message_handler(commands=['start'])
def main_menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    infotheater = types.KeyboardButton("📄 Информация о театре")
    bilet = types.KeyboardButton("💸 Бронирование билетов")
    infospektakl = types.KeyboardButton("🗿 Информация о спектаклях")
    keyboard.add(infotheater, infospektakl, bilet)
    bot.send_message(message.chat.id, 'Привет, я чат-бот Самарского театра, выбери опцию из главного меню, если нужна помощь, напиши /help).', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🔙 Назад в главное меню"))
    helptext = """
📄 Информация о театре - узнать адрес, сайт театра.
💸 Бронирование билетов - бронирование билетов на сайте.
🗿 Информация о спектаклях - информация о ближайших спектаклях(цена билета, дата проведения).
"""
    bot.send_message(message.chat.id, helptext, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '📄 Информация о театре')
def info_theater(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🔙 Назад в главное меню"))
    info = """
🏫 <b>Театр</b>: Самарский академический театр драмы им. М. Горького.
📌 <b>Адрес</b>: г. Самара, ул. площадь Чапаева, д.1.
💻 <b>Сайт</b>: <a href="https://www.dramtheatre.ru/">Перейти на сайт</a>
🕛 <b>Режим работы</b>: Ежедневно с 12:00-19:00.
📱 <b>Основной номер телефона</b>: 8 (846) 333-33-48
🌍 <a href="https://yandex.ru/maps/51/samara/?ll=50.096445%2C53.197657&mode=poi&poi%5Bpoint%5D=50.096949%2C53.197448&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1205469783&z=17">Найти нас на карте</a>
"""
    bot.send_message(message.chat.id, info, parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '💸 Бронирование билетов')
def bron_bilet(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("🔙 Назад в главное меню"))
    info = """
💳<b>Купить билет</b>: <a href="https://www.dramtheatre.ru/events/">Перейти на сайт</a>
"""
    bot.send_message(message.chat.id, info, parse_mode='HTML', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '🗿 Информация о спектаклях')
def info_spec(message):
    seans_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    seans_menu.add('😢🎵 Два благородных дона','😂 Фредерик, или Бульвар преступлений', '🎭 Иммерсивная экскурсия «Игра в театр»', '😂 Шесть блюд из одной курицы', '😲 Вот так и живём', '✌ Амадеус',
'🎶 Алые паруса', '🐎 История лошади', '🐦 Полёт над гнездом кукушки', '😂💕 Корсиканка', '📃💿 НА ДНЕ.DOC', '😖 Мертвые души', "🔙 Назад в главное меню")
    bot.send_message(message.chat.id, 'Список ближайших сеансов:', reply_markup=seans_menu)

@bot.message_handler(func=lambda message: message.text == '🔙 Назад в главное меню')
def back(message):
    main_menu(message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "😢🎵 Два благородных дона":
        two_noble_dons = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 1').fetchone()
        if two_noble_dons:
            title, more_about_the_performance, time, duration, price, age_limit, image = two_noble_dons
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "😂 Фредерик, или Бульвар преступлений":
        frederik = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 2').fetchone()
        if frederik:
            title, more_about_the_performance, time, duration, price, age_limit, image = frederik
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "🎭 Иммерсивная экскурсия «Игра в театр»":
        immersivnaya = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 3').fetchone()
        if immersivnaya:
            title, more_about_the_performance, time, duration, price, age_limit, image = immersivnaya
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "😂 Шесть блюд из одной курицы":
        six = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 4').fetchone()
        if six:
            title, more_about_the_performance, time, duration, price, age_limit, image = six
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "😲 Вот так и живём":
        life = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 5').fetchone()
        if life:
            title, more_about_the_performance, time, duration, price, age_limit, image = life
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "✌ Амадеус":
        amadeus = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 6').fetchone()
        if amadeus:
            title, more_about_the_performance, time, duration, price, age_limit, image = amadeus
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "🎶 Алые паруса":
        parusa = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 7').fetchone()
        if parusa:
            title, more_about_the_performance, time, duration, price, age_limit, image = parusa
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "🐎 История лошади":
        horse = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 8').fetchone()
        if horse:
            title, more_about_the_performance, time, duration, price, age_limit, image = horse
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "🐦 Полёт над гнездом кукушки":
        kukushka = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 9').fetchone()
        if kukushka:
            title, more_about_the_performance, time, duration, price, age_limit, image = kukushka
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "😂💕 Корсиканка":
        korsianka = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 10').fetchone()
        if korsianka:
            title, more_about_the_performance, time, duration, price, age_limit, image = korsianka
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "📃💿 НА ДНЕ.DOC":
        dno = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 11').fetchone()
        if dno:
            title, more_about_the_performance, time, duration, price, age_limit, image = dno
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)

    elif message.text == "😖 Мертвые души":
        death = conn.execute('SELECT Название, Подробнее_о_спектале, Время_проведения, Продолжительность, Цена, Возрастное_ограничение, Изображение FROM Спектакли WHERE id == 12').fetchone()
        if death:
            title, more_about_the_performance, time, duration, price, age_limit, image = death
            response_message = f"🔹 Название: {title}\n📝 Подробнее о спектакле: {more_about_the_performance}\n🕒 Время проведения: {time}\n🔜 Продолжительность: {duration}\n💲 Цена: {price}\n🔞 Возрастное ограничение: {age_limit}"
            bot.send_photo(message.chat.id, image)
            bot.send_message(message.chat.id, response_message)
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю. Пожалуйста, выберите одну из доступных опций.")

bot.polling(none_stop=True, interval=0)