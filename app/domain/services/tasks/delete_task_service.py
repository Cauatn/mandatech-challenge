from flask import jsonify
from flasgger import swag_from
from app.domain.services.task_service import delete_task_service
from app.utils.messages import TASK_DELETED
from app.utils.swagger_docs.task_docs import delete_task_doc

@swag_from(delete_task_doc)
def delete_task(task_id):
    """
    Endpoint para deletar uma tarefa pelo ID.

    Params:
        _id (str): ID da tarefa a ser deletada.

    Retorna:
        200: Tarefa deletada com sucesso.
        404: Tarefa não encontrada.
        500: Erro interno inesperado.
    """
    try:
        delete_task_service(task_id)
        return jsonify({"message": TASK_DELETED}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500