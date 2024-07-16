ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

y = list(ft_tuple)
y[1] = "France!"
ft_tuple = tuple(y)

to_remove = {"tutu!" : 1}
ft_set.difference_update(to_remove)
to_add = {"Mulhouse!" : 1}
ft_set.update(to_add)

ft_dict["Hello"] = "42Mulhouse!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)