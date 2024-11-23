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
    "Hemoglobina (subunidad beta)": (
        "MTQTPYEVIGQERLYQLIDHFYSLVEQDNRINHLFPGDFAETARKQKQFLTQFLGGPDLYTQEHGHPMLRMRHLPFPIDDKAKEAWLENMHTAITHAQLPHGAGDYLYERLRLTANHMVNIEN"
    ),
    "Colágeno (fragmento)": (
        "MHPGLWLLLVTLCLTEELAAAGEKSYGKPCGGQDCSGSCQCFPEKGARGRPGPIGIQGPTGPQGFTGSTGLSGLKGERGFPGLLGPYGPKGDKGPMGVPGFLGINGIPGHPGQPGPRGPPGLDGCNGTQGAVGFPGPDGYPGLLGPPGLPGQKGSKGDPVLAPGSFKGMKGDPGLPGLDGITGPQGAPGFPGAVGPAGPPGLQGPPGPPGPLGPDGNMGLGFQGEKGVKGDVGLPGPAGPPPSTGELEFMGFPKGKKGSKGEPGPKGFPGISGPPGFPGLGTTGEKGEKGEKGIPGLPGPRGPMGSEGVQGPPGQQGKKGTLGFPGLNGFQGIEGQKGDIGLPGPDVFIDIDGAVISGNPGDPGVPGLPGLKGDEGIQGLRGPSGVPGLPALSGVPGALGPQGFPGLKGDQGNPGRTTIGAAGLPGRDGLPGPPGPPGPPSPEFETETLHNKESGFPGLRGEQGPKGNLGLKGIKGDSGFCACDGGVPNTGPPGEPGPPGPWGLIGLPGLKGARGDRGSGGAQGPAGAPGLVGPLGPSGPKGKKGEPILSTIQGMPGDRGDSGSQGFRGVIGEPGKDGVPGLPGLPGLPGDGGQGFPGEKGLPGLPGEKGHPGPPGLPGNGLPGLPGPRGLPGDKGKDGLPGQQGLPGSKGITLPCIIPGSYGPSGFPGTPGFPGPKGSRGLPGTPGQPGSSGSKGEPGSPGLVHLPELPGFPGPRGEKGLPGFPGLPGKDGLPGMIGSPGLPGSKGATGDIFGAENGAPGEQGLQGLTGHKGFLGDSGLPGLKGVHGKPGLLGPKGERGSPGTPGQVGQPGTPGSSGPYGIKGKSGLPGAPGFPGISGHPGKKGTRGKKGPPGSIVKKGLPGLKGLPGNPGLVGLKGSPGSPGVAGLPALSGPKGEKGSVGFVGFPGIPGLPGISGTRGLKGIPGSTGKMGPSGRAGTPGEKGDRGNPGPVGIPSPRRPMSNLWLKGDKGSQGSAGSNGFPGPRGDKGEAGRPGPPGLPGAPGLPGIIKGVSGKPGPPGFMGIRGLPGLKGSSGITGFPGMPGESGSQGIRGSPGLPGASGLPGLKGDNGQTVEISGSPGPKGQPGESGFKGTKGRDGLIGNIGFPGNKGEDGKVGVSGDVGLPGAPGFPGVAGMRGEPGLPGSSGHQGAIGPLGSPGLIGPKGFPGFPGLHGLNGLPGTKGTHGTPGPSITGVPGPAGLPGPKGEKGYPGIGIGAPGKPGLRGQKGDRGFPGLQGPAGLPGAPGISLPSLIAGQPGDPGRPGLDGERGRPGPAGPPGPPGPSSNQGDTGDPGFPGIPGFSGLPGELGLKGMRGEPGFMGTPGKVGPPGDPGFPGMKGKAGARGSSGLQGDPGQTPTAEAVQVPPGPLGLPGIDGIPGLTGDPGAQGPVGLQGSKGLPGIPGKDGPSGLPGPPGALGDPGLPGLQGPPGFEGAPGQQGPFGMPGMPGQSMRVGYTLVKHSQSEQVPPCPIGMSQLWVGYSLLFVEGQEKAHNQDLGFAGSCLPRFSTMPFIYCNINEVCHYARRNDKSYWLSTTAPIPMMPVSQTQIPQYISRCSVCEAPSQAIAVHSQDITIPQCPLGWRSLWIGYSFLMHTAAGAEGGGQSLVSPGSCLEDFRATPFIECSGARGTCHYFANKYSFWLTTVEERQQFGELPVSETLKAGQLHTRVSRCQVCMKSL"
    ),
}

# Título de la aplicación
st.title("Secuencias de Aminoácidos de Proteínas")

# Descripción


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
    st.info("Por favor, selecciona una proteína para ver la secuencia.")
        
#PROPORCION DE  ATOMOS

import matplotlib.pyplot as plt

# Datos de la proporción de átomos de las proteínas
proteins = {
    "Insulina": {"C": 258, "H": 384, "O": 114, "N": 64, "S": 6},
    "Glucagón": {"C": 153, "H": 225, "O": 49, "N": 40, "S": 2},
    "Hemoglobina": {"C": 2954, "H": 4664, "O": 832, "N": 780, "S": 8},
    "Colágeno": {"C": 1590, "H": 2515, "O": 435, "N": 380, "S": 6},
}

# Función para graficar
def plot_atom_proportion(protein_name, atom_counts):
    atoms = list(atom_counts.keys())
    counts = list(atom_counts.values())
    
    fig, ax = plt.subplots()
    ax.pie(counts, labels=atoms, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
    ax.set_title(f"Proporción de átomos en {protein_name}")
    return fig

# Título
st.title("Proporción de átomos en proteínas")

# Descripción
st.write("Este programa muestra la proporción de átomos en diferentes proteínas. Selecciona una proteína para ver su gráfica.")

# Selección de proteína
selected_protein = st.selectbox("Selecciona una proteína:", list(proteins.keys()))

# Obtener datos de la proteína seleccionada
atom_data = proteins[selected_protein]

# Mostrar los datos en una tabla
st.subheader(f"Datos de {selected_protein}")
st.write(atom_data)

# Generar la gráfica
fig = plot_atom_proportion(selected_protein, atom_data)

# Mostrar la gráfica
st.pyplot(fig)


#FACTOR B


