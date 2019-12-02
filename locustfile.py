from locust import HttpLocust, TaskSet, task, between
from locust.web import app
from src import report
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)

class WebsiteTasks(TaskSet):
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    @task
    def post_message(self):
        self.client.post("/v1/message", data={
        "message": "Hello"
    })

    # @task
    # def index(self):
    #     self.client.get("/health")
        
    # @task
    # def about(self):
    #     self.client.get("/about/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
