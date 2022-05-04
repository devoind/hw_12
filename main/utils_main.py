# Набор функций для views_main
import json
from exeptions import *


def load_json_data(path):
    """
    Функция загрузки json-файла

    :param path: принимает json-файла
    :return: возвращает загруженный json-файл в виде списка словарей
    """
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    """
    Функция поиска поста по ключевой фразе

    :param posts: получает полный список постов из json-файла
    :param substring: принимает от пользователя ключевую фразу дял поиска поста
    :return: возвращает найденные посты согласно ключевой фразе пользователя
    """
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)

    return posts_founded
