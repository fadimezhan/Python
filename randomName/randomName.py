import random

def generate_name():
    first_name=["Elizabeth","Blair","Klaus","Leonardo","Michael","Chuck"]
    last_name=["Michaelson","Bass","White","Waldorf","Luck"]
    return "{} {}".format(random.choice(first_name),random.choice(last_name))

print generate_name()



