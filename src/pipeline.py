from src.filters import Filter


class Pipeline:
    def __init__(self, filters: Filter):
        self.filters = filters
        
    def run_background(self):
        for filter in self.filters:
            filter.run()
