
from app import app, db
from app.models import Posts
from datetime import datetime
import json
with open('wechat_data.json', 'r') as f:
    wechat_data = json.load(f)

for item in wechat_data:
    post = Posts()
    post.title = item["title"]
    post.abstract = item["digest"]
    post.link = item["link"]
    post.create_time = datetime.fromtimestamp(item["create_time"])
    db.session.add(post)
    db.session.commit()