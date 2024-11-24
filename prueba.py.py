# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-QWos-bqSCXwnOkdiGVlXGhPGm5DgXbV
"""
#
# Install streamlit library

# Then import the library as usual in the script.
import streamlit as st
from Bio import Entrez, SeqIO


# Secuencias de aminoácidos de las proteínas
proteins = {
    "Insulina": (
        "MALWMRLLPLLALLALWGPDPAAA"
        "FGPGGPLALTLSSSINQEGASQSTSQP"
        "LNSRWQRPVEEQELLPCEDPQVP"
    ),
    "Glucagón": "MKSIYFVAGLFVMLVQGSWQRSLQDTEEKSRSFSASQADPLSDPDQMNEDKRHSQGTFTSDYSKYLDSRRAQDFVQWLMNTKRNRNNIAKRHDEFERHAEGTFTSDVSSYLEGQAAKEFIAWLVKGRGRRDFPEEVAIVEELGRRHADGSFSDEMNTILDNLAARDFINWLIQTKITDRK",
    "Hemoglobina": (
        "MTQTPYEVIGQERLYQLIDHFYSLVEQDNRINHLFPGDFAETARKQKQFLTQFLGGPDLYTQEHGHPMLRMRHLPFPIDDKAKEAWLENMHTAITHAQLPHGAGDYLYERLRLTANHMVNIEN"
    ),
    "Colágeno": (
        "MHPGLWLLLVTLCLTEELAAAGEKSYGKPCGGQDCSGSCQCFPEKGARGRPGPIGIQGPTGPQGFTGSTGLSGLKGERGFPGLLGPYGPKGDKGPMGVPGFLGINGIPGHPGQPGPRGPPGLDGCNGTQGAVGFPGPDGYPGLLGPPGLPGQKGSKGDPVLAPGSFKGMKGDPGLPGLDGITGPQGAPGFPGAVGPAGPPGLQGPPGPPGPLGPDGNMGLGFQGEKGVKGDVGLPGPAGPPPSTGELEFMGFPKGKKGSKGEPGPKGFPGISGPPGFPGLGTTGEKGEKGEKGIPGLPGPRGPMGSEGVQGPPGQQGKKGTLGFPGLNGFQGIEGQKGDIGLPGPDVFIDIDGAVISGNPGDPGVPGLPGLKGDEGIQGLRGPSGVPGLPALSGVPGALGPQGFPGLKGDQGNPGRTTIGAAGLPGRDGLPGPPGPPGPPSPEFETETLHNKESGFPGLRGEQGPKGNLGLKGIKGDSGFCACDGGVPNTGPPGEPGPPGPWGLIGLPGLKGARGDRGSGGAQGPAGAPGLVGPLGPSGPKGKKGEPILSTIQGMPGDRGDSGSQGFRGVIGEPGKDGVPGLPGLPGLPGDGGQGFPGEKGLPGLPGEKGHPGPPGLPGNGLPGLPGPRGLPGDKGKDGLPGQQGLPGSKGITLPCIIPGSYGPSGFPGTPGFPGPKGSRGLPGTPGQPGSSGSKGEPGSPGLVHLPELPGFPGPRGEKGLPGFPGLPGKDGLPGMIGSPGLPGSKGATGDIFGAENGAPGEQGLQGLTGHKGFLGDSGLPGLKGVHGKPGLLGPKGERGSPGTPGQVGQPGTPGSSGPYGIKGKSGLPGAPGFPGISGHPGKKGTRGKKGPPGSIVKKGLPGLKGLPGNPGLVGLKGSPGSPGVAGLPALSGPKGEKGSVGFVGFPGIPGLPGISGTRGLKGIPGSTGKMGPSGRAGTPGEKGDRGNPGPVGIPSPRRPMSNLWLKGDKGSQGSAGSNGFPGPRGDKGEAGRPGPPGLPGAPGLPGIIKGVSGKPGPPGFMGIRGLPGLKGSSGITGFPGMPGESGSQGIRGSPGLPGASGLPGLKGDNGQTVEISGSPGPKGQPGESGFKGTKGRDGLIGNIGFPGNKGEDGKVGVSGDVGLPGAPGFPGVAGMRGEPGLPGSSGHQGAIGPLGSPGLIGPKGFPGFPGLHGLNGLPGTKGTHGTPGPSITGVPGPAGLPGPKGEKGYPGIGIGAPGKPGLRGQKGDRGFPGLQGPAGLPGAPGISLPSLIAGQPGDPGRPGLDGERGRPGPAGPPGPPGPSSNQGDTGDPGFPGIPGFSGLPGELGLKGMRGEPGFMGTPGKVGPPGDPGFPGMKGKAGARGSSGLQGDPGQTPTAEAVQVPPGPLGLPGIDGIPGLTGDPGAQGPVGLQGSKGLPGIPGKDGPSGLPGPPGALGDPGLPGLQGPPGFEGAPGQQGPFGMPGMPGQSMRVGYTLVKHSQSEQVPPCPIGMSQLWVGYSLLFVEGQEKAHNQDLGFAGSCLPRFSTMPFIYCNINEVCHYARRNDKSYWLSTTAPIPMMPVSQTQIPQYISRCSVCEAPSQAIAVHSQDITIPQCPLGWRSLWIGYSFLMHTAAGAEGGGQSLVSPGSCLEDFRATPFIECSGARGTCHYFANKYSFWLTTVEERQQFGELPVSETLKAGQLHTRVSRCQVCMKSL"
    ),
}

# Título de la aplicación
st.title("Secuencias de Aminoácidos de Proteínas")



# Selector de proteínas
selected_protein = st.selectbox("Selecciona una proteína:", list(proteins.keys()))

# Mostrar la secuencia de aminoácidos
if selected_protein:
    st.subheader(f"Secuencia de {selected_protein}:")
    sequence = proteins[selected_protein]
    st.code(sequence, language="plain")

    # Opcional: mostrar longitud de la secuencia
    st.write(f"**Longitud de la secuencia:** {len(sequence)} aminoácidos")

    # Botón para copiar la secuencia
    st.download_button(
        label="Descargar Secuencia",
        data=sequence,
        file_name=f"{selected_protein}_secuencia.txt",
        mime="text/plain",
    )
else:
    st.info("Selecciona una proteína para ver la secuencia.")

#PROPORCION DE  Aminoacidos
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter

# Función para calcular la proporción de átomos
def calcular_proporcion(proteina):
    # Definir las proteínas y sus secuencias
    proteinas = {
        "Insulina": "MALWMRLLPLLALLALWGPDPAAAFGPGGPLALTLSSSINQEGASQSTSQPLNSRWQRPVEEQELLPCEDPQVP",  # Reemplaza con la secuencia real de insulina
        "Glucagon": "MKSIYFVAGLFVMLVQGSWQRSLQDTEEKSRSFSASQADPLSDPDQMNEDKRHSQGTFTSDYSKYLDSRRAQDFVQWLMNTKRNRNNIAKRHDEFERHAEGTFTSDVSSYLEGQAAKEFIAWLVKGRGRRDFPEEVAIVEELGRRHADGSFSDEMNTILDNLAARDFINWLIQTKITDRK",  # Reemplaza con la secuencia real de glucagón
        "Hemoglobina": "MTQTPYEVIGQERLYQLIDHFYSLVEQDNRINHLFPGDFAETARKQKQFLTQFLGGPDLYTQEHGHPMLRMRHLPFPIDDKAKEAWLENMHTAITHAQLPHGAGDYLYERLRLTANHMVNIEN",  # Reemplaza con la secuencia real de hemoglobina
        "Colageno": "MHPGLWLLLVTLCLTEELAAAGEKSYGKPCGGQDCSGSCQCFPEKGARGRPGPIGIQGPTGPQGFTGSTGLSGLKGERGFPGLLGPYGPKGDKGPMGVPGFLGINGIPGHPGQPGPRGPPGLDGCNGTQGAVGFPGPDGYPGLLGPPGLPGQKGSKGDPVLAPGSFKGMKGDPGLPGLDGITGPQGAPGFPGAVGPAGPPGLQGPPGPPGPLGPDGNMGLGFQGEKGVKGDVGLPGPAGPPPSTGELEFMGFPKGKKGSKGEPGPKGFPGISGPPGFPGLGTTGEKGEKGEKGIPGLPGPRGPMGSEGVQGPPGQQGKKGTLGFPGLNGFQGIEGQKGDIGLPGPDVFIDIDGAVISGNPGDPGVPGLPGLKGDEGIQGLRGPSGVPGLPALSGVPGALGPQGFPGLKGDQGNPGRTTIGAAGLPGRDGLPGPPGPPGPPSPEFETETLHNKESGFPGLRGEQGPKGNLGLKGIKGDSGFCACDGGVPNTGPPGEPGPPGPWGLIGLPGLKGARGDRGSGGAQGPAGAPGLVGPLGPSGPKGKKGEPILSTIQGMPGDRGDSGSQGFRGVIGEPGKDGVPGLPGLPGLPGDGGQGFPGEKGLPGLPGEKGHPGPPGLPGNGLPGLPGPRGLPGDKGKDGLPGQQGLPGSKGITLPCIIPGSYGPSGFPGTPGFPGPKGSRGLPGTPGQPGSSGSKGEPGSPGLVHLPELPGFPGPRGEKGLPGFPGLPGKDGLPGMIGSPGLPGSKGATGDIFGAENGAPGEQGLQGLTGHKGFLGDSGLPGLKGVHGKPGLLGPKGERGSPGTPGQVGQPGTPGSSGPYGIKGKSGLPGAPGFPGISGHPGKKGTRGKKGPPGSIVKKGLPGLKGLPGNPGLVGLKGSPGSPGVAGLPALSGPKGEKGSVGFVGFPGIPGLPGISGTRGLKGIPGSTGKMGPSGRAGTPGEKGDRGNPGPVGIPSPRRPMSNLWLKGDKGSQGSAGSNGFPGPRGDKGEAGRPGPPGLPGAPGLPGIIKGVSGKPGPPGFMGIRGLPGLKGSSGITGFPGMPGESGSQGIRGSPGLPGASGLPGLKGDNGQTVEISGSPGPKGQPGESGFKGTKGRDGLIGNIGFPGNKGEDGKVGVSGDVGLPGAPGFPGVAGMRGEPGLPGSSGHQGAIGPLGSPGLIGPKGFPGFPGLHGLNGLPGTKGTHGTPGPSITGVPGPAGLPGPKGEKGYPGIGIGAPGKPGLRGQKGDRGFPGLQGPAGLPGAPGISLPSLIAGQPGDPGRPGLDGERGRPGPAGPPGPPGPSSNQGDTGDPGFPGIPGFSGLPGELGLKGMRGEPGFMGTPGKVGPPGDPGFPGMKGKAGARGSSGLQGDPGQTPTAEAVQVPPGPLGLPGIDGIPGLTGDPGAQGPVGLQGSKGLPGIPGKDGPSGLPGPPGALGDPGLPGLQGPPGFEGAPGQQGPFGMPGMPGQSMRVGYTLVKHSQSEQVPPCPIGMSQLWVGYSLLFVEGQEKAHNQDLGFAGSCLPRFSTMPFIYCNINEVCHYARRNDKSYWLSTTAPIPMMPVSQTQIPQYISRCSVCEAPSQAIAVHSQDITIPQCPLGWRSLWIGYSFLMHTAAGAEGGGQSLVSPGSCLEDFRATPFIECSGARGTCHYFANKYSFWLTTVEERQQFGELPVSETLKAGQLHTRVSRCQVCMKSL",  # Reemplaza con la secuencia real de colágeno
    }

    # Obtener la secuencia de la proteína seleccionada
    secuencia = proteinas.get(proteina)
    
    if secuencia is None:
        return None

    # Contar los átomos (aminoácidos) presentes en la secuencia
    aa_count = Counter(secuencia)
    
    return aa_count

# Interfaz Streamlit
st.title("Proporción de Aminoacidos en Proteínas")

# Opción para seleccionar la proteína
proteina = st.selectbox("Selecciona una proteína", ["Insulina", "Glucagon", "Hemoglobina", "Colageno"])

# Calcular la proporción de átomos
aa_count = calcular_proporcion(proteina)

if aa_count:
    # Convertir a listas para graficar
    aminoacidos = list(aa_count.keys())
    cantidades = list(aa_count.values())

    # Graficar la proporción de átomos
    plt.figure(figsize=(10, 6))
    plt.bar(aminoacidos, cantidades, color='skyblue')
    plt.xlabel("Aminoácidos")
    plt.ylabel("Cantidad")
    plt.title(f"Proporción de Aminoacidos en la Proteína: {proteina}")
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("No se encontró la secuencia para la proteína seleccionada.")

#ESTRUCTURA 3D

import streamlit as st
import py3Dmol

# Función para renderizar el modelo 3D desde un archivo PDB
def render_protein_from_file(pdb_file):
    try:
        # Leer el contenido del archivo PDB
        pdb_data = pdb_file.read()  # Leer en formato binario
        if isinstance(pdb_data, bytes):
            pdb_data = pdb_data.decode("utf-8")  # Decodificar si es necesario

        # Crear el visualizador 3D con py3Dmol
        view = py3Dmol.view(width=800, height=400)
        view.addModel(pdb_data, "pdb")  # Cargar el modelo en formato PDB
        view.setStyle({"cartoon": {"color": "spectrum"}})  # Estilo del modelo
        view.zoomTo()  # Ajustar zoom

        # Devolver el HTML generado
        return view.render()
    except Exception as e:
        st.error(f"Error al procesar el archivo PDB: {e}")
        return None

# Configuración del dashboard
st.title("Visualización 3D de Proteínas")

# Sidebar para seleccionar proteínas
protein_option = st.sidebar.selectbox(
    "Selecciona una proteína:",
    ["Insulina", "Glucagón", "Hemoglobina", "Colágeno"],
    key="protein_selector"  # Clave única
)

# Subida de archivo
uploaded_file = st.sidebar.file_uploader(
    "Sube un archivo PDB:",
    type=["pdb"],
    key="file_uploader"  # Clave única
)

# Renderizar la estructura 3D
if uploaded_file is not None:
    protein_html = render_protein_from_file(uploaded_file)
    if protein_html:  # Verificar que se generó el HTML
        st.components.v1.html(protein_html, height=500)  # Mostrar el modelo
    else:
        st.warning("No se pudo renderizar el archivo PDB. Verifica el formato.")
else:
    st.info("Sube un archivo PDB para visualizar su estructura 3D.")
