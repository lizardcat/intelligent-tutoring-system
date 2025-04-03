# tests/performance/load_test.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # wait between 1 and 5 seconds between tasks

    @task
    def load_home_page(self):
        self.client.get("/")

    @task(3)  # 3 times more likely than home page
    def load_dashboard(self):
        self.client.get("/dashboard")

    @task
    def login(self):
        self.client.post("/login", {
            "username": "test_user",
            "password": "test123"
        })