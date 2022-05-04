# Набор функций для views_loader

import json
from config import POST_PATH, UPLOAD_FOLDER
from exeptions import *


def save_image(picture):
    """
    Функция сохранения изображения

    :param picture: получает изображение от пользователя
    :return: возвращает ссылку на изображение
    """
    format_list = ["jpeg", "jpg", "png"]
    picture.type = picture.filename.split(".")[-1]
    if picture.type not in format_list:
        raise WrongImageType(f"Неверный формат файла! Допустимые форматы: {', '.join(format_list)}")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    """
    Функция добавление поста
    :param post_list: добавление нового поста к имеющимся
    :param post: новый пост
    :return: ничего не возвращет
    """
    post_list.append(post)
    with open(POST_PATH, 'w', encoding="UTF-8") as file:
        json.dump(post_list, file)
