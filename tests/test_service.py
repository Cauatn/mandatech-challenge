import pytest
from app.application.task_service import (
    create_task_service,
    list_tasks_service,
    get_task_service,
    update_task_service,
    delete_task_service
)

# Teste para a criação de uma tarefa
def test_create_task_service():
    task_data = {
        "title": "Testar serviço de criação",
        "description": "Verificar o serviço de criação de tarefa",
        "status": "pending",
        "owner": "Cauã"
    }
    task_id = create_task_service(task_data)
    assert task_id is not None

# Teste para a listagem de tarefas
def test_list_tasks_service():
    tasks = list_tasks_service()
    assert isinstance(tasks, list)

# Teste para obter uma tarefa específica
def test_get_task_service():
    task_data = {
        "title": "Testar serviço de obter tarefa",
        "description": "Obter tarefa pelo ID",
        "status": "pending",
        "owner": "Cauã"
    }
    task_id = create_task_service(task_data)
    task = get_task_service(task_id)
    assert task["title"] == task_data["title"]

# Teste para atualizar uma tarefa
def test_update_task_service():
    task_data = {
        "title": "Testar serviço de atualização",
        "description": "Alterando dados da tarefa",
        "status": "pending",
        "owner": "Cauã"
    }
    task_id = create_task_service(task_data)
    updated = update_task_service(task_id, {"status": "done"})
    assert updated == 1

# Teste para deletar uma tarefa
def test_delete_task_service():
    task_data = {
        "title": "Testar serviço de deleção",
        "description": "Remover tarefa do banco",
        "status": "pending",
        "owner": "Cauã"
    }
    task_id = create_task_service(task_data)
    deleted = delete_task_service(task_id)
    assert deleted == 1
