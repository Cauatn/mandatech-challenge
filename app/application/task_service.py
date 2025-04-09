from app.infrastructure.mongo_repository import (
    insert_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task,
    delete_all_tasks  
)

def create_task_service(task_data: dict) -> str:
    return insert_task(task_data)

def list_tasks_service(status: str = None) -> list:
    return get_all_tasks(status)

def get_task_service(task_id: str) -> dict:
    task = get_task(task_id)
    if not task:
        raise ValueError("Tarefa não encontrada")
    return task

def update_task_service(task_id: str, update_data: dict) -> int:
    updated = update_task(task_id, update_data)
    if updated == 0:
        raise ValueError("Tarefa não encontrada para atualizar")
    return updated

def delete_task_service(task_id: str) -> int:
    deleted = delete_task(task_id)
    if deleted == 0:
        raise ValueError("Tarefa não encontrada para deletar")
    return deleted

def delete_all_tasks_service():
    delete_all_tasks()
