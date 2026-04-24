from src.domain.models import Execution


class AlgorithmService:
    def __init__(self, algorithm_repository, execution_repository, file_repository):
        self.algorithm_repo = algorithm_repository
        self.execution_repo = execution_repository
        self.file_repo = file_repository
        
    def run_algorithm(self, algorithm_id, filename, user_id):
        algorithm_repo =  self.algorithm_repo
        file_repo = self.file_repo
        execution_repo = self.execution_repo

        img_full_path = file_repo.get_full_path(filename)
        algorithm = algorithm_repo.get_by_id(algorithm_id)
        
        if algorithm is None:
            raise Exception(f"unknown algorithm {algorithm_id}")
        
        
        try:
            exec = Execution(algorithm_id=algorithm.id, user_id=user_id)
            exec.add_log("starting")

            algorithm.run(img_full_path)
            
            exec.add_log("finished")
        except Exception:
            exec.add_log("error ocurred")
            raise
        finally:
            execution_repo.add(exec)

        return "success"

    def get_algorithms(self):
        return  self.algorithm_repo.get_all()
