from urllib.request import urlopen
center = urlopen('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=400064&date=30-06-2021')
center_words = []
for line in center:
    story_words = line.decode('utf-8').split()
    for word in story_words:
        center_words.append(word)
center.close()
print (center_words)