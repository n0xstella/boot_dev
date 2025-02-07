"""
Practice in alternative method of O(n) vs O(m) for mapping keywords in a document string,
to substrings that are treataed as keywords.
"""

def map_keywords(document, document_map):
    if document in document_map:
        return document_map[document], document_map
        
    new_dict = dict(document_map)
    found_keywords = find_keywords(document)
    new_dict[document] = found_keywords
    return found_keywords, new_dict


# O(n) - Linear progression through the the keywords, preferred for this type of problem for speed.
def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]
    
    found_words = []
    found_words = [x for x in keywords if x in document]

    return found_words
    
# O(m x len(document))
def find_keywords(document, keywords=None):
    if keywords is None:
        keywords = [
            "functional", "immutable", "declarative", "higher-order",
            "lambda", "deterministic", "side-effects", "memoization",
            "referential transparency",
        ]
    
    # Base case: If the keywords list is empty, return an empty list
    if not keywords:
        return []

    # Process the first keyword in the list
    current_keyword = keywords[0]
    words_in_doc = document.replace('.', '').split()
    words_in_doc_set = set(words_in_doc)

    # If the keyword is in the document, add it to the result
    found_words = [current_keyword] if current_keyword in words_in_doc_set else []

    # Recursively process the remaining keywords
    return found_words + find_keywords(document, keywords[1:])
