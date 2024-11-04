def find_common_participants(ft_string, sd_string, separator = ","):
     ft_list = set(ft_string.split(separator))
     sd_list = set(sd_string.split(separator))
     main_list = list(ft_list.intersection(sd_list))
     main_list.sort()

     return main_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "-")
