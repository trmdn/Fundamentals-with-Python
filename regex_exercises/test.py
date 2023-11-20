import re

input_text = "The waterfall was so high, that the child couldn't see its peak."
word_to_search = "the"

pattern = r'\b{}\b'.format(re.escape(word_to_search))
matches = re.findall(pattern, input_text, flags=re.IGNORECASE)

print(len(matches))