import streamlit as st
from pdf2docx import Converter  # Certifique-se de instalar essa biblioteca com `pip install pdf2docx`
import os

st.write("CONVERTER PDF PARA DOCX")

# Upload do arquivo
uploaded_file = st.file_uploader("Envie seu arquivo PDF", type=["pdf"])

if uploaded_file is not None:
    # Criação do diretório temporário
    os.makedirs("temp", exist_ok=True)
    
    # Caminhos para salvar o PDF e o DOCX
    pdf_path = os.path.join("temp", uploaded_file.name)
    docx_path = os.path.join("temp", uploaded_file.name.replace(".pdf", ".docx"))
    
    # Salva o PDF carregado
    with open(pdf_path, "wb") as temp_pdf:
        temp_pdf.write(uploaded_file.getbuffer())
    
    # Converte o PDF para DOCX
    st.write("Convertendo o arquivo...")
    converter = Converter(pdf_path)
    converter.convert(docx_path)
    converter.close()
    st.success("Conversão concluída!")
    
    # Adiciona botão para download
    with open(docx_path, "rb") as docx_file:
        st.download_button(
            label="Baixar arquivo DOCX",
            data=docx_file,
            file_name=os.path.basename(docx_path),
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )