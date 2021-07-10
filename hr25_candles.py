def birthdayCakeCandles(candles):
	val = 0
	candles.sort()
	a = candles[len(candles)-1]
	for i in candles:
		if i==a:
			val += 1
	return val




candles = [3,2,2,1,3,3]
print(birthdayCakeCandles(candles))