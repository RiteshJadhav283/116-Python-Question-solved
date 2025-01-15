import random
def random_select(lst):
    return random.choice(lst)
my_list=[1,2,3,4,5]
selected_element=random_select(my_list)
print(f"Randomly selected element: {selected_element}")