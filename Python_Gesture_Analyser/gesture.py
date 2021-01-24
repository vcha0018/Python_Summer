import numpy as np

class Gesture:
    def __init__(self, csv_data_str: str):
        self.csv_str = csv_data_str

    def get_parsed_data(self):
        lines = self.csv_str.split('\n')
        lines.pop()
        lines.pop(0)
        data = []
        for row in lines:
            timestamp = int(row.split(',')[0])
            points = row.split(',')[1:]
            if len(points) == 63:
                pointArray = [np.array([float(points[i].strip()), float(points[i + 1].strip()), float(points[i + 2].strip())]) for i in range(0, len(points), 3)]
                data.append((timestamp, pointArray))
        return data
