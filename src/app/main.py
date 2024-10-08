from fastapi import FastAPI
from app.api.v1.users.route import router as users_router

app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOWED_ORIGINS,
#     allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
#     allow_methods=settings.ALLOWED_METHODS,
#     allow_headers=settings.ALLOWED_HEADERS,
# )

# app.add_event_handler(
#     "startup",
#     execute_backend_server_event_handler(backend_app=app),
# )
# app.add_event_handler(
#     "shutdown",
#     terminate_backend_server_event_handler(backend_app=app),
# )

app.include_router(router=users_router)


@app.get("/")
async def root():
    return {"message": "Welcome to yet-another-fastapi-template"}
