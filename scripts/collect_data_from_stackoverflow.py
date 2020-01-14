from stackapi import StackAPI
import json

SITE = StackAPI('stackoverflow')

result = SITE.fetch('users', sort='reputation', order='desc')
users = result['items']
limit = 3

for user_dict in users[:limit]:
    print(json.dumps(user_dict, indent=4, sort_keys=True))