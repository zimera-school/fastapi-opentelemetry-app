from fastapi import APIRouter
from api.tables import Organization

class Org:

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/organization", self.all, methods=["GET"])
        self.router.add_api_route("/organization/{org_id}", self.by_id, methods=["GET"])

    async def all(self):
        data = await Organization.select()
        return data

    async def by_id(self, org_id):
        data = await Organization.select().where(
            Organization.organization_id == int(org_id)
        )
        return data
