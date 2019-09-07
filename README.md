<h1> Бот для VK на Python</h1>
Пример простого бота для ВКонтакте на Python 3. Обработка событий с использованием Bots Long Poll API.

<h2>Подготовка к использованию</h2>

<h3>Установка библиотек</h3>
<p><code>pip3 install vk requests</code></p>
<h3>Получение ключа доступа VK API</h3>
<p>
Ключ доступа к VK API можно получить в настройках сообщества, там же нужно 
<strong> включить Long Poll API</strong> 
, как минимум для доступа к сообщениям и управления сообществом.
<a>
<p>
<img src="https://camo.githubusercontent.com/5fd4079a1c460e12491a906e9710e89ed3b45642/68747470733a2f2f692e696d6775722e636f6d2f306f75785737422e706e67">
</p>
</a>
</p>
<p>
Сделать это можно перейдя в "Управление сообществом" -> "Работа с API" -> "Ключи доступа", "Long Poll API".
<p>

<h3> Запуск бота</h3>
<p>Получив API-токен прописываем его после импорта библиотек:
</p>
<a><code>
<a>import requests</a>
<a>import bs4</a>
<a>import urllib.request</a>
<a>import re</a>
<a>from datetime import datetime</a>
<a>token = "Полученный токен"</a>
<a>class VkBot:</a>

</code></a>

