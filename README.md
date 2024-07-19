## CO2_EMISSIONS_PREDICTOR_FROM_AUTOMOBILES

"The objective of this project is to analyze the predominant environmental pollutant, CO2, and explore its underlying causes and sources. Additionally, I  developed a robust machine- learning model to assist stakeholders in mitigating its impact. My focus lies in creating a predictive model that empowers automobile designers to forecast CO2 emissions resulting from feature modifications. Furthermore, I aim to provide consumers with insights into the environmental consequences of their vehicle choices."

## EDA 
Review the "CO2_Prediction.ipynb" and "Project_Report_co2_emissions.docx" files to understand the detailed data analyses I conducted to identify the problem.

<img width="826" alt="Screenshot 2024-07-18 at 9 09 24 PM" src="https://github.com/user-attachments/assets/b2bdc6db-a117-4605-90cf-cd6ad0723b31">

## STEPS TO GET THE PREDICTION OUTPUT and SHAP Explainations

 Download and Upload the "target_encoder.pkl", "scaler.pkl" and "best_model.pkl" files in the "Predictor.ipynb" file ( code to upload these artifacts provided in the Predictor.ipynb file) :

 Load the files:

 Enter the input values, Run the scoring function and get the output prediction:

 Interpret the model prediction using SHAP values for that prediction.


Note: (SHAP values are a way to explain prediction models by quantifying the impact each feature has on the prediction. Each SHAP value is a number that represents how much a given feature contributes to pushing the model's prediction away from the baseline, or expected value, for that prediction,
Baseline (Expected Value): This is the average prediction across all data points in the training set or another reference point determined by the model. It's what the model would predict if it didn't know any specific information about the data point in question)
