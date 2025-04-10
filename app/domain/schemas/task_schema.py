"""
Schemas Pydantic utilizados para validação de dados de tarefas (Tasks).
Esses modelos garantem que as requisições recebidas pela API estejam no formato correto
antes de serem processadas pela aplicação ou armazenadas no banco.

O `TaskSchema` é usado na criação de novas tarefas, enquanto o `TaskUpdateSchema` é usado para atualizações parciais.
"""

from pydantic import BaseModel, Field
from typing import Literal, Optional

class TaskSchema(BaseModel):
    """
    Schema para criação de uma nova tarefa.

    - title: Título da tarefa (obrigatório, mínimo 1 caractere)
    - description: Descrição opcional da tarefa
    - status: Status atual da tarefa ('done', 'in_progress' ou 'pending')
    - owner: Dono da tarefa (obrigatório, mínimo 1 caractere)
    """
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: Literal["done", "in_progress", "pending"]
    owner: str = Field(..., min_length=1)

class TaskUpdateSchema(BaseModel):
    """
    Schema para atualização de uma tarefa existente.

    Todos os campos são opcionais:
    - status: Novo status da tarefa
    - title: Novo título
    - description: Nova descrição
    """
    status: Optional[Literal["done", "in_progress", "pending"]] = None
    title: Optional[str] = None
    description: Optional[str] = None
