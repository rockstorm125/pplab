class reverse:
	def rev(self,str):
		str = str.split()
		n = []
		for i in str:
			n.append(i[::-1])
		s= " "
		s = s.join(n)

		return (s)

print("reversed string is: {} ".format(reverse().rev(input("enter string to be reversed: "))))