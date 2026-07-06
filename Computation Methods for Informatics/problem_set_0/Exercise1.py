#function to take the normal temperature as the parameter
def temp_tester(normal_temp):
    #creates a tester for a species and compares the temperature of the subject
    def tester(temp_check):
        if(abs(normal_temp - temp_check) < 1):
            return True
        else:
            return False
    return tester

human_tester = temp_tester(37)
chicken_tester = temp_tester(41.1)

print(chicken_tester(42))
print(human_tester(42))
print(chicken_tester(43))
print(human_tester(35))
print(human_tester(98.6))