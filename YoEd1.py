#Prediction and classification WebApp for YoEd
#Import dependencies
import streamlit as st
import pandas as pd
import numpy as np

#Dismiss the encoding message
st.set_option('deprecation.showfileUploaderEncoding', False)

#User interface of the WebApp using Markdown
st.write("""
# Observa el desarrollo _histórico_ de su **aprendizaje**

Conoce cuáles son las **Áreas de Atención** de tu hij@
""")

chart_data = pd.DataFrame({

   'Escuela': [20, 20, 30, 20, 30, 30],
   'Alumno': [20, 30, 30, 40, 40, 40],
   'Familia': [60, 50, 40, 40, 30, 30]

   }, index=["Mes anterior 1", 'Mes anterior 2', 'Mes anterior 3', 'Mes presente', 'Tendencia próximo mes', 'Tendencia próximo mes 2'])

st.line_chart(chart_data)


st.write("""
Acompaña el desarrollo de sus **Inteligencias múltiples**
""")

chart_data2 = pd.DataFrame({

   'Naturalista': [20, 15, 5, 10, 15, 20],
   'Musical': [20, 20, 15, 10, 15, 10],
   'Lógica Matemática': [20, 15, 15, 15, 10, 10],
   'Intrapersonal': [10, 10, 15, 10, 15, 15],
   'Espacial Visual': [10, 5, 10, 15, 5, 15],
   'Interpersonal': [5, 15, 10, 15, 10, 10],
   'Corporal Kinestésica': [5, 10, 15, 15, 10, 10],
   'Lingüística Verbal': [10, 10, 15, 15, 20, 10]

   }, index=["Mes anterior 1", 'Mes anterior 2', 'Mes anterior 3', 'Mes presente', 'Tendencia próximo mes', 'Tendencia próximo mes 2'])

st.line_chart(chart_data2)

st.write("""
Acompaña el desarrollo de sus **Inteligencias emocionales**
""")

chart_data3 = pd.DataFrame({

   'Competencias Emocionales': [5, 15, 10, 15, 10, 10],
   'Desarrollar la inteligencia emocional': [20, 15, 5, 10, 15, 20],
   'Dinámica de las emociones en los niños': [10, 5, 10, 15, 5, 15],
   'En la escuela': [20, 20, 15, 10, 15, 10],
   'Expresión de los sentimientos': [10, 5, 10, 15, 5, 15],
   'Expresión de los sentimientos y emociones en la familia y en la pareja': [5, 10, 15, 15, 10, 10],
   'Modelo esquemático': [20, 15, 15, 15, 10, 10],
   'Modelo por áreas': [10, 10, 15, 10, 15, 15],
   'Objetivos de la educación emocional': [5, 10, 15, 15, 10, 10],
   'Pilares de la educación': [10, 10, 15, 10, 15, 15],
   'Sistema inmunológico': [20, 20, 15, 10, 15, 10],
   'Valores educativos  ': [10, 10, 15, 15, 20, 10]

   }, index=["Mes anterior 1", 'Mes anterior 2', 'Mes anterior 3', 'Mes presente', 'Tendencia próximo mes', 'Tendencia próximo mes 2'])

st.line_chart(chart_data3)

st.subheader('Panel de valoración')

#Apply the model to make predictions on the input
prediction = np.random.randint(4)
prediction_proba = np.random.randint(40, high=70)

#Display the prediction in the screen
st.write('''**_Predicción_**''')
variables_aprendizaje = np.array(['Consultar casos', 'Evaluación de la estimulación del aprendizaje',
 'Valoración de la estimulación del aprendizaje', 'Análisis de la estimulación del aprendizaje'])
st.write(variables_aprendizaje[prediction])

#Display the probability of the prediction made
st.write('''**_Probabilidad de la predicción_**''')
st.write(prediction_proba, '%')
