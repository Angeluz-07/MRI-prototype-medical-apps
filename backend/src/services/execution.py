from src.repository.algorithm import InMemoryAlgorithmRepository
from src.repository.user import InMemoryUserRepository
 
def get_execution_details(execution_repository):
    algorithm_repository = InMemoryAlgorithmRepository()
    user_repository = InMemoryUserRepository()
    items = execution_repository.get_all()
    result = []
    for item in items:
        user_id = item.user_id
        algorithm_id = item.algorithm_id
        algorithm = algorithm_repository.get_by_id(algorithm_id)
        user = user_repository.get_by_id(user_id)
        for detail in item.details:
            result_item = {}
            result_item["algorithm_name"] = algorithm.name
            result_item["user_name"] = user.username
            result_item["timestamp"] = detail.timestamp
            result_item["message"] = detail.message
            result_item["level"] = detail.level
            result_item["id"] = detail.id
            result.append(result_item)
    return result