from fpdf import FPDF
import json
from datetime import datetime

from data import load_data_from_file


# Hisobot yaratish funksiyasinn
def generate_report():
    transactions = load_data_from_file(file_name='transactions', param_key='all')
    start_date = datetime.fromisoformat(input("Boshlanish sanasini kiriting (yyyy-mm-dd): "))
    end_date = datetime.fromisoformat(input("Tugash sanasini kiriting (yyyy-mm-dd): "))
    file_name = 'report.pdf'

    kelgan_tovarlar = 0
    chiqarilgan_tovarlar = 0
    filtered_data = []
    for i in transactions:
        if start_date <= datetime.fromisoformat(i['date']) <= end_date:
            filtered_data.append(i)
            if i['transaction_type'] == 'import':
                kelgan_tovarlar += 1
            elif i['transaction_type'] == 'export':
                chiqarilgan_tovarlar += 1

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Hisobot sarlavhasi
    pdf.cell(200, 10, txt="Hisobot", ln=True, align='C')
    pdf.cell(200, 10, txt=f"{start_date} dan {end_date} gacha", ln=True, align='C')

    pdf.ln(10)

    # Statistika
    pdf.cell(0, 10, txt=f"Kelgan tovarlar: {kelgan_tovarlar}", ln=True)
    pdf.cell(0, 10, txt=f"Chiqib ketgan tovarlar: {chiqarilgan_tovarlar}", ln=True)

    pdf.ln(10)

    # Filtrlangan ma'lumotlarni qo'shish
    for item in filtered_data:
        pdf.cell(0, 10, txt=f"Sana: {item['date']}, Turi: {item['transaction_type']}, Miqdor: {item['quantity']}", ln=True)

    pdf.output(file_name)
    print(f"Hisobot saqlandi: {file_name}")

if __name__ == "__main__":

    generate_report()
