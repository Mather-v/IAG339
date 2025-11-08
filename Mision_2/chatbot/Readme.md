# Guía de implentación del chatbot, modelo supervisado
pip install scikit-learn
pip install numpy
pip install gym==0.26.2
pip install gym-notices 
pip install nltk

Crear el archivo setup_nltk.py
´´´
import nltk

try: 
    nltk.download('punkt')
    print("NLTK punkt descargado correctamente")
except Exception as e:
    print("Error durante la descarga: ", e)

´´´

´´´

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 

def build_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs]
    answers = [a for _, a in train_pairs]
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(questions)

    unique_answers = sorted(set(answers))
    answer_to_label = {a:i for i, a in enumerate(unique_answers)}
    y = [answer_to_label[a] for a in answers]
    model = MultinomialNB()
    model.fit(x,y)
    return model, vectorizer, unique_answers

def predict_answer(model, vectorizer, unique_answers, user_text):
    x = vectorizer.transform([user_text])
    label = model.predict(x)[0]

    return unique_answers[label]

if __name__ == "__main__":
    training_data =[
        ("hola", "!Hola ¿En qué puedo ayudarte"),
        ("Buenos días", "!Buenos Días¡"),
        ("cómo estás", "Estoy bien, gracias por preguntar"),
        ("adiós", "!Hasta luego¡"),
        ("tu nombre", "Soy un chatbot de ejemplo"),
        ("que puedes hacer", "Puedo reponder preguntas simples basadas en ejemplos", "Deja de hacerme preguntar estupidas, por favor 😊"),
    ]
model, vectorizer, unique_answers = build_and_train_model(training_data)
print("Cahtbot supervisado listo, Escribe 'salir' para terminar")

while True:
    user = input("Tu: ").strip()
    if user.upper() in {"salir", "exit", "quit"}:
        print("Bot: ¡Hasta pronto mierdita!")
    response = predict_answer(model, vectorizer, unique_answers, user)
    print("Bot: ", response)



´´´