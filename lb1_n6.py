#6
scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
bob_score = scores.get("Bob")
dave_score = scores.get("Dave", "не найден")
print(scores)
print(bob_score)
print(dave_score)
scores.pop("Alice")
print(scores)
print(len(scores))
print(scores.keys(), scores.values())