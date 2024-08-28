def calculate_structure_sum(*args):
  summator = 0
  for i in args:
    if isinstance(i, list | tuple | set):
      summator += calculate_structure_sum(*i)
    elif isinstance(i, int):
      summator += i
    elif isinstance(i, str):
      summator += len(i)
    elif isinstance(i, dict):
      for i_value in i.values():
        summator += i_value
      for i_key in i.keys():
        summator += len(i_key)
      
  return summator


data_structure = ([1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}]))

result = calculate_structure_sum(*data_structure)
print(result)