import streamlit as st
from PIL import Image

st.title("🐢 Mundo Tortuga 🐢")

st.header("¡Bienvenidos a mi app sobre tortugas!")
st.write("Aquí celebramos lo geniales que son estos animalitos.")
image = Image.open('tortuguita.jpg')  # Asegúrate de tener una imagen con este nombre

st.image(image, caption='Hermosa tortuguita')

texto = st.text_input('Cuéntame algo curioso:', '¿Sabías que algunas tortugas viven más de 100 años?')
st.write('Tú dijiste:', texto)

st.subheader("¡Amo las tortugas!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Razón 1: Son muy tranquilas")
    st.write("¿No crees?")
    resp = st.checkbox('Totalmente de acuerdo')
    if resp:
        st.write("¡Somos almas tranquilas!")

with col2:
    st.subheader("Razón 2: Son muy:")
    modo = st.radio("Elige una opción", ('sabias', 'pacientes', 'tiernas'))
    if modo == 'sabias':
        st.write('Con esos ojos, lo han visto todo')
    if modo == 'pacientes':
        st.write('Van despacio, pero seguras')
    if modo == 'tiernas':
        st.write('¡Demasiado tiernas!')

st.subheader("Haz clic para darle cariño a la tortuga")
if st.button("caricias y lechuguitas"):
    st.write("¡La tortuguita sonríe lentamente!")
else:
    st.write("La tortuga te observa con serenidad...")

st.subheader("Elige el nombre de tu tortuga")
in_mod = st.selectbox(
    "Elige con cariño",
    ("Caparazoncito", "Lentilina", "Don Tortugo"),
)
if in_mod == "Caparazoncito":
    set_mod = "¡Nombre adorable!"
elif in_mod == "Lentilina":
    set_mod = "¡Suena a sabiduría!"
elif in_mod == "Don Tortugo":
    set_mod = "¡Suena respetable!"
st.write("Buena elección,", set_mod)
