import pytest
from main import create_app
from flask import json
from flask import Flask
from app.interfaces.routes import task_bp

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# Teste POST /tasks
def test_create_task(client):
    task_data = {
        "title": "Testar criação de tarefa",
        "description": "Descrição da tarefa",
        "status": "pending",
        "owner": "Caua"
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    assert "id" in response.json

# Teste GET /tasks
def test_list_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Teste GET /tasks/<task_id>
def test_get_task(client):
    task_data = {
        "title": "Testar tarefa específica",
        "description": "Detalhes da tarefa",
        "status": "pending",
        "owner": "Caua"
    }
    # Cria uma tarefa para pegar o ID
    post_response = client.post("/tasks/", json=task_data)
    task_id = post_response.json["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json["title"] == task_data["title"]

# Teste PUT /tasks/<task_id>
def test_update_task(client):
    task_data = {
        "title": "Testar atualização",
        "description": "Alteração da tarefa",
        "status": "pending",
        "owner": "Caua"
    }
    # Cria uma tarefa para pegar o ID
    post_response = client.post("/tasks/", json=task_data)
    task_id = post_response.json["id"]

    update_data = {"status": "done"}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json["message"] == "Tarefa atualizada com sucesso!"

# Teste DELETE /tasks/<task_id>
def test_delete_task(client):
    task_data = {
        "title": "Testar deleção",
        "description": "Deletando a tarefa",
        "status": "pending",
        "owner": "Caua"
    }
    # Cria uma tarefa para pegar o ID
    post_response = client.post("/tasks/", json=task_data)
    task_id = post_response.json["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Tarefa deletada com sucesso!"

# Teste DELETE /tasks/all
def test_delete_all_tasks(client):
    # Cria algumas tarefas
    for i in range(3):
        task_data = {
            "title": f"Tarefa {i}",
            "description": f"Descrição {i}",
            "status": "pending",
            "owner": "Caua"
        }
        client.post("/tasks/", json=task_data)

    # Deleta todas essas tarefas adicionadas
    response = client.delete("/tasks/all")
    assert response.status_code == 200
    assert response.json["message"] == "Todas as tarefas foram deletadas com sucesso!"

    # Verifica se não sobrou nenhuma
    list_response = client.get("/tasks/")
    assert list_response.status_code == 200
    assert isinstance(list_response.json, list)
    assert len(list_response.json) == 0