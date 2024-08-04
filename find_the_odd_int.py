def find_it(seq):
    resturn_int = None
    sequence_dict = {}
    for integer in seq:
        if integer not in sequence_dict:
            sequence_dict[integer] =1
        else:
            sequence_dict[integer] +=1
    for key, value in sequence_dict.items():
        print(key, value)
        if value %2 != 0:
            print(key, value, "return")
            return int(key)
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
