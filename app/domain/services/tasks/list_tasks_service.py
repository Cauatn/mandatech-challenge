from flask import request, jsonify
from flasgger import swag_from
from app.domain.services.task_service import list_tasks_service
from app.utils.swagger_docs.task_docs import list_tasks_doc

@swag_from(list_tasks_doc)
def list_tasks():
    """
    Endpoint para listar todas as tarefas.

    Query Params:
        status (str, opcional): Filtra as tarefas por status ("pending", "done", "in_progress").

    Retorna:
        200: Lista de tarefas (filtrada ou completa).
        500: Erro interno inesperado.
    """
    try:
        status = request.args.get("status")
        tasks = list_tasks_service(status)
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500