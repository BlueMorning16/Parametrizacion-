from locust import HttpUser, task, between

class Hello(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_wordl(self):
        self.client.get("")
    
    @task
    def sign(self):
        self.client.post("")

    
