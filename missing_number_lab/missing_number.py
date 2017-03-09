def find_missing(my_list):

	list1 = []
	count = 0

	for i in my_list:
		for x in range(len(my_list)):
			if i == my_list[x]:
				count = 0
		list1.append(count)
