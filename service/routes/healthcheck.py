from fastapi import APIRouter
from api.tables import Organization

class Healthcheck:

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/healthcheck", self.healthcheck, methods=["GET"])

    async def healthcheck(self):
        return {"alive": "yes"}
