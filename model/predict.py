import pickle
import pandas as pd

with open("model/model.pkl" , "rb") as file:
    model = pickle.load(file)
    
    
MODEL_VERRSION = '1.0.0'

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    
    input_df = pd.DataFrame([user_input]) # dict is converted into a Dataframe
    
    predicted_class = model.predict(input_df)[0] # getting the prediction, predicted class
    
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    class_probs = dict(
        zip(class_labels, map(lambda p: round(p, 4), probabilities))
    )
    
    return {
        'predicted_category': predicted_class,
        'confidence': round(confidence, 4),
        'class_probabilities': class_probs
        
    }