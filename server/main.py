import db_connection
import config_parser
from fastapi import FastAPI, UploadFile, File
from typing import List
import uvicorn
from pathlib import Path

app = FastAPI()
config = config_parser.ini_conf("server_config.ini")

db_conn = db_connection.database_conn("server_database.sqlite")
db_conn.insert_data("(product_id, product_files, product_attributes)", "('test1', 'test2', 'test4')")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/introduce_product")
async def introduce_product(files: List[UploadFile] = File(...)):
    REQUIRED_EXTENSIONS = {".kicad_sym", ".kicad_mod", ".step", ".wrl"}
    if len(files) != 4:
        return 401

    uploaded = []
    found_extensions = []
    for file in files:
        extension = Path(file.filename).suffix.lower()
        found_extensions.append(extension)
        contents = await file.read()
        size = len(contents)

        uploaded.append({
            "filename": file.filename,
            "extension": extension,
            "size_bytes": size
        })
        await file.seek(0)

    found_set = set(found_extensions)

    if found_set != REQUIRED_EXTENSIONS:
        return 400

    if len(found_extensions) != len(set(found_extensions)):
        return 400

    return 200

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)