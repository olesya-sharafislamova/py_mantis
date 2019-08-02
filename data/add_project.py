
from model.project import Project
import string
import random

constant = [
    Project(name="name1", status="obsolete", view_state="public", description="descroption1"),
    Project(name="name2", status="obsolete", view_state="public", description="descroption2"),
]

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

status_list = ["development", "release", "stable", "obsolete"]
view_state_list = ["public", "private"]

testdata = [Project(name=random_string("name",10),
                    status=random.choice(status_list), view_state=random.choice(view_state_list),
                    description=random_string("desc", 10))
            for i in range(2)]

