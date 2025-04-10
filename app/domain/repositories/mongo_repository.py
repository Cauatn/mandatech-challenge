from pymongo import MongoClient
from datetime import datetime
from config import MONGO_URI, DATABASE_NAME
from bson.objectid import ObjectId

# Cria a conexão com o MongoDB a partir da URI definida no config.py
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
tasks_collection = db['tasks']

def insert_task(task_data: dict) -> str:
    """
    Insere uma nova tarefa no banco de dados.
    Adiciona a data de criação e retorna o id inserido.
    """
    task_data['created_at'] = datetime.now()
    result = tasks_collection.insert_one(task_data)
    return str(result.inserted_id)

def get_all_tasks(status: str = None) -> list:
    """
    Retorna todas as tarefas. Se 'status' for fornecido,
    filtra as tarefas com base nele.
    Ordena as tarefas por data de criação (crescente).
    """
    query = {}
    if status:
        query['status'] = status
    tasks_cursor = tasks_collection.find(query).sort("created_at", 1)
    tasks = []
    for task in tasks_cursor:
        task['_id'] = str(task['_id'])
        tasks.append(task)
    return tasks

def get_task(task_id: str) -> dict:
    """
    Retorna uma tarefa a partir do seu ID.
    """
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task['_id'] = str(task['_id'])
    return task

def update_task(task_id: str, update_data: dict) -> int:
    """
    Atualiza uma tarefa com os dados fornecidos.
    Retorna o número de documentos modificados.
    """
    result = tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})
    return result.modified_count

def delete_task(task_id: str) -> int:
    """
    Deleta uma tarefa a partir do seu ID.
    Retorna o número de documentos deletados.
    """
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count

def delete_all_tasks():
    """
    Deleta todas as tarefas do Banco
    """
    tasks_collection.delete_many({})
