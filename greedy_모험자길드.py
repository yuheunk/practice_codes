def adventure_group(n, scared):
  scare_lst.sort()
  count = 0
  result = 0

  for value in scare_lst:
      count += 1
      if count >= value:
          result += 1
          count = 0
          
  return result          


N = int(input('Input number of adventurers:', ))
scare_lst = list(map(int, input('Enter scared levels of adventurers:',).split())) #[4, 1, 1, 1, 2]
print(adventure_group(N, scare_lst))
