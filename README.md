here, i first created a virtual environment to install the packages in that specific environment.
i then made seperate folders for each task like model folder have everything related to model. a trained model file, prediction code etc.
schema filee: this folder has the pydantic code, it did validation for both , the data received from the user as well as the response of the fastapi (model prediction result)
config file: it has some basic python list. kind of part of the dataset.
app.py: the main file