import re
	
def primitive(type):
	if type == "Int":
		return int
	elif type == "Float":
		return float
	elif type == "String":
		return str
	elif type == "*Int":
		return lambda x: map(int, filter(lambda y: len(y) > 0, x.split(' ')))
	elif type == "*Float":
		return lambda x: map(float, filter(lambda y: len(y) > 0, x.split(' ')))
	elif type == "*String":
		return lambda x: map(str, filter(lambda y: len(y) > 0, x.split(' ')))

def parse(src, struct, funcs):
	funcs['identity'] = lambda x: x
	return recparse(list(file(src)), structure(funcs, struct), 'Main')

def recparse(lines, patterns, status, params = None):
	if status == ".":
		return lines, None
	if len(lines) == 0:
		return [], None
	if status[0].isdigit():
		n = int(status[0])
		status = status[1:]
		while status[0].isdigit():
			n *= 10
			n += int(status[0])
			status = status[1:]
			print n
		if status[0] == '@':
			n = params[n-1]
			status = status[1:]
		if n <= 0:
			return lines, []
		lines, result = recparse(lines, patterns, status)
		if result is None:
			return None, None
		lr = [result]
		n -= 1
		last_lines = lines
		while n > 0:
			last_lines = lines
			lines, result = recparse(lines, patterns, status)
			n -= 1
			if result != None:
				lr.append(result)
		return last_lines, lr
	if status[0] == '*':
		status = status[1:]
		lines, result = recparse(lines, patterns, status)
		if result is None:
			return None, None
		lr = [result]
		last_lines = lines
		while result != None:
			last_lines = lines
			lines, result = recparse(lines, patterns, status)
			if result != None:
				lr.append(result)
		return last_lines, lr
	else:
		m = None
		for (regex, fix, func) in patterns[status]:
			m = re.match(regex[0], lines[0])
			if m is not None:
				break
			else:
				m = None
		if m is None:
			return None, None
		args = list(m.groups())
		args = [fix[x](args[x]) for x in range(len(args))]
		lines = lines[1:]
		for com in regex[1:]:
			lines, r = recparse(lines, patterns, com, args)
			if lines == [] and r is None:
				break
			if r is None:
				return None, None
			args.append(r)
		return lines, func(*args)
		

def structure(funcs, struct):
	patterns = dict()
	struct = struct.split('\n')
	for line in struct:
		if line != '':
			head, body = line.split('=')
			if body.find('|') == -1:
				regex = body
				func = 'identity'
			else:
				regex, func = body.split('|')
			head = head.replace(' ', '')
			fix = map(primitive, filter(lambda x: x.istitle() , regex.strip().split(' ')))
			regex = regex.split('->')
			regex[0] = (regex[0] + ' ') \
				.replace('*Int', '([-0-9 ]+)') \
				.replace('*Float', '([.-0-9 ]+)') \
				.replace('*String', '([0-9a-zA-Z ]+)') \
				.replace('Int', '(-?\\d+)') \
				.replace('Float', '(-?\d*[.,]?\d+)') \
				.replace('String', '([0-9a-zA-Z]+)') \
				.replace(' ', '\s*')
			regex[1:] = map(lambda x: x.replace(' ', ''), regex[1:])
			func = func.replace(' ', '')
			if patterns.get(head) is None:
				patterns[head] = []
			patterns[head].append((regex, fix, funcs[func]))
	return patterns
