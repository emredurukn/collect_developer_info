from github import Github
import os
import json

g = Github(os.environ['GITHUB_ACCESS_TOKEN'])


def search_with_keywords(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    print(f'Found {result.totalCount} repo(s)')
 
    return result


def search_with_language(language):
    query = 'language:' + language
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s)')
 
    return result


user_list = []
keywords = ['python', 'django', 'postgres']
result = search_with_keywords(keywords)
limit = 3

for repo in result[:limit]:
    user_id = repo.owner.id
    username = repo.owner.login
    user_url = repo.owner.html_url
    user_mail = repo.owner.email
    repo_url = repo.html_url
    location = repo.owner.location
    followers = repo.owner.followers
    following = repo.owner.following

    if user_mail is not None and followers != 0:
        user_list.append({
            'id': user_id,
            'username': username,
            'user_url': user_url,
            'user_mail': user_mail,
            'repo_url': repo_url,
            'location': location,
            'followers': followers,
            'following': following
        })

for user_dict in user_list:
    print(json.dumps(user_dict, indent=4, sort_keys=True))

