from config import Config
from qrcodegenerator import UrlQrCodeGenerator

def main():
    config = Config()
    qr_code_generator = UrlQrCodeGenerator(config.QR_CODE_DEFAULT_URL)    
    qr_code_generator.save_qr_code_to_path(config.QR_CODE_IMAGE_DIRECTORY, config.QR_CODE_DEFAULT_FILE_NAME)

if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()