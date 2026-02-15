import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1）训练数据（你可以理解成：给模型看的例子）
texts = [
    "I love this movie",
    "This is amazing",
    "So good and wonderful",
    "I hate this",
    "This is terrible",
    "So bad and disappointing",
]

labels = [
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
]

# 2）建立一个“文本分类流水线”
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

# 3）训练模型
model.fit(texts, labels)

print("Model training finished!")

# 4）保存模型到文件
joblib.dump(model, "sentiment_model.pkl")

print("Model saved as sentiment_model.pkl")
