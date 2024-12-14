import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
from categories import add_category
from data import load_data_from_file, save_data_to_file, update_data, delete_data
from suppliers import add_supplier


def create_dynamic_logo(category, logo_size=100):

    logo = Image.new( 'RGBA', (logo_size, logo_size), color=(255, 255, 255, 255) )
    draw = ImageDraw.Draw( logo )

    try:

        font = ImageFont.truetype( "arial.ttf", size=logo_size // 4 )  # Adjust the font size
    except IOError:

        font = ImageFont.load_default()

    text = category[:3].upper()


    bbox = draw.textbbox( (0, 0), text, font=font )
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]


    text_position = ((logo_size - text_width) // 2, (logo_size - text_height) // 2)
    draw.text( text_position, text, font=font, fill="black" )

    return logo


def generate_qr_code_with_dynamic_logo(product):

    qr_data = f"ID: {product['id']}\nName: {product['name']}\nPrice: {product['price']}\nDescription: {product['description']}\nCategory: {product['category']}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data( qr_data )
    qr.make( fit=True )


    qr_img = qr.make_image( fill="black", back_color="white" )

    logo = create_dynamic_logo( product['category'] )


    qr_width, qr_height = qr_img.size
    logo_size = int( qr_width / 4 )
    logo = logo.resize( (logo_size, logo_size) )


    logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)


    qr_img.paste( logo, logo_position, mask=logo.convert( "RGBA" ).split()[3] )


    qr_dir = "./Media/Qrcodes"
    os.makedirs( qr_dir, exist_ok=True )

    qr_filename = os.path.join( qr_dir, f"product_{product['id']}_qr_with_dynamic_logo.png" )
    try:
        qr_img.save( qr_filename )
        print( f"QR code with dynamic logo saved successfully at {qr_filename}" )
    except Exception as e:
        print( f"Error saving QR code with dynamic logo: {e}" )


def add_product():
    """Yangi mahsulot ma'lumotlarini yaratadi va qaytaradi."""
    print( "\nYangi mahsulot ma'lumotlarini kiriting:" )
    product = {
        "id": 0,
        "name": '',
        "price": '',
        "description": '',
        "quantity": '',
        "category": '',
        "supplier_id": 0,
        "warehouse_id": 0
    }

    name = input( "Mahsulot nomi: " )
    product["name"] = name

    price = input( "Narxi: " )
    product["price"] = price

    description = input( "Tavsif: " )
    product["description"] = description

    quantity = int( ''.join( input( "Miqdori: " ).split() ) )
    product["quantity"] = quantity

    category = input( "Kategoriya nomi: " )

    if load_data_from_file( file_name='categories', param_key='name', param_value=category ) is not None:
        product['category'] = category
    else:
        while True:
            question = input( "Bunaqa category hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): " )
            if question == 'yes':
                category_name = add_category()
                product['category'] = category_name
                break
            elif question == 'no':
                print( "Function failed." )
                return

    supplier_id = int( input( "Yetkazib beruvchi ID: " ) )
    if supplier_id != 0 and load_data_from_file( 'suppliers', param_key='id', param_value=supplier_id ) is not None:
        product['supplier_id'] = supplier_id
    else:
        while True:
            question = input( "Bunaqa supplier hali mavjud emas. Yangi qushishni istaysizmi('yes' or 'no'): " )
            if question == 'yes':
                supplier = add_supplier()
                product['supplier_id'] = supplier['id']
                break
            elif question == 'no':
                print( "Function failed." )
                return

    warehouse_id = int( input( "Ombor ID: " ) )

    if load_data_from_file( 'warehouses', param_key='id', param_value=warehouse_id ) is not None:
        product['warehouse_id'] = warehouse_id
    else:
        print( "Function failed." )
        return

    last_product_id = load_data_from_file( 'products', param_key='id' )
    if last_product_id is not None:
        product["id"] = last_product_id + 1
    else:
        product["id"] = 1

    print( "Product Added Successfully" )
    save_data_to_file( file_name='products', data=product )

    warehouse_capacity = load_data_from_file( 'warehouses', param_key='id', param_value=warehouse_id )[
                             'current_capacity'] + quantity
    update_data( file_name='warehouses', obj_id=warehouse_id, param_key='current_capacity',
                 new_param_value=warehouse_capacity )

    # Generate QR code with dynamic logo
    generate_qr_code_with_dynamic_logo( product )

    return product


def delete_product():
    product_id = int( input( "Product id ni kiriting: " ) )
    delete_data( file_name='products', param_key='id', param_value=product_id )
    print( "Product Deleted Successfully" )
    return


def view_products():
    products = load_data_from_file( file_name='products', param_key='all' )
    if products is not None:
        for i in products:
            print( f"""
                Products id: {i['id']}
                Products name is: {i['name']}
                Products category is: {i['category']}
                Products price is : {i['price']}
                Products quantity is : {i['quantity']}  
            """ )
    else:
        print( "Список транзакций пуст." )
    return