from setuptools import setup, find_packages

setup(
    name='my_ml_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'category_encoders==2.3.0',
        'shap==0.39.0',
        'scikit-learn==0.24.2',
        'joblib==1.0.1',
    ],
)
