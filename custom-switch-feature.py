def switch(argument):
   switcher = {
       1: "January",
       2: "February",
       3: "March",  
       4: "April",
       5: "May",
       6: "June",
       7: "July",
       8: "August",
       9: "September",
       10: "October", 
       11: "November",
       12: "December"
   }
   return switcher.get(argument, "Invalid month")

# provide multiple print statements to test the switch function
print(switch(10))
print(switch(2))
print(switch(7))
print(switch(13))
print(switch("a"))
