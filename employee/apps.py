from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    name = 'employee'

    def ready(self):
        # everytime server restarts
        import employee.signals
