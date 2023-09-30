import logging
from typing import Final
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN: Final = '5889078485:AAEe7G8zffK0ZVVBt0gQBcmi_yWm_zjZ7Yg'
BOT_USERNAME: Final = '@Status_GMT_Bot'
ADMIN_USER_ID: Final = 5355774833  # Admin's user ID

ASKING_EMAIL = "ASKING_EMAIL"
CONFIRM_EMAIL = "CONFIRM_EMAIL"
SENDING_MESSAGE = "SENDING_MESSAGE"
CANCEL_PENDING = "CANCEL_PENDING"
CONTACTING_ADMIN = "CONTACTING_ADMIN"

user_states = {}

logging.basicConfig(filename='user_data.log', level=logging.INFO, format='%(asctime)s - %(message)s')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_commands(message):
    

    bot.send_message(message.chat.id,'Appointment is available')

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Got it ✅', callback_data="2")
    keyboard.row(button)

    bot.send_message(message.chat.id, 'Please Click in below link:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_press(call):
    if call.data == "2":
        bot.send_message(call.message.chat.id, 'Please enter your email:')
        user_states[call.message.chat.id]["state"] = ASKING_EMAIL
    elif call.data.startswith("send_msg_to_"):
        user_id = call.data.replace("send_msg_to_", "")
        user_states[ADMIN_USER_ID] = {
            "state": SENDING_MESSAGE,
            "to_user_id": user_id,
        }
        bot.answer_callback_query(call.id)
        bot.send_message(ADMIN_USER_ID, 'Please enter the message you want to send to the user:')
    elif call.data == "confirm_email" and user_states.get(call.message.chat.id, {}).get("state") == CONFIRM_EMAIL:
        email = user_states[call.message.chat.id].get("email")

        user = call.message.chat.id
        log_text = f'User {user}, email: {email}'

        # Add this line to log the user data into user_data.log file
        logging.info(f'User Data: User ID = {user}, Email = {email}')


        keyboard = InlineKeyboardMarkup()
        button = InlineKeyboardButton('Reply to this user ✏️', callback_data=f"send_msg_to_{user}")
        keyboard.row(button)

        bot.send_message(chat_id=ADMIN_USER_ID, text=log_text, reply_markup=keyboard)

        keyboard = InlineKeyboardMarkup()
        button = InlineKeyboardButton('Go to Form 📝', url="https://online.forms.app/getmyterminde/registration-form")
        keyboard.row(button)

        bot.send_message(chat_id=call.message.chat.id, text='Now, press this button to go to the appointment details form and provide the required information', reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id)
    elif call.data == "edit_email" and user_states.get(call.message.chat.id, {}).get("state") == CONFIRM_EMAIL:
        bot.send_message(call.message.chat.id, 'Please enter your email again:')
        user_states[call.message.chat.id]["state"] = ASKING_EMAIL
        bot.answer_callback_query(callback_query_id=call.id)
    elif call.data == "confirm_cancel":
        user_id = call.message.chat.id
        user_states[user_id] = {
            "state": None,
            "email": None,
        }
        bot.send_message(user_id, 'Your appointment booking request has been cancelled successfully.')

        if user_id == ADMIN_USER_ID:
            bot.send_message(ADMIN_USER_ID, f'The admin has cancelled the appointment booking request.')
        else:
            bot.send_message(ADMIN_USER_ID, f'User with ID {user_id} has cancelled their appointment booking request.')

    elif call.data == "deny_cancel":
        user_id = call.message.chat.id
        bot.send_message(user_id, 'Continuing with your appointment booking request.')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if user_states.get(chat_id, {}).get("state") == ASKING_EMAIL:
        user_states[chat_id]["email"] = message.text
        user_states[chat_id]["state"] = CONFIRM_EMAIL
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton('Confirm ✅', callback_data="confirm_email")
        button2 = InlineKeyboardButton('Edit ✏️', callback_data="edit_email")
        keyboard.row(button1, button2)
        bot.send_message(chat_id, f'Do you confirm this email address: {message.text}', reply_markup=keyboard)
    elif user_states.get(chat_id, {}).get("state") == SENDING_MESSAGE:
        to_user_id = user_states[chat_id].get("to_user_id")
        bot.send_message(to_user_id, message.text)
        user_states[chat_id]["state"] = None
        bot.send_message(chat_id, 'Your message has been sent.')
    elif user_states.get(chat_id, {}).get("state") == CONTACTING_ADMIN:
        user_states[chat_id]["message"] = message.text
        user_states[chat_id]["state"] = None
        keyboard = InlineKeyboardMarkup()
        button = InlineKeyboardButton('Reply to this user ✏️', callback_data=f"send_msg_to_{chat_id}")
        keyboard.row(button)
        bot.send_message(ADMIN_USER_ID, f'User with ID {chat_id} sent this message:\n\n{message.text}', reply_markup=keyboard)
        bot.send_message(chat_id, 'Your message has been received and will be replied as soon as possible.')

bot.polling(none_stop=True, interval=0, timeout=20)
