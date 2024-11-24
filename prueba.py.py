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

# Función para visualizar estructuras 3D
def render_protein(protein_pdb):
    view = py3Dmol.view(width=800, height=400)
    view.addModel(protein_pdb, "pdb")  # Carga el modelo desde el contenido del archivo PDB
    view.setStyle({'cartoon': {'color': 'spectrum'}})  # Estilo de dibujo en forma de "cartoon"
    view.zoomTo()  # Ajusta el zoom para mostrar toda la estructura
    return view

# Diccionario con las proteínas y sus estructuras PDB
protein_structures = {
    "Insulina": """1zei""",  # Reemplaza con la estructura PDB de insulina
    "Glucagon": """7lck.pdb""",  # Reemplaza con la estructura PDB de glucagón
    "Hemoglobina": """1shr.pdb""",  # Reemplaza con la estructura PDB de hemoglobina
    "Colageno": """5nb1"""  # Reemplaza con la estructura PDB de colágeno
}

# Interfaz Streamlit
st.title("Visualización 3D de Proteínas")

# Selector para elegir la proteína
protein_choice = st.selectbox("Selecciona una proteína para visualizar", list(protein_structures.keys()))

# Mostrar la estructura de la proteína seleccionada
if protein_choice:
    st.subheader(f"Estructura 3D: {protein_choice}")
    
    # Obtener el archivo PDB de la proteína seleccionada
    protein_pdb = protein_structures[protein_choice]
    
    # Renderizar la proteína y obtener el HTML
    view = render_protein(protein_pdb)
    view_html = view.render()  # Renderiza el modelo a HTML
    
    # Mostrar la visualización en Streamlit
    st.components.v1.html(view_html, height=500)
