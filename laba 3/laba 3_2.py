def find_common_participants(str1, str2, delimiter=','):
    participants1 = str1.split(delimiter)
    participants2 = str2.split(delimiter)

    common_participants = list(set(participants1) & set(participants2))
    common_participants.sort()

    return common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group,participants_second_group)

print ("Общие участники:", result)