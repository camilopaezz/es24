def josephus(k: int, names: list[str]):
  offset = 0

  while len(names) != 1:
    current_len = len(names)
    delete_compesated = offset + k

    if delete_compesated < current_len:
      real_delete = delete_compesated - 1
      names.pop(real_delete)
      offset = real_delete
    else:
      if delete_compesated % current_len == 0:
        names.pop(-1)
        offset = 0
      else:
        real_delete = (delete_compesated % current_len) - 1
        names.pop(real_delete)
        offset = real_delete
  return names

print(josephus(5, ['Abel', 'Camilo', 'Laura', 'Carlos', 'Jose', 'Yurani']))
# print(josephus(1, ['Abel', 'Camilo', 'Laura']))