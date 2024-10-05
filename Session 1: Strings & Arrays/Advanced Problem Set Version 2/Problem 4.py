def minimum_boxes(meals, capacity):
	sum_meals = sum(meals)
	capacity.sort(reverse=True)
	box_count=0
	for i in capacity:
	    sum_meals -= i
	    box_count+=1
	    if sum_meals<=0:
	        break
	print(box_count)
meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)
