from flask import request, jsonify
from flasgger import swag_from
from pydantic import ValidationError
from app.domain.services.task_service import create_task_service
from app.domain.schemas.task_schema import TaskSchema
from app.utils.messages import TASK_CREATED
from app.utils.swagger_docs.task_docs import create_task_doc

@swag_from(create_task_doc)
def create_task():
    """
    Endpoint para criação de uma nova tarefa.

    Objeto JSON:
    {
        "title": "string",          # obrigatório
        "description": "string",    # opcional
        "status": "pending",        # obrigatório: 'done', 'in_progress' ou 'pending'
        "owner": "string"           # obrigatório
    }

    Retorna:
        201: Tarefa criada com sucesso, retorna ID.
        400: Erro de validação nos dados enviados.
        500: Erro interno inesperado.
    """
    try:
        task_data = TaskSchema(**request.json).model_dump()
        task_id = create_task_service(task_data)
        return jsonify({"message": TASK_CREATED, "id": task_id}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500