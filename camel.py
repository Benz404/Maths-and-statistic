def rem(var1):
	for i in var1:
		if i==" ":
			var1=var1.replace(i,"")
	return var1
	
def camel_word(var2):
	str1=rem(var2)
	new=[]
	final=""
	for i in str1:
		if (str1.index(i))%2==0:
			new.append(i.upper())
		else:
			new.append(i.lower())
	for i in new:
		final= final+"".join(i)
	return final

