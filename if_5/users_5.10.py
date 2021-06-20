current_users = ['andru', 'toBik', 'teddi', 'karolina', 'SANDRA', 'alex', \
'kleo']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
print(current_users_lower)

new_users = ['sara', 'TobiK', 'tor', 'elis', 'sanDra']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"the name {user} doesn't fit!! you choose another name")
    else:
        print(f"the name {user} fit")
