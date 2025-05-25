from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

app = FastAPI()

# Global DataFrame to hold the uploaded file
licenses_df = pd.DataFrame()

# 1. Upload license file
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    global licenses_df
    contents = file.file.read()
    if file.filename.endswith('.csv'):
        licenses_df = pd.read_csv(BytesIO(contents))
    elif file.filename.endswith('.xlsx'):
        licenses_df = pd.read_excel(BytesIO(contents))
    else:
        return {"error": "Unsupported file type"}
    return {"message": "File uploaded successfully", "rows": len(licenses_df)}

# 2. Classify licenses
@app.post("/classify")
def classify():
    global licenses_df
    if licenses_df.empty:
        return {"error": "No data available. Upload file first."}
    
    # Dummy classification logic (replace with real logic)
    def classify_license(name):
        if 'MIT' in name:
            return 'Open Source'
        elif 'Proprietary' in name:
            return 'Commercial'
        else:
            return 'Other'

    licenses_df["category"] = licenses_df["license_name"].apply(classify_license)
    return {"message": "Classification done", "categories": licenses_df["category"].unique().tolist()}

# 3. Summary of categories
@app.get("/summary")
def get_summary():
    global licenses_df
    if "category" not in licenses_df.columns:
        return {"error": "Data not classified yet. Run /classify first."}
    return licenses_df["category"].value_counts().to_dict()
