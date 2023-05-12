class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        print(f'El usuario se llama: {self.first_name} {self.last_name}') 
    def greet_user(self):
        print(f"Bienvenido {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attemps(self):
        self.login_attempts=0