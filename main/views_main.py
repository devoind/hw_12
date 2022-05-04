from flask import render_template, Blueprint, request
import logging
from main.utils_main import *
from config import POST_PATH
from exeptions import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    """
    Функция для формирования Главной страницы по шаблону index.html

    :return: возвращает страницу по шаблону index.html
    """
    logging.info("Открытие главной станицы")  # Запись события в журнал
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    """
    Функция поиска поста по ключевым фразам

    :return: возвращает страницу с найденными постами по шаблону post_list.html
    """
    s = request.args.get("s", "")
    logging.info("Выполняется поиск")  # Запись события в журнал

    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"

    file_post = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=file_post, s=s)
