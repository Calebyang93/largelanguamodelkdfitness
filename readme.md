# Lib Dependencies 
pip libraries. Check python pip packages by running pip freeze on any python library (django, flask etc)

asgiref==3.8.1
astroid==2.4.1
asttokens==3.0.0
backcall==0.2.0
backports.zoneinfo==0.2.1
blinker==1.8.2
certifi==2024.7.4
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.3
comm==0.2.3
dash==2.17.1
dash-core-components==2.0.0
dash-html-components==2.0.0
dash-table==5.0.0
debugpy==1.8.15
decorator==5.2.1
distlib==0.3.8
Django==2.1.15
django-crispy-forms==2.3
django-extensions==3.2.3
django-pyodbc-azure==2.1.0.0
et-xmlfile==1.0.1
executing==2.2.0
filelock==3.15.4
flash==1.0.3
Flask==3.0.3
Flask-JWT-Extended==4.6.0
Flask-SQLAlchemy==3.1.1
greenlet==3.0.3
idna==3.7
importlib_metadata==8.2.0
ipykernel==6.29.5
ipython==8.12.3
isort==4.3.21
itsdangerous==2.2.0
jdcal==1.4.1
jedi==0.19.2
Jinja2==3.1.4
joblib==1.0.1
jupyter_client==8.6.3
jupyter_core==5.8.1
lazy-object-proxy==1.4.3
MarkupSafe==2.1.5
matplotlib-inline==0.1.7
mccabe==0.6.1
nest-asyncio==1.6.0
nltk==3.6.1
numpy==1.24.4
openpyxl==3.0.3
packaging==24.1
pandas==2.0.3
parso==0.8.4
pickleshare==0.7.5
pika==1.3.2
platformdirs==4.2.2
plotly==5.23.0
prompt_toolkit==3.0.51
psutil==7.0.0
pure_eval==0.2.3
Pygments==2.19.2
PyJWT==2.9.0
pylint==2.5.2
pyodbc==5.1.0
python-dateutil==2.9.0.post0
pytz==2024.1
pywin32==311
pyzmq==27.0.0
regex==2021.4.4
requests==2.32.3
retrying==1.3.4
six==1.14.0
SQLAlchemy==2.0.32
sqlparse==0.5.1
stack-data==0.6.3
tenacity==9.0.0
toml==0.10.0
tornado==6.4.2
tqdm==4.60.0
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2024.1
urllib3==2.2.2
virtualenv==20.26.3
wcwidth==0.2.13
Werkzeug==3.0.3
wrapt==1.12.1
zipp==3.20.0

# Running django project 
1. run ```python manage.py runserver on kidfitness directory in your project 
2. run ```python manage.py createsuperuser on kdfintess directory in project to create super user to add tables of mock data on localhost:8080
3. run ``python manage.py makemigrations and ```python manage.py migrate to apply database migrations.

# Test Conditions in Django: Unit Tests 
data model files are in sqlalchemy_models.py in product django app
mock data files are in yaml format in products/fixtures
current mock data files include supplements, racquets, sportwear, mealprepplans,weights, customerservice etc
products/fixtures/supplements.yaml
products/fixtures/racquets.yaml
products/fixtures/sportswear.yaml
products/fixtures/weights.yaml
products/fixtures/mealportionplans.yaml
products/fixtures/customerservice.yaml 

Fixture mock data files can be done in JSON format as well. 

1. Load fixture data using loaddata command in django 
``` python manage.py loaddata products/fixtures/supplements.yaml 
``` python manage.py loaddata products/fixtures/racquets.yaml
```python manage.py loaddata products/fixtures/sportswear.yaml
```python manage.py loaddata products/fixtures/weights.yaml
```python manage.py loaddata products/fixtures/mealportionplan.yaml 
```python manage.py loaddata products/fixtures/customerservice.yaml 

2. For clearing database competely before loading fixture data, run flush commands in django 
``` python manage.py flush 
``` python manage.py loaddata products/fixtures/supplements.yaml 
``` python manage.py loaddata products/fixtures/racquets.yaml
```python manage.py loaddata products/fixtures/sportswear.yaml
```python manage.py loaddata products/fixtures/weights.yaml
```python manage.py loaddata products/fixtures/mealportionplan.yaml 
```python manage.py loaddata products/fixtures/customerservice.yaml 

Data Loading from MSSQL, Auto Generate Models 
1. Use inspectdb command in django 
``` python manage.py inspectdb 
For unix operations run 
``` python manage.py inspectdb > models.db
or replace models.db with the name of the model file in your database (mssql)
2. Install core django tables 
```python manage.py migrate 


This project is run on django. future iterations will implement large language models using jupyternotebook and data visuals can be done with mathplot libraries. For more documentation on django check out: https://docs.djangoproject.com/

# For setting up LLM 
1. Building a Large Language Model (LLM) within a Jupyter Notebook environment using Python involves several key steps, whether you are building from scratch, fine-tuning, or customizing.
1. Setting up the Environment:
Install JupyterLab/Jupyter Notebook: Ensure you have a recent version (JupyterLab 4.x or Jupyter Notebook 7+). You can install it using pip:
Code
    pip3 install jupyter
    pip install jupyterlab
Create a Virtual Environment (Recommended): Isolate your project's dependencies to avoid conflicts.
Code

    python -m venv llm_env
    source llm_env/bin/activate  # On Windows: llm_env\Scripts\activate
Install Necessary Libraries: Install libraries for LLM development, such as:
PyTorch or TensorFlow: For building and training models.
Transformers (Hugging Face): For accessing pre-trained models and tools for fine-tuning.
Numpy, Pandas: For data manipulation.
Matplotlib, Seaborn: For data visualization.
Code

    pip install torch transformers numpy pandas matplotlib
Install Jupyter AI (Optional but Recommended): For an enhanced LLM experience within Jupyter, including chat, code generation, and inline completions.
Code

    pip install "jupyter-ai[all]"
# 2. Building or Utilizing the LLM:
Data Preparation:
Load and preprocess your text data within Jupyter Notebook cells. This may involve tokenization, creating embeddings, and preparing input/target pairs.
Model Definition:
From Scratch: Define the architecture of your LLM using frameworks like PyTorch or TensorFlow, including layers like embedding layers, recurrent layers (e.g., GRU, LSTM), and dense layers.
Fine-tuning/Customizing Pre-trained Models: Load a pre-trained model from Hugging Face's Transformers library and fine-tune it on your specific dataset for a particular task (e.g., text generation, summarization).
Training:
Implement the training loop within your notebook, including forward passes, loss calculation, backpropagation, and optimization.
Evaluation:
Evaluate the model's performance on a validation set using appropriate metrics.
3. Interacting with the LLM in Jupyter:
Code Cells:
Write and execute Python code in cells to define, train, and interact with your LLM.
Jupyter AI (if installed):
Utilize the Jupyter AI chat interface for direct interaction with your loaded LLM, or leverage its inline completion and code generation features.
Visualization:
Use libraries like Matplotlib to visualize training progress, attention mechanisms, or other model insights.
By following these steps, you can effectively build, train, and interact with large language models within the interactive and iterative environment of a Jupyter Notebook.