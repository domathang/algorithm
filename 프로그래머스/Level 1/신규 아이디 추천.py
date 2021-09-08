import re
# 내 풀이
def solution(new_id):
    new_id = new_id.lower()
    p = re.compile('[a-z0-9\._-]+')
    new_id = "".join(p.findall(new_id))
    new_id = re.sub('[.]+', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

# 다른 사람의 풀이
def good_solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st