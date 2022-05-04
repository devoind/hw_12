from flask import Flask, send_from_directory
from main.views_main import main_blueprint
from loader.views_loader import loader_blueprint

ensure_ascii = False

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    Функция отправляет файл path из каталога uploads

    :param path: модификатор маршрута, позволяет положить в переменную path не один сегмент URL,
    а сразу весь путь, который написан после uploads
    :return: возвращает клиенту запрошенный файл при указании папки uploads
    """
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
