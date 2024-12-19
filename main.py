import sys


class JenkinsFunc:
    def __init__(self):
        # get the commands passed
        self.arguments = sys.argv

    def execute(self):
        print("------------")
        print(self.arguments)
        print(self.arguments[1])
        print(type(self.arguments[1]))
        print("------------")
        return False


jf = JenkinsFunc()
jf.execute()