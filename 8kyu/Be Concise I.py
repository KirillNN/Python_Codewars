def describe_age(i):
  return "You're a(n) "+['elderly','adult','teenager','kid'][(i<13)+(i<18)+(i<65)]

def describe_age(a):
    return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"