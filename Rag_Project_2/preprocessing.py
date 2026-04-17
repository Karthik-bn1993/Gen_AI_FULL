import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# import re   # regular exp

# text = "I love Python"
# match = re.search("cat", text)
# print(match)

# text = "My marks are 85 and 90"
# numbers = re.findall(r"\d+", text)

# print(numbers)   # ['85', '90']

# import re

# text = "I love Java"
# result = re.sub("Java", "Python", text)

# print(result)