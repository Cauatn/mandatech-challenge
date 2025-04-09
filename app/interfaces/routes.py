from flask import Blueprint, request, jsonify
from flasgger import swag_from
from pydantic import ValidationError
from app.application.task_service import (
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
    TASK_NOT_FOUND,
    INVALID_DATA,
)

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        # Usa o modelo JSON gerado pelo Pydantic como schema
        'schema': TaskSchema.model_json_schema()
    }],
    'responses': {
        201: {'description': TASK_CREATED},
        400: {'description': INVALID_DATA}
    }
})
def create_task():
    try:
        task_data = TaskSchema(**request.json).model_dump()
        task_id = create_task_service(task_data)
        return jsonify({"message": TASK_CREATED, "id": task_id}), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [{
        'name': 'status',
        'in': 'query',
        'type': 'string',
        'required': False,
        'description': "Filtrar tarefas pelo status (done, in_progress, pending)"
    }],
    'responses': {
        200: {'description': "Lista de tarefas"}
    }
})
def list_tasks():
    try:
        status = request.args.get("status")
        tasks = list_tasks_service(status)
        return jsonify(tasks), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route("/<task_id>", methods=["GET"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [{
        'name': 'task_id',
        'in': 'path',
        'type': 'string',
        'required': True,
        'description': "ID da tarefa"
    }],
    'responses': {
        200: {'description': "Detalhes da tarefa"},
        404: {'description': TASK_NOT_FOUND}
    }
})
def get_task(task_id):
    try:
        task = get_task_service(task_id)
        return jsonify(task), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route("/<task_id>", methods=["PUT"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': "ID da tarefa"
        },
        {
            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': TaskUpdateSchema.model_json_schema()
        }
    ],
    'responses': {
        200: {'description': TASK_UPDATED},
        400: {'description': INVALID_DATA},
        404: {'description': TASK_NOT_FOUND}
    }
})
def update_task(task_id):
    try:
        update_data = TaskUpdateSchema(**request.json).model_dump(exclude_none=True)
        update_task_service(task_id, update_data)
        return jsonify({"message": TASK_UPDATED}), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route("/<task_id>", methods=["DELETE"])
@swag_from({
    'tags': ['Tasks'],
    'parameters': [{
        'name': 'task_id',
        'in': 'path',
        'type': 'string',
        'required': True,
        'description': "ID da tarefa a ser deletada"
    }],
    'responses': {
        200: {'description': TASK_DELETED},
        404: {'description': TASK_NOT_FOUND}
    }
})
def delete_task(task_id):
    try:
        delete_task_service(task_id)
        return jsonify({"message": TASK_DELETED}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@task_bp.route("/all", methods=["DELETE"])
@swag_from({
    'tags': ['Tasks'],
    'responses': {
        200: {'description': ALL_TASKS_DELETED}
    }
})
def delete_all_tasks():
    try:
        delete_all_tasks_service()
        return jsonify({"message": ALL_TASKS_DELETED}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
