from flask import request, jsonify
from flasgger import swag_from
from pydantic import ValidationError
from app.domain.services.task_service import update_task_service

from app.domain.schemas.task_schema import TaskUpdateSchema
from app.utils.messages import TASK_UPDATED
  
from app.utils.swagger_docs.task_docs import update_task_doc

@swag_from(update_task_doc)
def update_task(task_id):
    """
    Endpoint para atualizar uma tarefa pelo ID.

    Params:
        _id (str): ID da tarefa a ser atualizada.

    JSON:
        - "title": Novo título (opcional)
        - "description": Nova descrição (opcional)
        - "status": Novo status, pode ser "pending", "done", ou "in_progress" (opcional)
        - Alternativamente, pode-se usar "in_progress": true/false ou "done": true/false

    Regras:
        - Se enviado "in_progress" ou "done", o campo "status" será definido automaticamente.
        - Caso contrário, será utilizado o esquema padrão de atualização.

    Retorna:
        200: Tarefa atualizada com sucesso.
        400: Erro de validação nos dados enviados.
        404: Tarefa não encontrada.
        500: Erro interno inesperado.
    """
    try:
        json_data = request.json or {}
        update_data = {}
        
        # Caso seja enviado no body da requisição "in_progress":
        if "in_progress" in json_data:
            update_data["status"] = "in_progress" if json_data["in_progress"] else "pending"
        # Caso seja enviado "done", trata esse caso:
        elif "done" in json_data:
            update_data["status"] = "done" if json_data["done"] else "pending"
        else:
            # Se nada for enviado, utiliza o esquema padrão para outros campos.
            update_data = TaskUpdateSchema(**json_data).model_dump(exclude_none=True)
        
        update_task_service(task_id, update_data)
        return jsonify({"message": TASK_UPDATED}), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500