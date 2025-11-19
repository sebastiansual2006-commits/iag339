# main.py
from flask import Flask, render_template, request, jsonify
from chatbot.data import training_data
from chatbot.model import build_and_train_model, load_model, predict_cluster
import random
app = Flask(__name__)

# Intentamos cargar el modelo (o entrenamos si no existe)
model, vectorizer = load_model()
if model is None:
    model, vectorizer = build_and_train_model(training_data, n_clusters=6)  # ✅ Número de grupos ajustable

#Respustas por grupo
Respuestas ={
    0:["¡hola! 😎 ¿como estas",
       "¡que gusto saludarte!",
       "¡hola! ¿en que puedo ayudarte?",
       ],
    1:["hasta luego",
          "nosvemos pronto",
          "Cuidate Espero verte de nuevo"
          ],
    2:["soy un asistente virtual creado para audarte",
        "¡por supuesto! ¿con que necesitas ayuda?,",
        "cuetame tu promblema y buscare una solucion",
        ],
    3:["puesto ofrecerte informacion o resolver tus  dudas",
        "¡en que te puedo ayudar",
        "estoy aqui par resolver tus preguntas",
        ],
    4:["¡gracias a ti! ❤️",
        "de nada, me alegro ser de ayuda",
        "¡muy amable de tu parte!",
        ],
    5:[
        "lamento que te sientas asi, puedo intentarlo de nuevo",
        "parece que algo no salio bien, ¿ Quieres que lo revisemos",
        "no siempre soy perfecto, pero puedo intertarlo otra vez",
        ]
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message", "")
    if not user_text.strip():
        return jsonify({"response": "Por favor escribe algo 😅"})

    # Predice el grupo al que pertenece el mensaje
    cluster = predict_cluster(model, vectorizer, user_text)

    # ✅ Mensaje más descriptivo
    #response =f"Tu mensaje pertenece al grupo {cluster}. Este grupo contiene frases con significados similares."
    response = random.choice(Respuestas.get(cluster, [
        "No estoy seguro de entender, pero puede intertarlo otra vez."
     ]))
    
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
