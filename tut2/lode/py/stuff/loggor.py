class Loggor:
    @staticmethod
    def debug(*args):
        # print in grey color
        print('\033[90m' + ' '.join(map(str, args)) + '\033[0m')
