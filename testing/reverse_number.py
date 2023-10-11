
def reverse_number(number):
  """
  Returns the reverse of a given number.
  """
  rev = 0
  
  while(number > 0):
    a = number % 10 # modulus (gives the unit digit)
    rev = rev * 10 + a # multiple current value by 10 so that the next digit can be added
    number = number // 10 # floor division by 10 remove the unit digit for next iteration

  return rev

if __name__ == '__main__':
  number = 4562
  reverse = reverse_number(number)

  print(reverse)