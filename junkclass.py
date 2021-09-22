class NetworkNode:
    def __init__(self, serialNumber, os):
        self.serialNumber = serialNumber
        self.os = os
    def nodeInfo(self):
        print('-' * 75)
        return '{} {}'.format(self.serialNumber, self.os)
