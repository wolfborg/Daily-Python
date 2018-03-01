def nearest_sq(n):
	return round(n**0.5)**2

def number(bus_stops):
	return sum([stop[0]-stop[1] for stop in bus_stops])

def toCsvText(array):
	return '\n'.join(','.join(map(str,line)) for line in array)

def maps(a):
	return [x*2 for x in a]

def remove_char(s):
	return s[1:-1]



print remove_char('Tests')