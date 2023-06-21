from pymongo import MongoClient
from urllib.parse import unquote


# dbclient = MongoClient("mongodb://localhost:27017/")
dbclient = MongoClient('mongo', 27017)

resume_db = dbclient['vedantaResume']
resume_coll = resume_db['Resume']
file_coll = resume_db['ResumeFiles']

def insertToMongoDB(payload):
    try:
        inserted_count = resume_coll.insert_one(payload)
    except Exception as e:
        print(' Exception occured while inserting to MongoDb {str(e)}')
def find_inMongoDb(find_text):
    matched_entry = {}
    try:
        matched_entry = resume_coll.find_one({"FileText" : {"$regex": find_text}},{"_id":0})
    except Exception as e:
        print("-- Exception while finding in Mongo DB {str(e)}")
    return matched_entry

def make_FileEntry(file_link,updatedTime):
    file_path = file_name = unique_link = ""    
    try:
        # link = "https://vtelecom319.sharepoint.com/:w:/r/sites/ResumeDb/Shared%20Documents/Resume%20Data/Project_Construction/Alexandra%20Darrow%20Resume.docx?d=w16d8d2db12034ed3a1eb266cfd4f9a34&csf=1&web=1&e=4TjWmp"
        link_str = unquote(file_link)
        link_str = link_str.split("?")[0].split("Shared Documents")[1].split("/")
        file_name = link_str[-1:][0]
        file_path = "/".join([x for x in link_str[:-1] if x])
        if not file_coll.find_one({"FileName": file_name, "FilePath":file_path}):
            file_coll.insert_one({"FileName": file_name, "FilePath":file_path,"updatedTimestamp":updatedTime})
            print(f'-- Entry inserted in file colletion for file {file_name}')
            unique_link = file_link
        else:
            print(f'-- Duplicate skipping entry for file {file_name}')        
    except Exception as e:
        print(f'-- Exception while making entry in mongoDb {str(e)}')
    return unique_link
    
# make_FileEntry("https://vtelecom319.sharepoint.com/:w:/r/sites/ResumeDb/Shared%20Documents/Resume%20Data/Project_Construction/Alexandra%20Darrow%20Resume.docx?d=w16d8d2db12034ed3a1eb266cfd4f9a34&csf=1&web=1&e=4TjWmp","04-24-2023")
# print(find_inMongoDb("Alexandra Darrow"))

