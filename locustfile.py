from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", {"email": "test@club.com"})

    @task
    def getcompetition(self):
        self.client.get("/book/TestLocust/TestClub")

    # @task
    # def purchaseplaces(self):
        # self.client.post("purchasePlaces", {"places": 2})

    @task
    def logout(self):
        self.client.get("/logout")
