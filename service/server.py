from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from routes.organization import Org
from routes.healthcheck import Healthcheck

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

organization = Org()
healthcheck = Healthcheck()

app.include_router(organization.router)
app.include_router(healthcheck.router)
