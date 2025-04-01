import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename (e.g., qr_code.png): ').strip()

# Ensure the filename has an extension
if not any(filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
    filename += '.png'  # Default to PNG

try:
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)  # Ensure it properly fits the data
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(filename)
    print(f'QR code saved as {filename}')
except Exception as e:
    print(f"Error: {e}")
