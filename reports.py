from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
from data import load_data_from_file


def generate_pdf(file_name):
    start_date = datetime.fromisoformat(input("Boshlanish sanasini kiriting (yyyy-mm-dd): "))
    end_date = datetime.fromisoformat(input("Tugash sanasini kiriting (yyyy-mm-dd): "))
    ustama_foiz = 10
    # Создаем PDF файл
    pdf = canvas.Canvas(file_name, pagesize=A4)
    pdf.setTitle("Hisobot")

    # Устанавливаем базовые параметры
    width, height = A4
    margin = 50
    text_x = margin
    y_position = height - margin

    # Заголовок
    pdf.setFont("Helvetica-Bold", 20)
    pdf.setFillColor(colors.darkblue)
    pdf.drawString(text_x, y_position, "Hisobot")
    y_position -= 40

    # Даты
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(colors.black)
    pdf.drawString(text_x, y_position, "Sana: 2024-12-12 dan 2025-01-01 gacha")
    y_position -= 30

    # Подзаголовок
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(text_x, y_position, "Omborxonalar Statistikasi")
    y_position -= 30

    # Данные по складам (пример для двух складов)
    warehouses = load_data_from_file(file_name="warehouses", param_key="all")

    # Рендеринг данных по каждому складу
    for warehouse in warehouses:
        import_qilingan_tovarlar = 0
        xarajatlar = 0
        kirgan_summa = 0
        export_qilingan_tovarlar = 0
        foyda = 0

        for transaction in load_data_from_file(file_name="transactions", param_key="warehouse_id", param_value=warehouse["id"], quantity="all"):
            if start_date <= datetime.fromisoformat(transaction['date']) <= end_date:
                product = load_data_from_file(file_name="products", param_key="id", param_value=transaction["product_id"])

                if transaction["transaction_type"] == "import":
                    import_qilingan_tovarlar += transaction["quantity"]
                    xarajatlar += transaction["quantity"] * float(product['price'][0:-1])

                else:
                    export_qilingan_tovarlar += transaction["quantity"]
                    kirgan_summa += transaction["quantity"] * (float(product['price'][0:-1]) + float(product['price'][0:-1]) / 100 * ustama_foiz)

                    foyda += kirgan_summa / 100 * ustama_foiz




        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(text_x, y_position, warehouse["location"])
        y_position -= 20

        pdf.setFont("Helvetica", 12)
        pdf.drawString(text_x, y_position, f"    Import qilingan tovarlar soni: {import_qilingan_tovarlar} ta")
        y_position -= 15
        pdf.drawString(text_x, y_position, f"    Export qilingan tovarlar soni: {export_qilingan_tovarlar} ta")
        y_position -= 15
        pdf.drawString(text_x, y_position, f"    Hozirda Mavjud Tovarlar Soni: {warehouse['current_capacity']} ta")
        y_position -= 15
        pdf.drawString(text_x, y_position, f"    Harajatlar: {xarajatlar}$ ")
        y_position -= 15
        pdf.drawString(text_x, y_position, f"    Kirgan summa: {kirgan_summa}$")
        y_position -= 15
        pdf.drawString(text_x, y_position, f"    Foyda: {foyda}$")
        y_position -= 15

        y_position -= 20  # Пробел перед следующим складом

    # Завершаем документ
    pdf.save()

# Генерация PDF файла
generate_pdf("hisobot.pdf")