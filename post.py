# Hey, don't forget to fix parameters for random generator for yourself

import vkontakte
import random

source="./store.txt"

group_id = "YOUR_GROUP_ID"
token = "YOUR_TOKEN" 
#  Get it here: https://oauth.vk.com/authorize?client_id=YOUR_GROUP_ID&https://oauth.vk.com/blank.html&scope=wall,groups,offline&display=popup&response_type=token


def pick_random_poem(source=source):
    
    print "Picking brilliant poetry from " + source
    poem_number = random.randint(1,597)
    count = 1
    result=""
    delimiter = "--------"
    
    with open(source, 'r') as text:
        for line in text:
            if count == poem_number and delimiter not in line:
                result += line
            if delimiter in line:
                count += 1
    return result.decode("cp1251")
    
def push_to_group(token=token,group_id=group_id):
    
    print "Pushing poetry to VK..."
    vk = vkontakte.API(token=token)
    publish = pick_random_poem()
    
    vk.wall.post(owner_id=group_id,friends_only=0,from_group=1,message=publish)
    
    print "Succesfully published"

push_to_group()
