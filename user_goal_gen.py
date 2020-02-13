import json
import random
import copy

activity_dict_file = open('/media/minhhieu/DATA/HOC/Thesis/reinforcement_bot/reinforcement_learning_bot/activity_dict.json',encoding='utf-8')
activity_dict = json.load(activity_dict_file)

activity_list = [activity for activity in list(activity_dict[0].keys()) if activity != 'other' and activity != 'greeting']
# print(activity_list)
user_goal_list = []
user_inform_list = []
max_num_request_slot = 1
max_num_inform_slot = 5

for num_request_slot in range(max_num_request_slot + 1):
    for num_inform_slot in range(1, max_num_inform_slot + 1):
        request_slot = None
        
        if num_request_slot > 0:
            request_slot = random.choice(activity_list)
        inform_dict = {}
        for i in range(num_inform_slot):
            # rand = random.uniform(0,1)
            # print(rand)
            # if rand < 0.1:
            #     break
            inform_slot = random.choice(activity_list)
            while inform_slot == request_slot:
                inform_slot = random.choice(activity_list)
            # print(inform_slot)
            inform_dict[inform_slot]=[random.choice(activity_dict[0][inform_slot]) for i in range(0,random.randint(1,2))]
            if request_slot != None:
                user_goal_list.append({'request_slots':{request_slot:'UNK'},'diaact':'request','inform_slots':inform_dict})
            else: 
                user_goal_list.append({'request_slots':{},'diaact':'request','inform_slots':inform_dict})

            user_inform_list.append(inform_dict)

            # print("aaaa")
        # print(inform_dict)
        

print(len(user_goal_list))
print(user_goal_list)
# user_goal_file = open('/media/minhhieu/DATA/HOC/Thesis/reinforcement_bot/reinforcement_learning_bot/activity_user_goals_3.json', "w",encoding='utf8')
user_goal_file = open('/media/minhhieu/DATA/HOC/Thesis/reinforcement_bot/reinforcement_learning_bot/activity_user_inform_list.json', "w",encoding='utf8')

json.dump(user_inform_list,user_goal_file,ensure_ascii=False)
user_goal_file.close()