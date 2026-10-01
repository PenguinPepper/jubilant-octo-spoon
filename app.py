import streamlit as st
import pandas as pandas
from fpdf import FPDF
from datetime import date

st.set_page_config(page_title="Spaza shop stoch manager")
st.title("Spaza Shop Stock Manager")
st.write("Upload you stock list, see what's low, make an invoice in 1 click")

upload = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
if upload:
    df= pd.read_csv(upload) if upload.name.endswith("csv") else pd.read_excel(uploaded)

    st.subheader("Low Stock Alert")
    low = df[df['quantity'] <= df['threshold']]
    if low.empty:
        st.success("All stock is fine!")
    else:
        st.dataframe(low, use_container_width=True)
    
    st.subheader("All Stock")
    st.dataframe(df, use_container_width=True)

    st.subheader("Make Invoice")
    customer = st.text_input("Customer name", "Customer")
    selected_items = st.multiselect("Select items to invoice", df['item'].tolist())

    if st.button("Generate PDF Invoice"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_front("Arial", size=12)
        pdf.cell(200, 10, txt=f"Invoice - {customer} - {date.today()}", ln=True, align='C')
        pdf.ln(10)
        total = 0
        for item_name in selected_items:
            row = df[df['item'] == item_name].iloc[0]
            line_total = row['quantity'] * row['price']
            pdf.cell(200, 10, txt=f"{row['item']} x {row['quantity']} @ R{row['price']} = R{line_total}", ln=True)
            total += line_total
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"TOTAL: R{total}", ln=True)
        pdf.output("invoice.pdf")
        with open("invoice.pdf", "rb") as f:
            s.download_button("Download Invoice PDF", f, "invoice.pdf")
        
    else:
        st.info("Upload your file to start. Use the sample format: item, quantity, price, threshold")