from flask import Blueprint
from app.domain.services.tasks.create_task_service import create_task
from app.domain.services.tasks.list_tasks_service import list_tasks
from app.domain.services.tasks.get_task_service import get_task
from app.domain.services.tasks.update_task_service import update_task
from app.domain.services.tasks.delete_task_service import delete_task
from app.domain.services.tasks.delete_all_task_service import delete_all_tasks

task_bp = Blueprint("tasks", __name__)

task_bp.add_url_rule("/", view_func=create_task, methods=["POST"])
task_bp.add_url_rule("/", view_func=list_tasks, methods=["GET"])
task_bp.add_url_rule("/<task_id>", view_func=get_task, methods=["GET"])
task_bp.add_url_rule("/<task_id>", view_func=update_task, methods=["PUT"])
task_bp.add_url_rule("/<task_id>", view_func=delete_task, methods=["DELETE"])
task_bp.add_url_rule("/all", view_func=delete_all_tasks, methods=["DELETE"])