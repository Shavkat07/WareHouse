from os import name

from fpdf import FPDF
import json
from datetime import datetime

# Ma'lumotlarni yuklash funksiyasi
def load_data(file_name='transactions.json', param_key='all', quantity='all'):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"{file_name} topilmadi.")
        return []

# Hisobot yaratish funksiyasi (yangilangan)
def generate_report(data, start_date, end_date, filename="report.pdf"):
    # Import va eksport sanash uchun o'zgaruvchilar
    kelgan_tovarlar = 0
    chiqarilgan_tovarlar = 0

    # Berilgan vaqt oralig'ida filtrlash
    filtered_data = []
    for i in data:
        if start_date <= datetime.fromisoformat(i['date']) <= end_date:
            filtered_data.append(i)
            if i['transaction_type'] == 'import':
                kelgan_tovarlar += 1
            elif i['transaction_type'] == 'export':
                chiqarilgan_tovarlar += 1

    # PDF yaratish jarayoni
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Hisobot sarlavhasi
    pdf.cell( 200, 10, ln=True, align='C' )
    pdf.cell( 200, 10, ln=True, align='C' )

    pdf.ln(10)  # Bo'sh joy qo'shish

    # Statistika qo'shish
    pdf.cell( 0, 10, ln=True )
    pdf.cell( 0, 10, ln=True )

    pdf.ln(10)  # Yana bo'sh joy

    # Filtrlangan ma'lumotlarni qo'shish
    pdf.cell( 0, 10, ln=True )
    for item in filtered_data:
        pdf.cell( 0, 10, ln=True )

    # PDFni saqlash
    pdf.output(filename)
    print(f"Hisobot saqlandi: {filename}")

# Dasturni boshqarish
if name == "main":
    # Foydalanuvchidan vaqt oralig'ini kiritishni so'rash
    start_date_input = input("Boshlanish sanasini kiriting (yyyy-mm-dd): ")
    end_date_input = input("Tugash sanasini kiriting (yyyy-mm-dd): ")

    start_date = datetime.fromisoformat(start_date_input)
    end_date = datetime.fromisoformat(end_date_input)

    # Ma'lumotlarni yuklash
    data = load_data(file_name='transactions.json')

    # Hisobot yaratish
    generate_report(data, start_date, end_date)