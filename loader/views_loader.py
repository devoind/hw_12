from flask import render_template, Blueprint, request
import logging
from main.utils_main import *
from loader.utils_loader import *
from config import POST_PATH

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET"])
def create_new_post_page():
    """
    Функция добавления поста по шаблону post_form.html
    :return: возвращает страницу по шаблону post_form.html
    """
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def create_new_post_by_user():
    """
    Функция создания нового поста по шаблону post_uploaded.html
    :return: возвращает новый пост по шаблону post_uploaded.html
    """
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены или отсутствует часть данных")  # Запись в журнал
        return "Отсутствует часть данных!"

    posts = load_json_data(POST_PATH)

    try:
        new_post = {"pic": save_image(picture), "content": content}
    except WrongImageType:
        logging.info("Загруженный файл - не картинка")  # Запись в журнал
        return "Неверный тип или забыли загрузить изображение!"

    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)
