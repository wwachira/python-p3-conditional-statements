#!/usr/bin/env python3

def admin_login(username, password):

    if (username.lower() == "admin") and (password == "12345"):
        return "Access granted"
    elif (username.upper() == "ADMIN") and (password == "12345"):
        return "Access granted"
    elif (username.lower() == "sudo") and (password == "12345"):
        return "Access denied"
    else:
        return "Access denied"
        
 
print(admin_login("ADMIN", "12345"))#Access granted
print(admin_login("user", "password")) #Access denied
print(admin_login("admin", "12345"))# Access granted
print(admin_login("sudo", "12345")) #Access denied
print(admin_login("liz", "12345"))#Access denied


def hows_the_weather(temperature):
    #indexing(range)
  temp_ranges = {
      "below 40": "It's brisk out there!",  
      "40.1 to 65": "It's a little chilly out there!",    
      "65.1 to 84.9": "It's perfect out there!",  
      "85 t0 100": "It's too dang hot out there!",             
  }

  try:
    # string to float(temp)
    temperature = float(temperature)  
  except ValueError:
    return "Invalid temperature format."

  for range_str, description in temp_ranges.items():
    # temp limit from range
    upper_bound = float(range_str.split()[-1])
    if temperature <= upper_bound:  
      return description


print(hows_the_weather(36)) #It's brisk out there
print(hows_the_weather(65.2))  #It's perfect out there!
print(hows_the_weather(87)) #It's too dang hot out there!
print(hows_the_weather(35))#It's brisk out there

def fizzbuzz(num):
   # modulo check by my num
 if (num % 3 == 0) and (num % 5 == 0):
    return "FizzBuzz"
 elif num % 3 == 0: 
   return "Fizz"
 elif num % 5 == 0:
    return "Buzz"
 else:
  return str(num)
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(90))#fizzbuzz
print(fizzbuzz(79))#return orig num

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
       return num1 + num2
    elif operation == "-":
       return num1 - num2
    elif operation == "*":
       return num1 * num2
    elif operation == "/":
        return num1 / num2
   
    else:
          print("Invalid operation!")
          return None
print(calculator("*", 31, 5))
print(calculator("/", 30, 5))
print(calculator("-", 1, 5))
print(calculator("%", 1, 1))#invalid op,None
print(calculator("()", 1, 1))#invalid op,None

