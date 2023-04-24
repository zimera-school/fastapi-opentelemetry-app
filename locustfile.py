from locust import HttpUser, task, between


class LoadTesting(HttpUser):
    wait_time = between(1, 5)

    @task
    def root_organization(self):
        self.client.get("/organization", json={})

    @task(3)
    def root_organization_by_id(self):
        self.client.get("/organization/1", json={})
