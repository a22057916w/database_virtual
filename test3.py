from collections import defaultdict

my_list = ["post_id", "坪數", "樓層", "型態", "現況", "社區", "權狀坪數"]
my_dict = {}.fromkeys(my_list, "NULL")
#my_dict = defaultdict(lambda: "NULL")
#my_dict["post_id"] = post_id
print(my_dict.keys())
print(my_dict.items())
