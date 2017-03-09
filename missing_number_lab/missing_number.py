def find_missing(list1,list2):

	list3 = []
	count =0

	for i in list1:
		if i in list2:
			set1 = set(list1)
			set2 = set(list2)
			count = set1 - set2
			count = list(count)

	list3.append(count)
	return (list3)
