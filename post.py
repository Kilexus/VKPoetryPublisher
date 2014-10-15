import vkontakte
from time import gmtime, strftime

publish=""
store=""

first_occur=False
print "Retrieving brilliant poetry from database..."
with open("./store.txt", 'r') as text:
    for line in text:
        if first_occur is False:
            if "--------" in line:
                first_occur=True
            else:
                publish=publish + line
        else:
            store = store + line

with open("./store.txt", 'w') as text:
    text.write(store)


print "Pushing poetry to VK..."

vk = vkontakte.API(token='YOUR_TOKEN')

print vk.wall.post(owner_id=-#YOUR_GROUP_ID#,friends_only=0,from_group=1,message=publish.decode("cp1251"))

print("Succesfully published.")
