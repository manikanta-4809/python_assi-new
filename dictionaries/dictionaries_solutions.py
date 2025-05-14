# (easy questions)
# dictionaries basic
def invert_dictionary(d):
    return {v: k for k, v in d.items()}
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))

# dictionary operation
def merge_dictionaries(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))

# (medium questions)
# dictionary comprehensions
def words_frequencies(text):
    words = text.split()
    return {word: words.count(word)
for word in set(words)}
text = "the quick brown fox jumps over the lazy dog"
print(words_frequencies(text))

# nested dictionaries
def add_contact(contacts, name, info):
    contacts[name] = info
    return contacts
contact_book = {
    "Alice": {"phone": "123", "email": "alice@example.com"}
}
add_contact(contact_book, "Bob", {"phone": "999", "email": "bob@example.com"})
add_contact(contact_book, "Alice", {"phone": "999", "email": "alice_new@example.com"})
print(contact_book)