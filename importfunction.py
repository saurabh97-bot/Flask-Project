import csv
import io
from pymongo import MongoClient
import uuid

def generate_unique_id(key, collection):
    unique_id = str(uuid.uuid4())
    while dbconnect[collection].find_one({key: unique_id}):
        unique_id = str(uuid.uuid4())
    return unique_id

client = MongoClient("mongodb://localhost:27017")
dbconnect = client.VettedDB

def upload_product_service_from_file():
    mandatory_field_list = [
        "dms_Product_Title",
        "dms_Product_Description",
        "dms_Category",
        "dms_Main_Image_URL",
        "store_url"
    ]

    file_path = "C:/Users/saura/PycharmProjects/VettedBackend/App/products.csv"
    user_id = 123

    try:
        # Open the CSV file using a file object
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_data = file.read()  # Read the CSV content
            csv_io = io.StringIO(csv_data)  # Convert to a file-like object
            reader = csv.reader(csv_io)  # Create a CSV reader

            print("Filename", file_path)
            data_list = []

            # Read the first row to get column names (keys)
            keys = next(reader)

            # Process the rest of the rows
            for row in reader:
                data_dict = {}
                for c, data in enumerate(row):
                    data_dict[keys[c]] = data

                updated_dic = {
                    'company_id': generate_unique_id("company_id", "product_master"),
                    'dms_Product_id': generate_unique_id("dms_product_id", "product_master"),
                    'user_id': user_id
                }
                data_dict.update(updated_dic)

                data_list.append(data_dict)

            print(data_list)

            # Check for mandatory fields (inside the loop to check each row)
            for data_dict in data_list:
                if not all(field in data_dict for field in mandatory_field_list):
                    response = {
                        'result': 'Please check your file before uploading',
                        'status_code': 400
                    }
                    return response

            # Save the data in the database with insert_many query
            collection = dbconnect["product_master"]
            collection.insert_many(data_list)

            response = {
                "result": "Data Uploaded successfully",
                "status_code": 200
            }

            return response

    except Exception as e:
        response = {
            "result": str(e),
            "status_code": 500
        }
        return response

if __name__ == "__main__":
    upload_product_service_from_file()
