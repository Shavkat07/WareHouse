from fpdf import FPDF
from datetime import datetime
from data import load_data_from_file

def get_filters():
    """Foydalanuvchidan qo'shimcha filtrlash parametrlarini so'rash."""
    print("\nQo'shimcha filtrlash:")
    transaction_type = input("Tranzaktsiya turi (import/export yoki bo'sh qoldiring): ").strip()
    product_names = input("Tovar nomlarini kiriting (vergul bilan ajrating yoki bo'sh qoldiring): ").strip()
    product_names = [name.strip() for name in product_names.split(',')] if product_names else []
    return transaction_type, product_names

def generate_report():
    """Hisobot yaratish funksiyasi."""
    transactions = load_data_from_file(file_name='transactions', param_key='all')
    start_date = datetime.fromisoformat(input("Boshlanish sanasini kiriting (yyyy-mm-dd): "))
    end_date = datetime.fromisoformat(input("Tugash sanasini kiriting (yyyy-mm-dd): "))
    transaction_type, product_names = get_filters()

    file_name = 'report.pdf'
    kelgan_tovarlar = 0
    chiqarilgan_tovarlar = 0
    umumiy_summa = 0.0
    filtered_data = []
    product_totals = {}
    total_quantity = 0
    total_value = 0.0
    product_sales = {}

    for i in transactions:
        if start_date <= datetime.fromisoformat(i['date']) <= end_date:
            # Filtrlash shartlari
            if (not transaction_type or i['transaction_type'] == transaction_type) and \
                    (not product_names or i.get('product_name') in product_names):
                filtered_data.append(i)
                if i['transaction_type'] == 'import':
                    kelgan_tovarlar += 1
                elif i['transaction_type'] == 'export':
                    chiqarilgan_tovarlar += 1

                # Narxni hisoblash
                try:
                    narx = float(i.get('price', 0))
                    miqdor = int(i.get('quantity', 0))
                    umumiy = narx * miqdor
                    umumiy_summa += umumiy

                    product_name = i.get('product_name')
                    if product_name:
                        if product_name not in product_totals:
                            product_totals[product_name] = 0
                        product_totals[product_name] += umumiy

                        # Umumiy miqdor va qiymatni hisoblash
                        total_quantity += miqdor
                        total_value += umumiy

                        # Maxsulot sotilishi haqida ma'lumot
                        if product_name not in product_sales:
                            product_sales[product_name] = 0
                        product_sales[product_name] += miqdor

                except (ValueError, TypeError) as e:
                    print(f"Xato: Tranzaktsiyadagi narx yoki miqdor noto'g'ri formatda. Ma'lumot: {i}")

    # Maxsulot bo'yicha eng ko'p sotilganini topish
    max_selling_product = max(product_sales, key=product_sales.get, default=None)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=8)

    pdf.cell(200, 10, txt="Hisobot", ln=True, align='C')
    pdf.cell(200, 10, txt=f"{start_date.date()} dan {end_date.date()} gacha", ln=True, align='C')

    if transaction_type:
        pdf.cell(200, 10, txt=f"Tranzaktsiya turi: {transaction_type}", ln=True, align='C')
    if product_names:
        pdf.cell(200, 10, txt=f"Tovar nomlari: {', '.join(product_names)}", ln=True, align='C')

    pdf.ln(10)
    pdf.cell(0, 10, txt=f"Kelgan tovarlar: {kelgan_tovarlar}", ln=True)
    pdf.cell(0, 10, txt=f"Chiqib ketgan tovarlar: {chiqarilgan_tovarlar}", ln=True)
    pdf.cell(0, 10, txt=f"Umumiy summa: {umumiy_summa} so'm", ln=True)
    pdf.ln(10)

    # Har bir tranzaktsiya haqida qo'shimcha ma'lumotlar va narxni chiqarish
    for item in filtered_data:
        narx = float(item.get('price', 0))
        miqdor = int(item.get('quantity', 0))
        umumiy = narx * miqdor
        supplier = item.get('supplier', 'N/A')
        transaction_id = item.get('transaction_id', 'N/A')

        pdf.cell(0, 10,
                 txt=f"Sana: {item['date']}, Turi: {item['transaction_type']}, "
                     f"Miqdor: {miqdor}, Narx: {narx} so'm, Umumiy: {umumiy} so'm, "
                     f"Yetkazib beruvchi: {supplier}, Tranzaktsiya ID: {transaction_id}",
                 ln=True)

    # Har bir tovarning umumiy narxini chiqarish
    pdf.ln(10)
    for product, total in product_totals.items():
        pdf.cell(0, 10, txt=f"{product} ning umumiy narxi: {total} so'm", ln=True)

    # Umumiy summary (o'rtacha narx, eng ko'p sotilgan tovar)
    if total_quantity > 0:
        avg_price = total_value / total_quantity
        pdf.ln(10)
        pdf.cell(0, 10, txt=f"O'rtacha narx: {avg_price:.2f} so'm", ln=True)
        if max_selling_product:
            pdf.cell(0, 10, txt=f"Eng ko'p sotilgan tovar: {max_selling_product}", ln=True)

    pdf.output(file_name)
    print(f"Hisobot saqlandi: {file_name}")
