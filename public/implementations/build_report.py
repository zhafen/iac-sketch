class Registry:

    def __init__(self):
        self.data = {}

    def add(self, str: str, data: dict):
        for key, value in data.items():
            self.data.setdefault(key, {})[str] = value

    def get(self, str: str, key: str):
        return self.data[key][str]

    def set(self, str: str, key: str, value):
        self.data[key][str] = value

    def delete(self, str: str):
        for key in self.data:
            if str in self.data[key]:
                del self.data[key][str]

class Request:
    pass

class Report:
    pass

class ReportManagementSystem:

    def accept_request(self, request: Request) -> str:

        pass

    def set_up_report(self, report_id: str):

        metadata: dict = self.registry.get(report_id, "metadata")

    def deliver_report(self, report_id: str):

        pass

