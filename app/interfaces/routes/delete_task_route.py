from flask import Blueprint, request, jsonify
from flasgger import swag_from
from pydantic import ValidationError
from app.domain.services.task_service import (
    create_task_service,
    delete_all_tasks_service,
    list_tasks_service,
    get_task_service,
    update_task_service,
    delete_task_service,
)
from app.schemas.task_schema import TaskSchema, TaskUpdateSchema
from app.utils.messages import (
    TASK_CREATED,
    TASK_UPDATED,
    TASK_DELETED,
    ALL_TASKS_DELETED,
  
)
from app.utils.swagger_docs.task_docs import (
    create_task_doc,
    list_tasks_doc,
    get_task_doc,
    update_task_doc,
    delete_task_doc,
    delete_all_tasks_doc,
)

@swag_from(delete_task_doc)
def delete_task(task_id):
    try:
        delete_task_service(task_id)
        return jsonify({"message": TASK_DELETED}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500