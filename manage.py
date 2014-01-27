from flask.ext.script import Manager
from dictionary import app
import nose


manager = Manager(app)

@manager.command
def test():
	nose.main(argv=['dictionary'])

def main():
	manager.run()

if __name__ == '__main__':
	main()