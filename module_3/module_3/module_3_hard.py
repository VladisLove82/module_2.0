data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_):

  if isinstance(data_, (list, tuple, set)):
    return sum(calculate_structure_sum(element) for element in data_)

  elif isinstance(data_, dict):
    return sum(calculate_structure_sum(key) + calculate_structure_sum(value) for key, value in data_.items())

  elif isinstance(data_, str):
    return len(data_)

  elif isinstance(data_, int):
    return data_


result = calculate_structure_sum(data_structure)
print(result)