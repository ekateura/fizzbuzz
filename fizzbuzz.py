// from solution import fizz_buzz
//print(fizz_buzz(1,5))
//1 2 Fizz 4 Buzz
//print(fizz_buzz(11, 20))
//11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

#BEGIN
def fizz_buzz(start,end):
result = ''

current = start
while current <= end:
  if result:
      result = result + ' '

  if current % 3 == 0 and current % 5 == 0:
      result = result + 'FizzBuzz'

  elif current % 3 == 0:
      result = result + 'Fizz'

  elif current % 5 == 0:
      result = result + 'Buzz' 

  else;
      result = result + str(current)

  current = current + 1

return result
#end       