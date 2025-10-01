from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from services import ai_handler, parser

app = FastAPI()

class AskRequest(BaseModel):
    session_id: str
    query: str

@app.get("/")
def read_root():
    return {"message": "Global AI Knowledge Bridge Backend is running!"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF, extract text per page, and summarize each page with Cerebras.
    """
    pages_text = parser.extract_text_by_page(file)

    if len(pages_text) == 1 and pages_text[0].startswith("Error:"):
        return {"session_id": None, "pages": [{"page": 1, "summary": pages_text[0]}]}

    summarized_pages = []
    for i, page_text in enumerate(pages_text):
        summary = ""
        if page_text and not page_text.isspace():
            summary = ai_handler.summarize_text_with_cerebras(page_text)
        else:
            summary = "(No significant text on this page)"
        summarized_pages.append({"page": i + 1, "summary": summary})

    return {
        "session_id": "real_session_abc123",
        "pages": summarized_pages,
    }

@app.post("/ask")
async def ask_question(request: AskRequest):
    # TODO: Implement LLaMA Q&A logic
    answer = f"This is the answer to: {request.query}"
    return {"answer": answer}

