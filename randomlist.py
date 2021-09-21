import random

f = open("instahashtags.txt","r")
content = f.read()
hashtags = content.split(' ')
print(hashtags)
f.close()

ranHashtags = random.sample(hashtags, len(hashtags))
print(ranHashtags)

str1 = ','.join(ranHashtags)
n = open("randomhashtags.txt","w")
nContent = n.write(str1.replace(',',' '))
n.close
