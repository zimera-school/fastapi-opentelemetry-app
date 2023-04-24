from locust import HttpUser, task


class LoadTesting(HttpUser):
    @task
    def root_organization(self):
        self.client.post("/organization", json={})

    @task
    def root_organization_by_id(self):
        self.client.post("/organization/1", json={})
