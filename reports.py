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
        print(f"{file_name} topilmadi yoki noto'g'ri formatda.")
        return []

# Hisobot yaratish funksiyasinn
def generate_report(data, start_date, end_date, filename="report.pdf"):
    kelgan_tovarlar = 0
    chiqarilgan_tovarlar = 0
    filtered_data = []

    for i in data:
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

    pdf.output(filename)
    print(f"Hisobot saqlandi: {filename}")

if __name__ == "__main__":
    start_date_input = input("Boshlanish sanasini kiriting (yyyy-mm-dd): ")
    end_date_input = input("Tugash sanasini kiriting (yyyy-mm-dd): ")

    start_date = datetime.fromisoformat(start_date_input)
    end_date = datetime.fromisoformat(end_date_input)

    data = load_data(file_name='transactions.json')
    generate_report(data, start_date, end_date)
