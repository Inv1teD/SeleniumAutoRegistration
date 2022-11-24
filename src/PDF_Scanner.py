import time

from PIL import Image
from pytesseract import pytesseract
import os


def get_validated_files():
    PATH = str(os.getcwdb())[2:-6] + "\\PDF"
    allowed_Extensions = ['png', 'jpeg', 'jpg']
    print('Directory for PDFs found: ' + PATH + '\n' \
                                                'Found files in PDF directory: ' + ', '.join(os.listdir(PATH)) + "\n" \
            f'Validating files in directory for "{", ".join(allowed_Extensions)}" format')
    file_list = []
    for file in os.listdir(PATH):
        if file[-3:] in allowed_Extensions:
            file_list.append(file)
    print('Validated files: ' + ', '.join(file_list))
    return file_list


def get_text_from_img():
    file_list = get_validated_files()
    name = ''
    surname = ''
    date = ''
    pass_num = ''
    # Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    PATH = str(os.getcwdb())[2:-6] + "\\PDF"
    for file in file_list:
        has_date = False
        has_FullName = False

        # Define path to image
        path_to_image = PATH + "\\" + file
        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = path_to_tesseract

        # Open image with PIL
        img = Image.open(path_to_image)

        # Extract text from image
        if 'Атестат' in file or 'Аттестат' in file:
            img_content = pytesseract.image_to_string(img, lang='ukr').replace("Nod", "№").replace('Хе', '№')
        elif 'Загран' in file:
            img_content = pytesseract.image_to_string(img, lang='ukr+eng').replace("Nod", "№").replace('Хе', '№')
        else:
            img_content = pytesseract.image_to_string(img, lang='ukr+eng').replace("Nod", "№").replace('Хе', '№')

        print(f'Got text from file {file}!')
        with open(f'{PATH}/Results/{file}_text.txt', 'w') as txt_file:
            txt_file.write(img_content)
        with open(f'{PATH}/Results/{file}_text.txt', 'r') as txt_file:
            text = txt_file.read().split('\n')
            if 'здобув повну загальну середню освіту' in ' '.join(text):
                #Means that it is VALID atestat
                # print(set(text))
                pass
            for i in txt_file:
                if i.strip() != '' and len(i.strip().replace(' ', '')) == 44 and not '/' in i:
                    text = i.strip().replace(' ', '').replace('O', '0')
                    year = text[28:-12]
                    month = text[32:-10]
                    day = text[34:-8]
                    pass_num = text[:8]
                    date = f"{day}.{month}.{year}"
                    # print(f'Date: {date}')
                    # print(f'Pass num: {pass_num}')
                if "P<UKR" in i.strip():
                    text = i.strip().replace(' ', '').replace('P<UKR', '').split('<')
                    surname = ''
                    name = ''
                    for counter, block in enumerate(text):
                        if counter == 0:
                            surname = block
                        elif counter == 2:
                            if block[-1] == 'S':
                                name = block[:-1]
                            else:
                                name = block
                        else:
                            pass
                    if name != '' and surname != '':
                        has_FullName = True

                    if not has_FullName:
                        print("[!] Didn't get full name from file! [!]" +
                              f"[!] File: {file} [!]")
    result_dict = {
        'name': name,
        'surname': surname,
        'date_of_birth': date,
        'pass_num': pass_num
    }
    return result_dict

def main():
    info = get_text_from_img()
    print(info)

if __name__ == "__main__":
    main()
