# MLOPS Indian Flight Price Prediction

Please give a star to this repo, if you like the project!!!!

In this project we will be predicting flight prices for Indian market which will be deployed to Azure Cloud using Github. Various technologies like Docker, Github Action, Airflow, MLflow and DVC will be incorporated in the project. 

## Phase 1: 
Phase 1 of the project is to get the minimal viable MLOPS project ready. So will be downloading the data using data_ingestion.py file in modular fashion and train the model. Adding functionality of AirFlow, DVC and MLFlow will be int the coming phase. 

## Workflow of Project - ML Pipelines

1. Data Ingestion
2. Data Validation
3. Data Transformation -> Feature Engineering, Data Preprocessing
4. Model Training
5. Model Evaluation

## Workflow for each steps above 

1. Update config/config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the src/entity/config_entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline(Training and Batch Prediction Pipeline)
8. Update the main.py




## Phase 2: Add AirFlow + MongoDB
In Phase 2 we will be adding the functionality to load the data from API using Airflow and store it in MongoDB automatically. 