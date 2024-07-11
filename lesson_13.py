import csv
import json
import logging




#task_1
with open('random.csv', 'r') as t1, open('random-michaels.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()


with open('output.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)


#task_2

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def validate_json_syntax(json_data):
    try:
        json.loads(json_data)
        return True
    except json.JSONDecodeError as e:
        logging.error(f"JSON Syntaxis error: {e}")
        return False

def validate_json_files(files):
    results = {}
    for f in files:
        try:
            with open(f, 'r', encoding='utf-8') as file:
                json_data = file.read()

            syntax_valid = validate_json_syntax(json_data)

            results[f] = {
                'syntax_valid': syntax_valid
            }
        except Exception as e:
            logging.error(f"Error in the {f}: {e}")
            results[f] = {
                'error': str(e)
            }
    return results


file_paths = ['login.json', 'localizations_en.json', 'localizations_ru.json', 'swagger.json']


validation_results = validate_json_files(file_paths)

