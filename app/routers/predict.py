from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

router = APIRouter()

# Set up the templates directory
templates = Jinja2Templates(directory="app/templates")

# GET route to render the form
@router.get("/prediction", response_class=HTMLResponse)
async def get_prediction_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# POST route to handle the form submission
@router.post("/prediction", response_class=HTMLResponse)
async def predict_datapoint(request: Request, 
                            carat: float = Form(...), 
                            depth: float = Form(...), 
                            table: float = Form(...),
                            x: float = Form(...), 
                            y: float = Form(...), 
                            z: float = Form(...),
                            cut: str = Form(...), 
                            color: str = Form(...), 
                            clarity: str = Form(...)):
    data = CustomData(
        carat=carat,
        depth=depth,
        table=table,
        x=x,
        y=y,
        z=z,
        cut=cut,
        color=color,
        clarity=clarity
    )

    pred_df = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(pred_df)
    results = round(pred[0], 2)
    
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "pred_df": pred_df.to_dict(orient='records')[0]})

# API route for JSON-based requests
@router.post("/predictAPI")
async def predict_api(data: CustomData):
    pred_df = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(pred_df)
    return {"price": round(pred[0], 2)}
