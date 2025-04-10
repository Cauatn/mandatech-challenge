from flask import jsonify
from flasgger import swag_from
from app.domain.services.task_service import get_task_service
from app.utils.swagger_docs.task_docs import get_task_doc
    

@swag_from(get_task_doc)
def get_task(task_id):
    """
    Endpoint para buscar uma tarefa pelo ID.

    Params:
        task_id (str): ID da tarefa a ser recuperada.

    Retorna:
        200: Tarefa encontrada e retornada com sucesso.
        404: Tarefa não encontrada no banco.
        500: Erro interno inesperado.
    """
    try:
        task = get_task_service(task_id)
        return jsonify(task), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500