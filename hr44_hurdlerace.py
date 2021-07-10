def hurdleRace(k, height):
	height.sort()
	if height[len(height)-1] <= k:
		return 0
	else:
		return height[len(height)-1]-k




k = 7
height = [2,5,4,5,2]
print(hurdleRace(k,height))