from src.repository.algorithm import InMemoryAlgorithmRepository

 
def get_execution_details(execution_repository):
    algorithm_repository = InMemoryAlgorithmRepository()
    items = execution_repository.get_all()
    result = []
    for item in items:
        algorithm_id = item.algorithm_id
        algorithm = algorithm_repository.get_by_id(algorithm_id)
        for detail in item.details:
            result_item = {}
            result_item["algorithm_name"] = algorithm.name
            result_item["timestamp"] = detail.timestamp
            result_item["message"] = detail.message
            result_item["level"] = detail.level
            result_item["id"] = detail.id
            result.append(result_item)
    return result