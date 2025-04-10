from flask import Blueprint
from app.interfaces.routes.create_task_route import create_task
from app.interfaces.routes.list_tasks_route import list_tasks
from app.interfaces.routes.get_task_route import get_task
from app.interfaces.routes.update_task_route import update_task
from app.interfaces.routes.delete_task_route import delete_task
from app.interfaces.routes.delete_all_task_route import delete_all_tasks

task_bp = Blueprint("tasks", __name__)

task_bp.add_url_rule("/", view_func=create_task, methods=["POST"])
task_bp.add_url_rule("/", view_func=list_tasks, methods=["GET"])
task_bp.add_url_rule("/<task_id>", view_func=get_task, methods=["GET"])
task_bp.add_url_rule("/<task_id>", view_func=update_task, methods=["PUT"])
task_bp.add_url_rule("/<task_id>", view_func=delete_task, methods=["DELETE"])
task_bp.add_url_rule("/all", view_func=delete_all_tasks, methods=["DELETE"])
