import sys
from prompt_toolkit import prompt


def cli_query():
	"""
		Function to handle command line usage
	"""
	try:
		args = sys.argv
		args = args[1:] # First element of args is the file name
		if len(args) == 0:
			print('Please pass some queries!')
		else:
			for a in args:
				if a == '--query':
					query = prompt(input("Enter your query to search: "))
				elif a == '--help':
					print('Command Line Operations')
					print('Options:')
					print('    --help -> Show this message and exit.')
					print('    --query -> Read the user query.')
				else:
					print('Unrecognised argument.')
			return query
	except Exception as e:
		print(e)
		print("Query Parsing Error!!!")


if __name__ == '__main__':
	cli_query()
