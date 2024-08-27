from pyzbar.pyzbar import decode
from PIL import Image
from PIL.PngImagePlugin import PngImageFile

def decode_qr_code(filename: str) -> str:
    image: PngImageFile = Image.open(filename)
    decoded_qr_code: list = decode(image)
    qr_code_data: str = decoded_qr_code[0][0].decode()
    return qr_code_data

def main() -> None:
    filename: str = "qr_code.png"
    decoded_qr = decode_qr_code(filename)
    print(decoded_qr)
    
if __name__ == "__main__":
    main()