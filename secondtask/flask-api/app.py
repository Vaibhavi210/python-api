from flask import Flask,jsonify,request
import backoff
import requests
from backoff import on_exception, expo

on_exception(
     expo, requests.exceptions.RequestException, max_time=30

)

def send_request():
    response = requests.get("http://127.0.0.1:8000/success",allow_redirects=True)
    response.raise_for_status()  # Raise an error for HTTP responses with status codes >= 400
    return response.json()


app=Flask(__name__)

@app.route('/success',methods=['GET'])
def successFromGet():
     try:
          data=send_request()
          message=[{'message':'your request has been sent successfully','data':data}]
          return jsonify(message), 200
     except requests.exceptions.RequestException as e:
          error={'error':'this is your error'}
          return jsonify(str(e),error), 501

@app.route('/forbidden',methods=['GET'])
def forbiddenFromGet():
     message=[{'message':'forbidden'}]
     return jsonify(message), 403

@app.route('/post/success',methods=['POST'])
def successFromPost():
     message=[{'message':'your request has been sent successfully'}]
     return jsonify(message), 200

@app.route('/badrequest',methods=['POST'])
def badrequestFromPost():
    # message=[{'message':'bad request'}]
     return jsonify({'error': 'Bad Request'}), 400

@app.route('/v1/adaccounts/ad_account_id/segments',methods=['POST'])
def scSegments():
     request_data = request.get_json()
     message = {
          "request_status": "success",
          "request_id": "57ae54d800ff0a4a5232b1a7210001737e616473617069736300016275696c642d35396264653638322d312d31312d37000100",
          "segments": [
               {
                    "sub_request_status": "success",
                    "segment": {
                         "updated_at": "2016-08-12T22:59:42.452Z",
                         "created_at": "2016-08-12T22:59:42.405Z",
                         "name": "all the sams in the world",
                         "id": "5677923948298240",
                         "ad_account_id": "8adc3db7-8148-4fbf-999c-8d2266369d74",
                         "description": "all the sams in the world",
                         "status": "PENDING",
                         "source_type": "FIRST_PARTY",
                         "retention_in_days": 180,
                         "approximate_number_users": 0
                    }
               }
          ]
     }

    
     return jsonify(message,request_data), 200


@app.route('/open_api/v1.3/custom_audience/create/',methods=['POST'])
def tiktok():
     request_data = request.get_json()

     requiredParams = [
        'advertiser_id',
        'custom_audience_name',
        'custom_audience_type',
        'is_amount',
        'is_retention',
        'retention_days',
        'description'
    ]
     missingParams=[params for params in requiredParams if params not in request_data]
     if  missingParams:
               error={
                         "code": 40001,
                         "message": "Invalid request parameters",
                         "data": {}
                         }

               return jsonify(error),400
     
     else:   
          message = {
               "code": 0,
               "message": "OK",
               "data": {
               "custom_audience_id": "1234567890123456789",
               "custom_audience_name": "My TikTok Audience"
               }
               }


     
          return jsonify(message,request_data), 200
     

@app.route('/api/v3/ad_accounts/<ad_account_id>/custom_audiences',methods=['POST'])
def reddit(ad_account_id):
     request_data = request.get_json()

     
     message = {
  "data": {
    "name": "My Customer List 1",
    "id": "ca.129482487242828",
    "status": "VALID",
    "ad_account_id": ad_account_id,
    "created_at": "2023-03-27T21:18:39Z",
    "modified_at": "2023-03-27T21:18:39Z",
    "size_range_upper": 160000,
    "size_range_lower": 140000,
    "type": "CUSTOMER_LIST"
  }
}


     
     return jsonify(message,request_data), 200

@app.route('/v2/dp/audiencemetadata/',methods=['POST'])
def amazon():
       
     request_data = request.get_json()

    # Required parameters list
     requiredParams = [
        "name",
        "description",
        "advertiserId",
        "metadata",
       
    ]
    
    
     missingParams = [param for param in requiredParams if param not in request_data]

     if missingParams:
        error = {
            "code": 40001,
            "message": f"Missing required parameters: {', '.join(missingParams)}",
            "data": {}
        }
        return jsonify(error), 400

     message = {
        "requestId": "a1b1234c-d11d-4e5f-82gh-c609c22255bd",
        "audience": {
            "id": 0,
            "name": "string",
            "description": "string",
            "advertiserId": 0,
            "metadata": {
                "type": "DATA_PROVIDER",
                "externalAudienceId": "string",
                "ttl": 34300800,
                "audienceFees": [
                    {
                        "cpmCents": 0,
                        "currency": "USD"
                    }
                ],
                "dataSourceCountry": [
                    "US",
                    "CA"
                ]
            }
        }
    }
    
     return jsonify(message,request_data), 200

@app.route('/traffic/audiences/email_address/',methods=['POST'])
def yahoo():
       
     request_data = request.get_json()
     seedList = request_data.get("seedList", [])
    
    
     if not seedList:
               message = {
          "response": {
               "status": "ACTIVE",
               "id": 54714971,
               "name": "Electronics",
               "accountId": 108784,
               "createdAt": "2024-08-01",
               "retentionDays": 730
          },
          "errors": None,
          "timeStamp": "2024-08-01T12:35:11.325Z"
          }
               return jsonify(message,request_data), 200
     else:
          return jsonify({'error':'seedlist value is not allowed'})

@app.route('/v18.0/<AD_ACCOUNT_ID>/customaudiences',methods=['POST'])
def meta(AD_ACCOUNT_ID):
       
     request_data = request.get_json()
     requiredParams = [
        "name",
        "subtype",
        "description",
        "customer_file_source",
        "data_source",
        "fields" 
       
    ]
    
    
     missingParams = [param for param in requiredParams if param not in request_data]

     if missingParams:
          error = {
               "error": {
                    "message": "(#2654) Not allowed to create Custom Audience",
                    "type": "OAuthException",
                    "code": 2654,
                    "fbtrace_id": "ABC123XYZ"
               }
          }
          
          if (request_data["customer_file_source"] != "USER_PROVIDED_ONLY" or
            not isinstance(request_data["data_source"], dict) or
            ("type" not in request_data["data_source"] or request_data["data_source"]["type"] != "FIRST_PARTY" or
            "sub_type" not in request_data["data_source"] or request_data["data_source"]["sub_type"] != "CUSTOMER_LIST") or
            not isinstance(request_data["fields"], list)):
                    return jsonify(error), 400
    
     message = {
               "id": AD_ACCOUNT_ID,
               "name": "My Custom Audience"
          }
     return jsonify(message,request_data), 200

@app.route('/v2/adAccounts/<adAccountId>/audiences',methods=['POST'])
def linkedin(adAccountId):
     request_data = request.get_json()

     
     message = {
  "id": adAccountId,
  "name": "My Custom Audience",
  "type": "EMAIL",
  "sourceType": "FIRST_PARTY",
  "retentionPeriod": 30,
  "description": "Audience segment for email-based targeting",
  "status": "ACTIVE"
}


     
     return jsonify(message,request_data), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)