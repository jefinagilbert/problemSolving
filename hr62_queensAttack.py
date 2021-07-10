# this is my solution... but it is terminated due to time complexity.. but the solution is right...
def queensAttack(n, k, r_q, c_q, obstacles):
	tot = 0
	a = 0
	for i in reversed(range(1,c_q+1)):
		if i == c_q:
			continue
		if [r_q,i] in obstacles:
			break
		if 1 <= r_q <= n and 1 <= i <= n:
			a += 1
		else:
			break
	tot += a
	a = 0
	#right of the position
	for i in range(c_q,n+1):
		if i == c_q:
			continue
		if [r_q,i] in obstacles:
			break
		if 1 <= r_q <= n and 1 <= i <= n:
			a += 1
		else:
			break
	tot += a
	a = 0
	#up of the position
	for i in range(r_q,n+1):
		if i == r_q:
			continue
		if [i,c_q] in obstacles:
			break
		if 1 <= i <= n and 1 <= c_q <= n:
			a += 1
		else: break
	tot += a
	a = 0
	#bottom of the position
	for i in reversed(range(1,r_q+1)):
		if i == r_q:
			continue
		if [i,c_q] in obstacles:
			break
		if 1 <= i <= n and 1 <= c_q <= n:
			a += 1
		else: break
	tot += a
	a = 0
	#left-bottom diagonal of the position
	r,c = r_q,c_q
	for i in range(n):
		if [r,c] == [r_q,c_q]:
			r -= 1
			c -= 1
			continue
		if [r,c] in obstacles:
			break
		if 1 <= r <= n and 1 <= c <= n:
			a += 1
		else:
			break
		r -= 1
		c -= 1
	tot += a
	a = 0
	r,c = r_q,c_q
	#right-top diagonal of the position
	for i in range(n):
		if [r,c] == [r_q,c_q]:
			r += 1
			c += 1
			continue
		if [r,c] in obstacles:
			break
		if 1 <= r <= n and 1 <= c <= n:
			a += 1
		else:
			break
		r += 1
		c += 1
	tot += a
	a = 0
	r,c = r_q,c_q
	#right-bottom diagonal of the position
	for i in range(n):
		if [r,c] == [r_q,c_q]:
			r -= 1
			c += 1
			continue
		if [r,c] in obstacles:
			break
		if 1 <= r <= n and 1 <= c <= n:
			a += 1
		else:
			break
		r -= 1
		c += 1
	tot += a
	a = 0
	r,c = r_q,c_q
	#left-top diagonal of the position
	for i in range(n):
		if [r,c] == [r_q,c_q]:
			r += 1
			c -= 1
			continue
		if [r,c] in obstacles:
			break
		if 1 <= r <= n and 1 <= c <= n:
			a += 1
		else:
			break
		r += 1
		c -= 1
	tot += a
	return tot

n,k = 100000 , 0
r_q = 4187
c_q = 5068
obstacles = []
print(queensAttack(n,k,r_q,c_q,obstacles))