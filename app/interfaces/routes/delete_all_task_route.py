from flask import jsonify
from flasgger import swag_from
from app.domain.services.task_service import delete_all_tasks_service
from app.utils.messages import ALL_TASKS_DELETED
from app.utils.swagger_docs.task_docs import delete_all_tasks_doc


@swag_from(delete_all_tasks_doc)
def delete_all_tasks():
    try:
        delete_all_tasks_service()
        return jsonify({"message": ALL_TASKS_DELETED}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
