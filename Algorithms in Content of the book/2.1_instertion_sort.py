def insertion_sort(array_):
	for i in range(1, len(array_)):
		key = array_[i]
		j = i-1
		while j > -1 and array_[j] < key:
			array_[j+1] = array_[j]
			j -= 1
		array_[j+1] = key
		print(array_)

	print(array_)

if __name__ == '__main__':
	insertion_sort([5, 2, 4, 6, 1, 3])
	# insertion_sort([1, 2, 4, 5, 6, 3])