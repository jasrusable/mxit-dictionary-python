from flask.ext.script import Manager
from dictionary import app
import nose


manager = Manager(app)

@manager.command
def test():
	nose.main(argv=['dictionary', '--failed'])

def main():
	manager.run()

@manager.command
def build_dictionary():
	from dictionary.bin import build_dictionary
	build_dictionary()

if __name__ == '__main__':
	main()