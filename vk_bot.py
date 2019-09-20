import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def write_msg(user_id, message, random_id):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})
    
# API-ключ созданный ранее
token = "Ваш токен"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
print("Server started")
keyboard = open("keyboard.json", "r", encoding = "UTF-8").read()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            
            print('New message:')
            print(f'For me by: {event.user_id}', end='')
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text),event.random_id)
            
            print('Text: ', event.text)
            
             
            
            vk.method('messages.send', {'user_id': event.user_id,'keyboard':keyboard, 'message': 'ыыы', 'random_id': 0})

            if event.text.lower() == 'саня':
                
                vk.method('messages.send', {'user_id': event.user_id, 'attachment':'photo144827456_457246174', 'message': 'ооо', 'random_id': 0})
            


