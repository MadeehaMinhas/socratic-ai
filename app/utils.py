import spacy


nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)

    cleaned_tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct and token.is_alpha
    ]

    return " ".join(cleaned_tokens)
