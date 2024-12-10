import qrcode
import os
import json

PRODUCTS_FILE = "products.json"

# Ensure the products file exists
if not os.path.exists( PRODUCTS_FILE ):
    with open( PRODUCTS_FILE, 'w' ) as f:
        json.dump( [], f )


def load_products():
    """Load the products from the JSON file."""
    with open( PRODUCTS_FILE, 'r' ) as f:
        return json.load( f )


def save_products(products):
    """Save products to the JSON file."""
    with open( PRODUCTS_FILE, 'w' ) as f:
        json.dump( products, f, indent=4 )


def generate_qr_code(product_info, product_id):
    """Generate a QR code for a product and save it as an image."""
    qr = qrcode.QRCode(
        version=1,  # Version of the QR code, controls size (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls error correction
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border
    )

    # Add product information to the QR code
    qr.add_data( product_info )
    qr.make( fit=True )

    # Create an image from the QR code
    img = qr.make_image( fill='black', back_color='white' )

    # Save the image file with a unique name
    qr_filename = f"product_qr_{product_id}.png"
    img.save( qr_filename )

    print( f"QR code for product saved as {qr_filename}" )


def add_product():
    """Add a new product to the system with a QR code."""
    product_name = input( "Enter product name: " ).strip()
    product_category = input( "Enter product category: " ).strip()
    product_quantity = int( input( "Enter product quantity: " ) )

    # Create product ID based on current number of products
    products = load_products()
    product_id = len( products ) + 1  # Simple ID generation

    # Create a product entry
    product = {
        "id": product_id,
        "name": product_name,
        "category": product_category,
        "quantity": product_quantity
    }

    # Add the product to the list
    products.append( product )
    save_products( products )

    # Generate product information as a string for the QR code
    product_info = f"ID: {product_id}\nName: {product_name}\nCategory: {product_category}\nQuantity: {product_quantity}"

    # Generate and save the QR code
    generate_qr_code( product_info, product_id )

    print( f"Product {product_name} added successfully with QR code!" )
