class Utils:
    def __init__(self):
        pass

    def sort(self, data, begin, finish):
        start = data.find(begin) + len(begin)
        end = data.find(finish)
        substring = data[start:end]
        return substring

    def check(self, data, string1, string2):
        if string1 in str(data):
            info = Utils.sort(self, data, string1, string2)
            return info
        else:
            return 'Unknown'

    def color(self, category):
        category_dict = {
            'VFR': (0, 255, 0),
            'MVFR': (0, 0, 255),
            'IFR': (255, 0, 0),
            'LIFR': (255, 20, 47)
        }
        return category_dict[category] if category in category_dict else (0, 255, 255)
