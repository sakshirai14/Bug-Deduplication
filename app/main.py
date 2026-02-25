from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_vector_store, routes_dedupe,json_store_routes
from app.core.logging import logger

app = FastAPI(title="Bug Deduplication API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(routes_vector_store.router)
app.include_router(routes_dedupe.router)
app.include_router(json_store_routes.router)


@app.get("/")
async def root():
    return {"message": "Bug Deduplication API is running"}
