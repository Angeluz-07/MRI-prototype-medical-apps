from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.mri_router import router as mri_router
from src.entrypoints.algorithm_router import router as algorithm_router
from src.entrypoints.execution_router import router as execution_router
from src.entrypoints.user_router import router as user_router

app = FastAPI()

# Handle CORS in local dev
origins= [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_credentials=True,  # Allows cookies and authorization headers
    allow_methods=["*"],     # Allows all methods (GET, POST, PUT, DELETE, OPTIONS, etc.)
    allow_headers=["*"],     # Allows all headers, including Authorization and Content-Type
)

app.include_router(mri_router)
app.include_router(algorithm_router)
app.include_router(execution_router)
app.include_router(user_router)


# from src.services.file import get_input_files, get_input_file_as_base64
# from src.services.file import get_output_files, get_output_file_as_base64
# from src.services.file import save_input_file

# @app.get("/mri/images")
# def mri_images():
#     return {"images": get_input_files()}

# @app.get("/mri/images/{id}")
# def mri_images(id:str):
#     return {"basestr": get_input_file_as_base64(id)}
    
# @app.get("/mri/results")
# def mri_images_results():
#     return {"images": get_output_files()}

# @app.get("/mri/results/{id}")
# def mri_images_results(id:str):
#     return {"basestr": get_output_file_as_base64(id)}

# from fastapi import UploadFile, File
# from typing import Annotated

# @app.post("/mri/images")
# def save_mri_image( fileMRI: Annotated[UploadFile, File(...)]):
#     filename = save_input_file(fileMRI.filename, fileMRI.file)
#     return {"filename":filename}

# from pydantic import BaseModel
# class AlgorithmRun(BaseModel):
#     algorithm_id: str
#     filename: str
#     user_id: str
    
# from src.services.algorithm  import run_algorithm
# from src.repository.execution import InMemoryExecutionRepository, JsonExecutionRepository
# from src.domain.filepath_manager import BASE_DIR
# #execution_repository = InMemoryExecutionRepository()
# execution_repository = JsonExecutionRepository(str(BASE_DIR / "data" / "executions.json"))

# @app.post("/algorithm/run")
# def segment_brain(algorithm_run: AlgorithmRun):
#     msg = run_algorithm(algorithm_run.algorithm_id, algorithm_run.filename, algorithm_run.user_id, execution_repository)
#     return { "message": msg }

# from src.services.algorithm import get_algorithms
# from pydantic import BaseModel, ConfigDict
# from typing import List

# class AlgorithmPublicSchema(BaseModel):
#     # This configuration is required to map from objects/dataclasses
#     model_config = ConfigDict(from_attributes=True)
#     id: str
#     name: str
#     description: str
    
# class AlgorithmsResponse(BaseModel):
#     items: List[AlgorithmPublicSchema]

# @app.get("/algorithms", response_model=AlgorithmsResponse)
# def get_operations():
#     return {"items":get_algorithms()}

# from src.services.execution import get_execution_details
from pydantic import BaseModel, ConfigDict
from typing import List
# from datetime import datetime

# class ExecutionDetailPublicSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#     algorithm_name: str
#     user_name: str
#     timestamp: datetime
#     message: str
#     level: str 
#     id: str 

# class ExecutionsResponse(BaseModel):
#     items: List[ExecutionDetailPublicSchema]

# @app.get("/execution-details", response_model=ExecutionsResponse)
# def get_operations():
#     return {"items":get_execution_details(execution_repository)}

# from src.services.auth import get_users_
from src.repository.user import InMemoryUserRepository
users_repository = InMemoryUserRepository()

# class UserDetailPublicSchema(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#     id: str
#     username: str
#     email: str

# class UsersResponse(BaseModel):
#     items: List[UserDetailPublicSchema]

# @app.get("/users", response_model=UsersResponse)
# def get_users():
#     return {"items":get_users_(users_repository)}

from src.services.auth import auth_backend
from src.services.auth import get_user_by_email, add_user, is_user_authorized
from pydantic import EmailStr
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Esquema para Swagger
security = HTTPBearer()

# 3. Schemas para Endpoints
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# 2. Modelos y Repositorio
class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str # En memoria será el hash

# 4. Endpoints de Autenticación
@app.post("/register")
def register(user: UserRegisterSchema):
    if get_user_by_email(users_repository, user.email):
        raise HTTPException(status_code=400, detail="El email ya existe")
    add_user(users_repository)
    return {"message": "ok"}

@app.post("/login")
def login(login_schema: LoginRequest):
    authorized = is_user_authorized(users_repository, login_schema)

    if not authorized:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    
    user = get_user_by_email(users_repository, login_schema.email)
    # AuthX genera el token usando el ID del usuario
    token = auth_backend.create_access_token(uid=user.id)
    return {"access_token": token, "token_type": "bearer"}

# 5. Ruta Protegida
@app.get("/me")
def get_current_user(token: HTTPAuthorizationCredentials = Depends(security),payload = Depends(auth_backend.access_token_required)):
    user_id = payload.sub 
    user = users_repository.get_by_id(user_id)
    return {"username": user.username, "email": user.email, "id": user.id}