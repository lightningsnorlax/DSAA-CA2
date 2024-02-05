# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# mergeSort function
# -------------------------
def mergeSort(l):
	if len(l) > 1:
		mid = int (len(l)/2)
		# Here is where split into 2 halves
		leftHalf = l[:mid]
		rightHalf = l[mid:]

		# Recursive call
		mergeSort(leftHalf)
		mergeSort(rightHalf)

		leftIndex,rightIndex,mergeIndex = 0,0,0

		# Takes care of merging
		mergeList = l
		while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
			if leftHalf[leftIndex] < rightHalf[rightIndex]:
				mergeList[mergeIndex] = leftHalf[leftIndex]
				leftIndex+=1
			else:
				mergeList[mergeIndex] = rightHalf[rightIndex]
				rightIndex+=1
			mergeIndex+=1

		# Handle those items still left in the left Half
		while leftIndex < len(leftHalf):
			mergeList[mergeIndex] = leftHalf[leftIndex]
			leftIndex+=1
			mergeIndex+=1
		
        # Handle those items still left in the right Half
		while rightIndex < len(rightHalf):
			mergeList[mergeIndex] = rightHalf[rightIndex]
			rightIndex+=1
			mergeIndex+=1