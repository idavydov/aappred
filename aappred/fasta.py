import re

class fasta:
	def __init__(self, string=None, filename=None):
		if filename!=None:
			f=open(filename,'r')
			string_list=f.readlines()
			f.close()
		elif string!=None:
			string_list=string.split("\n")
		self._read_fasta(string_list)
		
	def _read_fasta(self,string_list):
		self.sequence=""
		first=True
		for line in string_list:
			if len(line)<1 or line[0]=='#':
				continue

			if  line[0]=='>': #protein name
				if first:
					self.name=line[1:]
					first=False
					continue
				else:
					break
			line=re.sub('(\d|\s)','',line) #clear digits and spaces
			self.sequence+=line.strip()
			

	def split(self,wl=20,st=1):
		ret_list=[]
		for i in xrange(0,len(self.sequence)-wl+1,st):
			ret_list.append(self.sequence[i:i+wl])

		return ret_list

