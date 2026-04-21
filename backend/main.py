from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.entrypoints.mri_router import router as mri_router
from src.entrypoints.algorithm_router import router as algorithm_router
from src.entrypoints.execution_router import router as execution_router
from src.entrypoints.user_router import router as user_router
from src.entrypoints.auth_router import router as auth_router

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
app.include_router(auth_router)
