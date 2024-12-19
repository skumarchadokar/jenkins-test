import sys


class JenkinsFunc:
    def __init__(self):
        # get the commands passed
        self.arguments = sys.argv

    def execute(self):
        print("----2-------")
        print(self.arguments)
        print(self.arguments[1])
        for i in self.arguments:
            print(i)
        print(type(self.arguments[1]))
        print("------2-----")
        return False


jf = JenkinsFunc()
jf.execute()