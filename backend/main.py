from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BuyerInquiry(BaseModel):
    companyName: str
    contactName: str
    email: str
    phone: str
    leadType: str
    targetMarket: str
    serviceRadius: str | None = None
    monthlyVolume: str | None = None
    notes: str | None = None

@app.post("/api/buyer-inquiry")
async def create_inquiry(inquiry: BuyerInquiry):
    record = inquiry.dict()
    record["id"] = str(uuid.uuid4())
    record["receivedAt"] = datetime.utcnow().isoformat()

    try:
        with open("buyer_inquiries.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open("buyer_inquiries.json", "w") as f:
        json.dump(data, f, indent=2)

    return {
        "status": "success",
        "leadID": record["id"]
    }

@app.get("/api/inquiries")
async def get_inquiries():
    try:
        with open("buyer_inquiries.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    return data