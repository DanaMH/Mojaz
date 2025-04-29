import re

def normalize_sentence(sentence):
    """تنظيف الجملة من المسافات والنقاط."""
    return sentence.strip().rstrip(".")

def generate_distinct_colors(n):
    """توليد ألوان مميزة للتظليل."""
    base_colors = ['#FFFF99', '#FFCC99', '#FF99CC', '#CC99FF', '#99CCFF', '#99FFCC', '#CCFF99']
    return [base_colors[i % len(base_colors)] for i in range(n)]

def highlight_text(text, matched_sentences, color):
    highlighted = text
    for sentence in matched_sentences:
        normalized_sentence = sentence.strip().rstrip('.').rstrip()
        if not normalized_sentence:
            continue  # لو الجملة فاضية يتجاهلها
        
        pattern = re.escape(normalized_sentence)
        highlighted, count = re.subn(
            pattern,
            f'<mark style="background-color: {color};">{normalized_sentence}</mark>',
            highlighted,
            count=1,  # فقط أول ظهور
            flags=re.IGNORECASE  
        )
    return highlighted
