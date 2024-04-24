class AnalysisModule:
    def __init__(self, results):
        self.results = results

    def generate_report(self):
        """Generate a report""" # TODO : report 형태로 만들어서 save까지 하도록 구현
        report = f"US | {self.results['US']}\nKO | {self.results['KO']}"
        return report
