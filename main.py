import sys


class JenkinsFunc:
    def __init__(self):
        # get the commands passed
        self.arguments = sys.argv

    def execute(self):
        print(self.arguments)


jf = JenkinsFunc()
jf.execute()