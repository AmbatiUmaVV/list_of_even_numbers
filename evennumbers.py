def find_Even_Numbers(start_number,end_number):
    list1 = []
    for number in range(start_number,end_number+1):
        if number % 2 == 0:
            list1.append(number)
    return ("even : " + str(list1))

initial_number = 7
final_number =  77
print(find_Even_Numbers(initial_number,final_number))