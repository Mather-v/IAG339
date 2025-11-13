from chatbot.data import training_data
from chatbot.model import buid_and_train_model, predict_answer, load_model

def main():
    model, vectorizer, unique_answers = load_model()
    