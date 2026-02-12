import pandas as pd
import yaml

# #===========================================
# # Read Features Confif YAML file
with open("./src/config/conf.yaml", 'r') as stream:
    conf_features = yaml.safe_load(stream)

#===========================================
# Prepara o dado para realizar predict
def preparar_dado_predict(data):
    
    # load base de dados
    X = pd.DataFrame([data.model_dump()])
    X.columns = conf_features['features']

    return X
