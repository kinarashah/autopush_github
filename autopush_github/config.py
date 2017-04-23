import ConfigParser 

class Parser(object):
    def __init__(self):
        self.parser = ConfigParser.ConfigParser()

    def parse(self):
        self.parser.read('../config.cfg')
        self.username = self.parser.get('leetcode','username')
        self.password = self.parser.get('leetcode', 'password')
        return not self.username and not self.password

parser = Parser()
if not parser.parse():
    print "No login data in config.cfg."

USERNAME = parser.username
PASSWORD = parser.password
