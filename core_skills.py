import random
rand_list =  []
    # random.randint(1,20)

for i in range(10):
    rand_list.append(random.randint(1,20))

list_comprehension_below_10 = [a for a in rand_list if a < 10]

list_comprehension_below_10_filter = filter(lambda x : x < 10, rand_list)



if __name__ == '__main__':
    pass
    # print(list(list_comprehension_below_10_filter))
