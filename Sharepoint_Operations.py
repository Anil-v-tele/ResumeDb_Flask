import requests

sharepoint_config = {
    "clientId" : "fb516139-b2ef-4735-b205-1686881a8b67",
    "tenantId" : "1b78f26c-9ddc-4301-aebc-41fd55591d80",
    # "resourceId": "0d10361e-ea7e-4176-9487-b4c72a6cc571",
    "secId" : "Qr7Os2VCG+KLnvPD4rtbRkNHG8GCPlJeEpuvxdOXSWk="

}
### ------------------------------------------------
## This function will generate token for Sharepoint
###-------------------------------------------------

def getToken(sharepoint_config):
    access_token = ""
    try:
        auth_url = f'https://login.microsoftonline.com/{sharepoint_config["tenantId"]}/oauth2/v2.0/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': sharepoint_config["clientId"],
            'client_secret': sharepoint_config["secId"],
            'scope': 'https://graph.microsoft.com/.default'
        }
        response = requests.post(auth_url, data=data)
        # access_token = response.json()['access_token']

        # print(f'Access token Received {access_token}')
        if response.status_code in [200, 201] and (not response.json().get('access_token', "")== ""):
            access_token = response.json().get('access_token')
            print(f'--- Access token Received {access_token}')
        else:
            print(f'--- Access token not received failed response code :{response.status_code} text : {response.text}')
    except Exception as e:
        print("Exception while getting the token:", e)
    return access_token

def scan_sharepoint():
    try:
        base_Url = "https://vtelecom319.sharepoint.com/sites/ResumeDb"
        folderURL = "Shared Documents/Resume Data/Project_Construction"

        main_Url = f"{base_Url}/_api/web/GetFolderByServerRelativeUrl(\{folderURL}\')/Files"
        print(url)

        access_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IlRUNUhXRElfd0p4Y0VMRHBnWjY5UmxNTFFPdmhGRDdTal8yUWVOUklkWGsiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8xYjc4ZjI2Yy05ZGRjLTQzMDEtYWViYy00MWZkNTU1OTFkODAvIiwiaWF0IjoxNjg2OTQ4MDAzLCJuYmYiOjE2ODY5NDgwMDMsImV4cCI6MTY4Njk1MTkwMywiYWlvIjoiRTJaZ1lMaVdZNUJoRWMyczVON3k3bXN4VCtJZkFBPT0iLCJhcHBfZGlzcGxheW5hbWUiOiJyZXN1bWVSZWFkIiwiYXBwaWQiOiJjODc5OWMwNS03Mzg5LTRjNGQtOTA3Zi0wNTk0M2NlYmU5NGUiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8xYjc4ZjI2Yy05ZGRjLTQzMDEtYWViYy00MWZkNTU1OTFkODAvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiI2ODI1Zjg2ZS03MzBjLTRkMDctYjRjZS1kNGE5ODA1MGUyNjMiLCJyaCI6IjAuQVM0QWJQSjRHOXlkQVVPdXZFSDlWVmtkZ0FNQUFBQUFBQUFBd0FBQUFBQUFBQUF1QUFBLiIsInN1YiI6IjY4MjVmODZlLTczMGMtNGQwNy1iNGNlLWQ0YTk4MDUwZTI2MyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJOQSIsInRpZCI6IjFiNzhmMjZjLTlkZGMtNDMwMS1hZWJjLTQxZmQ1NTU5MWQ4MCIsInV0aSI6Ik81ZjZ5MkV5TkVLNmpJRjkzN29pQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbIjA5OTdhMWQwLTBkMWQtNGFjYi1iNDA4LWQ1Y2E3MzEyMWU5MCJdLCJ4bXNfdGNkdCI6MTU0NTQ5NzgwMX0.P376gypFhvXrZ6srLaid1C4kkHbGtD36X85hOwL3bd0IFX36PaKbAPjmOaRP3A6wIFPb5edSgZL0eULPSNNdt_MuXv1m66g0a2NVc8JWOpNGg00GQ-ui3RyYhMeWyJWMn4MfMoYH39F8CM7WMplOka1JvFSSwh1YF97vlZAlos9OOwaXFvD0TEDgXg3lQqyGh9LWlKJY4falzCiTwgjqQPcMKd6waIHd8L20utzq4TA3PenKaVUX273ltfOHBEMjwpCjBa1QyZGeVbK_8uzRbqUWxOUmjOzx4s0BbJSV2orTYYwvE4xjjlv5YTOq0cXetVrVChz9pD_89emQJTyptA"
        reqHeader = {
            'Authorization' : "Bearer " + access_token,
            'Accept' : "application/json"
        }
        try:
            response = requests.request("GET", main_Url, headers=reqHeader)
            if response.status_code ==200:
                respObj = response.json()       
                print(f'Response Received')
            else:
                print(f"Response Code {response.status_code} , Response Text : {response.text}")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
def download_Sharepointfile():
    try:
        print(f'y')
    except Exception as e:
        print(e)