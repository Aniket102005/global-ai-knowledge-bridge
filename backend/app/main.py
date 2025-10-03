from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from services import ai_handler, parser
import uuid
from fastapi.middleware.cors import CORSMiddleware # 1. Import the CORS middleware

app = FastAPI()

# 2. Add this entire section to configure CORS
origins = [
    "http://localhost:3000", # The address of your React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allow all methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all headers
)
# --- End of CORS configuration ---

# --- Simple In-Memory "Database" for Hackathon ---
sessions_db = {}

class AskRequest(BaseModel):
    session_id: str
    query: str
    language: str = "English"

@app.get("/")
def read_root():
    return {"message": "Global AI Knowledge Bridge Backend is running!"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    pages_text_list = parser.extract_text_by_page(file)

    if len(pages_text_list) == 1 and pages_text_list[0].startswith("Error:"):
        return {"session_id": None, "pages": [{"page": 1, "summary": pages_text_list[0]}]}

    full_text = "\n\n---\n\n".join(pages_text_list)
    session_id = str(uuid.uuid4())
    sessions_db[session_id] = full_text

    summarized_pages = []
    for i, page_text in enumerate(pages_text_list):
        summary = ""
        if page_text and not page_text.isspace():
            summary = ai_handler.summarize_text_with_cerebras(page_text)
        else:
            summary = "(No significant text on this page)"
        summarized_pages.append({"page": i + 1, "summary": summary})

    return {
        "session_id": session_id,
        "pages": summarized_pages,
    }

@app.post("/ask")
async def ask_question(request: AskRequest):
    document_context = sessions_db.get(request.session_id)
    
    if not document_context:
        return {"answer": "Error: Invalid or expired session ID. Please upload the document again."}
        
    answer = ai_handler.get_answer_with_llama(
        context=document_context, 
        question=request.query, 
        language=request.language
    )
    
    return {"answer": answer}

