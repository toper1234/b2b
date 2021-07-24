import settings
import telebot
from telebot import types

buy_access = '❕ Покупка доступа\n\n' \
             '🥝 Оплата qiwi:\n\n' \
             f'❕ Номер:     {settings.QIWI_NUMBER}\n' \
             f'❕ Сумма:     {settings.ACCESS_COST} руб\n' \
             '❕ Комментарий:    {code}\n \n' \
             '❕ Пополнение с карты: https://qiwi.com/payment/form/99?amountFraction=0&extra%5B%27comment%27%5D={code}&extra%5B%27account%27%5D=%2B79519089164&amountInteger=50&currency=643&blocked[0]=sum&blocked[1]=account&blocked[2]=comment'
          


kak_karta = 'привет'


start_menu = 'Здравствуйте, {name}\n' \
        '🏅Ваш id - {id}\n' \
        '🧑‍💻Вы находитесь в меню:\n\n' \
        '💬Наш чат - https://t.me/black2box_chat'


admin_menu = 'Здравствуйте, {name}\n' \
             'Вы находитесь в меню админа: '


profile = '📰 Профиль\n\n' \
          'Ваше имя - {name}\n' \
          'Ваш id - {id}\n' \
          'Доступ - {access}'


access_no_info = '❕ Информация о Black2Box\n\n' \
                 '💥 Black2Box имеет 3-х уровневаю систему\n' \
                 '💥 Оплачивая доступ вы получаете личную ссылку для приглашения пользователей\n' \
                 f'💥 За каждого пригл. пользователя который оплатил доступ вы получаете {settings.PERCENT_1 * 100} % от оплаты\n' \
                 f'💥 За каждого пригл. им пользователя вы получаете {settings.PERCENT_2 * 100} % от оплаты\n' \
                 f'💥 Далее {settings.PERCENT_3 * 100} % от оплаты\n' \
                 f'💥 Пригласив всего 1 активного пользователя вы можете получить более 100 тысяч рублей!!'


access_yes_info = '⚠️ Информация\n\n' \
                  '❕ Ваш реф. код - {ref_code}\n' \
                  '❕ Ваша реф. ссылка - {ref_url}\n\n' \
                  '💰 Ваш заработок - {profit} руб\n' \
                  '👥 Кол-во приглашенных людей - {amount_invite_users}'


support = 'Если у вас есть вопрос/проблема напишите:\n\n' \
          '@UPCENTS'


admin_profit = '💰 Прибыть за все время составила - {} рублей'


admin_info = 'Общая информация\n\n' \
             'Всего уникальных пользователей - {users}\n' \
             'Кол-во людей оплативших доступ - {deposit}\n'


order_payment = 'Запрос на вывод\n\n' \
                'ID запроса - {}\n' \
                'User_id - {}\n' \
                'Имя - {}\n' \
                'Сумма - {}\n' \
                'Дата - {}\n' \
                'QIWI - {}'


withdraw = '⚠️ Запрос выплаты\n\n' \
           '❕ Ваш баланс - {} руб\n' \
           f'❕ Мин. сумма выплаты - {settings.MIN_PAYOUT} руб\n\n' \
           '❕ Введите сумму которую хотите вывести: \n\n' \
           f'❗️ Например: 500 или 764.34'

