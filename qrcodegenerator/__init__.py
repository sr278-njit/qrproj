# Importing library
import qrcode
from file_ops import FileOperations

class UrlQrCodeGenerator(object):
    
    def __init__(self, url):
        self.url = url
    
    def save_qr_code_to_path(self, directory, file):
        qr_code_image = self.get_qr_code()

        # Saving as an image file
        dest = FileOperations.get_calculated_file_path(directory, file)
        print(f"Writing to {dest}")
        qr_code_image.save(dest)        
        
    def get_qr_code(self):    
        # Encoding data using make() function
        return qrcode.make(self.url) 
 