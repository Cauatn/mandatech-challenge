from flask import jsonify
from flasgger import swag_from
from app.domain.services.task_service import delete_all_tasks_service
from app.utils.messages import ALL_TASKS_DELETED
from app.utils.swagger_docs.task_docs import delete_all_tasks_doc


@swag_from(delete_all_tasks_doc)
def delete_all_tasks():
    """
    Endpoint para deletar todas as tarefas do banco de dados.

    Esse endpoint remove todas as tarefas existentes na coleção.

    Retorna:
        200: Todas as tarefas foram deletadas com sucesso.
        500: Erro interno inesperado durante a operação.
    """
    try:
        delete_all_tasks_service()
        return jsonify({"message": ALL_TASKS_DELETED}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
