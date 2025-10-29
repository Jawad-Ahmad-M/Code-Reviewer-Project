import logging
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/execute", tags=["Execution"])
logger = logging.getLogger("execute")
logging.basicConfig(level=logging.INFO)

PISTON_URL = "https://emkc.org/api/v2/piston/execute"

class CodeRequest(BaseModel):
    language: str
    source_code: str
    stdin: str | None = None

@router.post("")
def execute_code(req: CodeRequest):
    payload = {
        "language": req.language,
        "version": "*",
        "files": [{"name": "main", "content": req.source_code}],
        "stdin": req.stdin or ""
    }
    try:
        response = requests.post(PISTON_URL, json=payload, timeout=10)
        response.raise_for_status()
        piston_result = response.json()
        # Return frontend-friendly output
        return {
            "stdout": piston_result.get("run", {}).get("stdout"),
            "stderr": piston_result.get("run", {}).get("stderr"),
            "exit_code": piston_result.get("run", {}).get("code")
        }
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Execution timed out.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail="Failed to contact Piston API.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

