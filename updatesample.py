from pymongo import MongoClient
from pprint import pprint

MONGODB_URL = "YOUR MONGODB URL"
client = MongoClient(MONGODB_URL)
db = client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.reviews.update_one({'_id': ASingleReview.get('_id')}, {'$inc': {'likes': 1}})
print('Number of documents modified: ' + str(result.modified_count))

UpdatedDocument = db.reviews.find_one({'_id': ASingleReview.get('_id')})
print('The updated document:')
pprint(UpdatedDocument)