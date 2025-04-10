from app.utils.messages import (
    TASK_CREATED,
    TASK_UPDATED,
    TASK_DELETED,
    ALL_TASKS_DELETED,
    TASK_NOT_FOUND,
    INVALID_DATA,
)
from app.schemas.task_schema import TaskSchema

create_task_doc = {
    'tags': ['Tasks'],
    'parameters': [{
        'in': 'body',
        'name': 'body',
        'required': True,
        'schema': TaskSchema.model_json_schema()
    }],
    'responses': {
        201: {'description': TASK_CREATED},
        400: {'description': INVALID_DATA}
    }
}

list_tasks_doc = {
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
}

get_task_doc = {
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
}

update_task_doc = {
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
            'schema': {
                'type': 'object',
                'properties': {
                    'in_progress': {
                        'type': 'boolean',
                        'example': True,
                        'description': 'Se true, atualiza o status para "in_progress"; se false, para "pending".'
                    },
                    'done': {
                        'type': 'boolean',
                        'example': True,
                        'description': 'Se true, atualiza o status para "done"; se false, para "pending".'
                    },
                    'title': {
                        'type': 'string',
                        'example': 'Comprar leite'
                    },
                    'description': {
                        'type': 'string',
                        'example': 'Ir ao supermercado e comprar leite'
                    }
                },
                'additionalProperties': False,
                'description': (
                    "Envie a chave 'in_progress' ou 'done' para atualizar o status. "
                    "Caso ambas estejam ausentes, os demais campos serão validados via TaskUpdateSchema."
                )
            }
        }
    ],
    'responses': {
        200: {'description': TASK_UPDATED},
        400: {'description': INVALID_DATA},
        404: {'description': TASK_NOT_FOUND}
    }
}

delete_task_doc = {
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
}

delete_all_tasks_doc = {
    'tags': ['Tasks'],
    'responses': {
        200: {'description': ALL_TASKS_DELETED}
    }
}
