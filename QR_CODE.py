import qrcode
import os
import json

PRODUCTS_FILE = "Database/products.json"

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


