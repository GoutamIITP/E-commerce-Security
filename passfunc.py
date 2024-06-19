import pickle
import numpy as np



# Load the pre-trained vectorizer from a pickle file
def load_vectorizer():
    with open("tfidf_password_strength.pickle", 'rb') as file:
        saved_vectorizer = pickle.load(file)
    return saved_vectorizer

# Load the pre-trained model from a pickle file
def load_passmodel():
    with open("final_model.pickle", 'rb') as file:
        final_model = pickle.load(file)
    return final_model

# def word_divide_char(inputs):
#     character = []
#     for i in inputs:
#         character.append(i)
#     return character
# def word_divide_char(password):
#     return list(password)

def check_password_strength(exampleInputpassword1, saved_vectorizer, final_model):
    password = np.array([exampleInputpassword1])
    # password_str = ''.join(password_chars)
    vectorized_password = saved_vectorizer.transform(password)
    prediction = final_model.predict(vectorized_password)
    return prediction
