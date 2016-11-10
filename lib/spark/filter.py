def not_empty(dataset_name):
	def f(data):
		return data['datasets'][dataset_name].size > 0
	return f

def not_bad():
	def f(data):
		return len(data.get('exceptions', [])) == 0
	return f
