from collections import Counter

stopwords = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}

def make_crusoe_dict():
    my_text = open("Defoe_Robinson_Crusoe.txt", encoding="utf-8").read()  # Get the text
    my_text = my_text.lower()  # Set it to lowercase
    punctuation = "!\"#$—%&'()*+,-.”/:;<=>?@[\]^“_`{|}~0123456789"
    no_punct = str.maketrans("", "", punctuation)  # replaces things in puctuation var with nothing
    my_text = my_text.translate(no_punct)  # Excludes all punct from the punctuation var, returns the text without it.
    my_text = my_text.split()  # Makes it into a list by itself. Why? No idea, but it´s cool.

    my_text = [i for i in my_text if not i in stopwords]  # Removes all stopwords from the list
    crusoe_dict = Counter(my_text)
    return crusoe_dict

make_crusoe_dict()