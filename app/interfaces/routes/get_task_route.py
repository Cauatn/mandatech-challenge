from flask import jsonify
from flasgger import swag_from
from app.domain.services.task_service import get_task_service
from app.utils.swagger_docs.task_docs import get_task_doc
    

@swag_from(get_task_doc)
def get_task(task_id):
    try:
        task = get_task_service(task_id)
        return jsonify(task), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500