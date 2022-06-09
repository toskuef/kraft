from vk_api.bot_longpoll import VkBotEventType

from .services.services import Vkontakte
from .views import CustomerDetail
from django.shortcuts import render

def main():
    for event in Vkontakte().get_vk_listener_group():
        print(event)

main()



