import pymongo
import json

# Menghubungkan ke MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["courses"]
collection = db["courses"]

# membaca data json
with open("courses.json", "r") as f:
    courses = json.load(f)

# membuat index name
collection.create_index("name")

# membuat variabel rating di courses
for course in courses:
    course['rating'] = {'total': 0, 'count': 0}
    
# menambahkan variabel rating di setiap chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# menambahkan courses ke collection
for course in courses:
    collection.insert_one(course)

# menutup koneksi dengan MongoDB
client.close()
