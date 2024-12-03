data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(data_structure)

def calculate_structure_sum(args):

    count = 0

    if isinstance(args, int):
        count += args
    elif isinstance(args, str):
        count += len(args)
    elif isinstance (args, (list, tuple, set)):
        for elements in args:
            count += calculate_structure_sum(elements)
    elif isinstance(args, dict):
        for key, value in args.items():
            count += calculate_structure_sum(value) + calculate_structure_sum(key)
    return count
result = calculate_structure_sum(data_structure)
print('Cумма всех чисел и длин всех строк:', result)














