import time

class Utility(object):

	module_name = "Utility"

	def safe_int(self, a):
		try:
			return int(a)
		except:
			return -1

	def getCurrentTime(self):
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

	def checkForSQLInjectionCharacters(self, input):
		if not input:
			return 0
		invalid_characters = [';','=','"',"'",'or 1', 'delete ','drop ', '\\','like', '%','select ','update ','insert ', '(',')']
		for invalid_character in invalid_characters:
			if input.lower().find(invalid_character) != -1 :
				return 1
		return 0
