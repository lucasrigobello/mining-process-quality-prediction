import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import logging

import pandas as pd
import joblib
import yaml

from utils.functions import preparar_dado_predict
from classes.dataset import Test_Data
## =====================================================================
## Inicio do serviço Fast API
## =====================================================================

# Read Features Confing YAML file
with open("./src/config/swagger_documentation.yaml", 'r', encoding='utf-8') as stream:
    conf_swagger = yaml.safe_load(stream)

# Iniciando FastAPI
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(**conf_swagger)

# #===========================================
# # Read Features Confif YAML file
with open("./src/config/conf.yaml", 'r') as stream:
    conf_features = yaml.safe_load(stream)

#===========================================
# Rota da Prediçao da Predição de RUL
@app.post("/predict", tags=["Predict"])
async def predict(data: Test_Data):

    try:
        # carregar o dado para o predict    
        X = preparar_dado_predict(data)
        
        # carregar o modelo e fazer predição
        modelo = joblib.load("./src/models/prediction_RandomForestRegressor.joblib") 
        pred = modelo.predict(X)

    except Exception as e:
        logger.exception("Unhandled error in get_user endpoint")
        raise HTTPException(status_code=500, detail="Internal server error")
    
    return  {conf_features['target_prediction']: pred[0]}

#===========================================
# Iniciando web server
if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        logger.exception("Unhandled error in get_user endpoint")
        raise HTTPException(status_code=500, detail="Internal server error")