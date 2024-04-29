import random as rd
def makepassword(x):
	lower='abcdefghijklmnopqrstuvwxyz'
	upper=lower.upper()
	numbers='1234567890'
	symbols="~!@#$%^&*()_+:?>/"
	password_length=x

	newline=lower+upper+numbers+symbols
	password="".join(rd.sample(newline,password_length))
	return password