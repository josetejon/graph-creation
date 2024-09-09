class ActionService:
    def __init__(self, repository):
        self.repository = repository

    def create_action(self):
        self.repository.create_action()
