from flask import Flask
from flasgger import Swagger
from app.interfaces.controllers.task_controller import task_bp

def create_app():
    app = Flask(__name__)
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "API de Gerenciamento de Tarefas",
            "description": "API RESTful para criar, listar, editar e deletar tarefas",
            "version": "1.0"
        },
        "basePath": "/tasks"
    })
    app.register_blueprint(task_bp, url_prefix="/tasks")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",debug=True)