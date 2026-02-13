def predict(text):
    if "good" in text or "love" in text:
        sentiment = "positive"
    elif "bad" in text or "hate" in text:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment


if __name__ == "__main__":
    text = input("Input a sentence: ")
    result = predict(text)
    print("预测结果:", result)
