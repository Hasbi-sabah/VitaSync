import qrcode

def generate_qr_code(user_id):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(user_id)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save or display the image
    img.save(f"{id}.png")

# Example usage
user_id = "5d4c0dbf-79de-40e6-9476-14133992f93c"
generate_qr_code(user_id)
