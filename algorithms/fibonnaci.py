# Assisted by watsonx Code Assistant 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import time

start_time = time.time()
fibonacci(40)
end_time = time.time()

print("Time taken:", end_time - start_time, "seconds")