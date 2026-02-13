from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1）定义输入格式
class PredictRequest(BaseModel):
    text: str

# 2）主页接口
@app.get("/")
def home():
    return {"message": "API is working!"}

# 3）预测接口（POST）
@app.post("/predict")
def predict(req: PredictRequest):
    text = req.text.lower()

    # 暂时用规则模拟模型
    if "good" in text or "love" in text:
        sentiment = "positive"
    elif "bad" in text or "hate" in text:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {"sentiment": sentiment}
