import string
import re
import csv
from collections import defaultdict
import os

def count_and_lines(theword):
	count=0
	lst=''
	flag= True
	lines_list=[]
	header=['Word','Total Count']
	word_dict=defaultdict(list)
	for filename in os.listdir(os.getcwd()):
		with open(filename, 'r') as file:
			if filename == 'shakespeare.csv':
				flag = False
			if filename[-3:] =="txt":
				header.append('Lines from ' + filename)
				for line in file:
					words = line.split()
					count+=1
					for word in words:
						if re.search(theword, word.lower()):
							lines_list.append(count)
				word_dict[theword].append(lines_list)
				lines_list=[]
	print(word_dict)

	with open('shakespeare.csv', 'a') as csvfile:
		i=0
		result= []
		total=[]
		csvwriter = csv.writer(csvfile)
		if flag:
			csvwriter.writerow(header) 
			flag = False
		for word,lines in word_dict.items():
			result.append(word)
			for item in lines:
				if item:
					i+=len(item)
					total.append(str(item))
				else:
					total.append('N/A')
			result.append(str(i))
			result.extend(total)
		print(result)
		csvwriter.writerow(result)

count_and_lines('witchcraft')
count_and_lines('royal')
