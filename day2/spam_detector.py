""" The Spam Detector (Search in Stream) -linear search
A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist has no order. """

blacklist_id = [101, 405, 104, 203, 301]
sender_id = int(input("enter sender id: "))

f=0
for i in blacklist_id:
    if sender_id == i:
        print("sender with",sender_id, " is a spam mail")
        f=1
        break

if f==0:
    print("sender with",sender_id, " is a not spam mail")