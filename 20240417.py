from googletrans import Translator
import pyzipper

path = "C:/Users/user/Desktop"

def create_encrypted_zip(file_list, password):
    with pyzipper.AESZipFile(file_list+".zip", 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        zf.write(file_list)


in_file_path = path+"/value/english.txt"
out_file_path = path+"/value/한글번역.txt"

translator = Translator()

with open(in_file_path, "r", encoding="utf-8") as input_file:
    text = input_file.read()
    result = translator.translate(text, dest="ko")

with open(out_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(result.text)
    if __name__ == '__main__':
        create_encrypted_zip(out_file_path,"1234")

