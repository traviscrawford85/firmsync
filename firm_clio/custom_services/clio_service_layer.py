from custom_services.matter_service import MatterService
from custom_services.contact_service import ContactService
from custom_services.activity_service import ActivityService
# from firm_clio.services.task_service import TaskService  # Add later

class ClioServiceLayer:
    """
    Aggregates all Clio-related service classes under one entry point.
    """

    def __init__(self):
        self.matters = MatterService()
        self.contacts = ContactService()
        self.activities = ActivityService()
        # self.tasks = TaskService()
