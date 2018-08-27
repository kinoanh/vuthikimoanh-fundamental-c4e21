mean = {
    "lol": "laugh out loud",
    "nyc": "new york city",
    "c4e":"code for everyone",
}

#ctrl+c:out(terminal)
for x in mean.keys() :
    print(x)
for v in mean.values():
    print(v)
for x , v in mean.items():
    print(x,":", v)