from pymongo import MongoClient
from mongoengine import connect, Document, StringField, DateTimeField, IntField, ListField, Q
import logging

# Configure logging to display MongoDB-related logs
logging.basicConfig(level=logging.DEBUG)


# Connect to MongoDB using mongoengine
connect(db="VettedDB", host="mongodb://localhost:27017", connect=False)


class product_master(Document):
    dms_Product_id = StringField()
    dms_Product_category = StringField()
    dms_Product_Title = StringField()
    dms_Brand = StringField()
    dms_SKU_ID = StringField()
    dms_Color = StringField()
    dms_Included_Components = StringField()
    dms_MRP = StringField()
    dms_Feature_1 = StringField()
    dms_Feature_2 = StringField()
    dms_Feature_3 = StringField()
    dms_Feature_4 = StringField()
    dms_Feature_5 = StringField()
    dms_Entry_Date = DateTimeField()
    dms_Collection_Name = StringField()
    dms_Capacity_Units = StringField()
    dms_Capacity_Value = StringField()
    dms_Standard_Price = StringField()
    dms_Manufacturer = StringField()
    dms_Product_Length = StringField()
    dms_Product_Breadth = StringField()
    dms_Product_Height = StringField()
    dms_Product_Weight = StringField()
    dms_HSN_Code = StringField()
    dms_GST = StringField()
    dms_Qty = StringField()
    dms_Category = StringField()
    dms_Main_Image_URL = StringField()
    dms_Main_View_Image = StringField()
    dms_Front_View_Image = StringField()
    dms_Side_View_Image = StringField()
    dms_Commercial_View_Image_1 = StringField()
    dms_Explainer_view_image = StringField()
    dms_Commercial_View_Image_2 = StringField()
    dms_GST_applicable = StringField()
    dms_Product_Description = StringField()
    dms_Search_Terms = StringField()
    dms_Search_Terms_Keywords_1 = StringField()
    dms_Search_Terms_Keywords_2 = StringField()
    dms_Search_Terms_Keywords_3 = StringField()
    dms_Search_Terms_Keywords_4 = StringField()
    dms_Search_Terms_Keywords_5 = StringField()
    dms_Package_Length = StringField()
    dms_Package_Breadth = StringField()
    dms_Package_Height = StringField()
    dms_Package_Weight = StringField()
    dms_Big_Carton_Dimension = StringField()
    dms_Big_Carton_Weight = StringField()
    dms_Master_Pack_Details = StringField()
    dms_Barcode_UPC_Model_Number = StringField()
    function_id = StringField()
    label_id = StringField()
    vertical_access = IntField()
    horizontal_access = StringField()
    user_id = StringField()
    company = StringField()
    department_name = StringField()
    branch_name = StringField()
    company_id = StringField()
    department_id = StringField()
    branch_id = StringField()
    tenant_id = StringField()
    super_admin_id = StringField()
    dms_slug_field = StringField()
    dms_Additional_Image_1 = StringField()
    dms_Additional_Image_2 = StringField()
    user_name = StringField()
    status = StringField()
    stage = StringField()
    expiry_date = DateTimeField()
    category_rank = StringField()
    ASIN = StringField()
    ASIN_barcode_path = StringField()
    UPC_barcode_path = StringField()
    dms_thumbnail = StringField()
    dms_franchisee_enable = StringField()
    dms_distributor_enable = StringField()
    dms_tenant_enable = StringField()
    dms_box_pack = StringField()
    dms_MOQ = StringField()
    sell_Amazon = StringField()
    sell_Facebook = StringField()
    sell_Cloudtail = StringField()
    sell_Flipkart = StringField()
    sell_Webstore = StringField()
    seo_title = StringField()
    seo_desc = StringField()
    seo_keywords = ListField(StringField())
    seo_meta = ListField(StringField())
    store_url = StringField()
    Amazon_url = StringField()
    Flipkart_url = StringField()
    Google_url = StringField()
    dms_discount = IntField()
    dms_tax_inclusive = StringField()
    variant_name = StringField()
    variant_type = StringField()
    variant_id = StringField()
    brand_id = StringField()
    session_id = StringField()
    viewflow_id = StringField()
    platform_id = StringField()
    category_id = StringField()
    collection_id = StringField()



def get_product_service_details(request_body):
    if request_body.get('user_id') and request_body.get('type'):
        try:
            product_service_obj = product_master.objects(
                Q(user_id=request_body['user_id']) & Q(dms_Category=request_body['type'])
            )
        except Exception as e:
            print(f"Error querying the database: {e}")
            product_service_obj = None

        res = []
        if product_service_obj:
            for data in product_service_obj:
                result = {
                    'dms_Product_id': data.dms_Product_id,
                    'company_id': data.company_id,
                    'dms_Product_Title': data.dms_Product_Title,
                    'dms_Product_Description': data.dms_Product_Description,
                    'dms_Category': data.dms_Category,
                    'dms_Entry_Date': data.dms_Entry_Date,
                    'dms_Main_Image_URL': data.dms_Main_Image_URL,
                    'store_url': data.store_url,
                }
                res.append(result)

            response = {'result': res, 'status_code': 200}

        else:
            response = {'result': res, 'status_code': 200}

    else:
        response = {'result': "Please provide user_id and type", 'status_code': 400}

    return response

if __name__ == "__main__":

    request_body = {
        'user_id': 123,
        'type': 'Toys'

    }

result = get_product_service_details(request_body)

print(result)