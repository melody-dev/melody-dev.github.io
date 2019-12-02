from locust import HttpLocust
from locust import TaskSet
from locust import task

# For HTML reporting
from locust.web import app
from src import report
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)

class WebsiteTasks(TaskSet):
    @task
    def post_message(self):
        self.client.post("/v1/message", data={
        "message": "Hello"
    })
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)
