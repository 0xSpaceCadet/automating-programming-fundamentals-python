spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))

#.items() enumaerate()
#.keys() #.values()

print(spam.get('age', 50))
print(spam.get('aged', 50)) # fallback

msg = "it was a bright cold day ina pril and it was late"
cnt = {}

#hash sequence methodology
for c in msg:
    cnt.setdefault(c, 0)  # does nothing if exists
    cnt[c]+=1
print(cnt)

