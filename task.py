def count_words(text):
    """Считает количество слов в тексте"""
    words = text.split()
    return len(words)

def count_sentences(text):
    """Считает количество предложений в тексте"""
    # Считаем, что предложения заканчиваются на . ! или ?
    sentences = 0
    for char in text:
        if char in '.!?':
            sentences += 1
    return sentences if sentences > 0 else 1  # Если нет знаков - считаем весь текст одним предложением

def text_analysis(text):
    """Возвращает словарь с анализом текста"""
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text)
    }

# Пример использования
print("\n=== Анализатор текста ===")
sample_text = "Привет! Как твои дела? У меня все хорошо."
analysis = text_analysis(sample_text)
print(f"Анализ текста: {analysis}")
