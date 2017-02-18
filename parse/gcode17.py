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

def recparse(lines, patterns, status, params = None, formals = None, last_formals = None):
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
		if status[0] == '@':
			n = params[n-1]
			status = status[1:]
		elif status[0] == '#':
			n = last_formals[n-1]
			status = status[1:]
		if n <= 0:
			return lines, []
		lines, result = recparse(lines, patterns, status, None, formals, last_formals)
		if result is None:
			return lines, None
		lr = [result]
		n -= 1
		last_lines = lines
		while n > 0:
			last_lines = lines
			lines, result = recparse(lines, patterns, status, None, formals, last_formals)
			n -= 1
			if result != None:
				last_lines = lines
				lr.append(result)
		return last_lines, lr
	elif status[0] == '*':
		status = status[1:]
		lines, result = recparse(lines, patterns, status, None, formals, last_formals)
		if result is None:
			return lines, None
		lr = [result]
		last_lines = lines
		while result != None:
			last_lines = lines
			lines, result = recparse(lines, patterns, status, None, formals, last_formals)
			if result != None:
				lr.append(result)
		return last_lines, lr
	else:
		m = None
		none = False
		for (regex, fix, func) in patterns[status]:
			if regex[0] is None:
				none = True
				break
			m = re.match(regex[0], lines[0])
			if m is not None:
				break
			else:
				m = None
		if not none and m is None:
			return lines, None
		args = []
		if not none:
			args = list(m.groups())
			args = [fix[x](args[x]) for x in range(len(args))]
			lines = lines[1:]
		for com in regex[1:]:
			com, newformals = get_formals(com, args, formals)
			lines, r = recparse(lines, patterns, com, args, newformals, formals)
			if lines == [] and r is None:
				break
			if r is None:
				return lines, None
			args.append(r)
		return lines, func(*args)

def get_formals(status, params, formals):
	status = status.split('(')
	newformals = ""
	if len(status) == 2:
		status, newformals = status
	else:
		status = status[0]
	if newformals != "":
		newformals = newformals.replace(')', '').split(',')
		refformals = []
		for f in newformals:
			if f[-1] == '@':
				refformals.append(params[int(f[:-1])-1])
			elif f[-1] == '#':
				refformals.append(formals[int(f[:-1])-1])
			else:
				refformals.append(int(f))
	else:
		refformals = []
	return status, refformals	

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
			if len(regex[0].replace(' ', '')) == 0:
				regex[0] = None
			else:
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
