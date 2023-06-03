import pytest
import requests
import json
from src import config
from src.database import clear_users, clear_invoices, clear_bucket, access_db

@pytest.fixture
def clear_data():
    clear_users()

@pytest.fixture
def register_one_user():
    clear_users()
    # Register 1 user
    payload = {'name': 'Bob', 'email': 'myemail@gmail.com', 'password': 'password', 'account': 'business'}
    resp = requests.post(config.url+'auth/register', data=payload)
    return json.loads(resp.text)['api_key']

# 403 Error code (AccessError) when api key is invalid
def test_invalid_api_key(clear_data):
    # Send POST request with xml file and invalid api key
    # No users have registered
    headers = {'x-api-key': 'invalid_api_key'}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    resp = requests.post(config.url+'render/html', files=files, headers=headers)

    assert resp.status_code == 403

# 403 Error code (AccessError) when api key is empty str
def test_empty_api_key(clear_data):
    # Send POST request with xml file and EMPTY api key str
    headers = {'x-api-key': ''}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    resp = requests.post(config.url+'render/html', files=files, headers=headers)

    assert resp.status_code == 403

# 276 Error code (XMLError) when XML file is invalid
def test_invalid_xml(register_one_user):
    # Send POST request with INVALID xml file and valid api key
    headers = {'x-api-key': register_one_user}
    files = {'xml_file': open('tests/invalid_sample.xml','rb')}
    resp = requests.post(config.url+'render/html', files=files, headers=headers)

    assert resp.status_code == 276

# Test if return is correct HTML format 
def test_return_info(register_one_user):
    # Send POST request with xml file and api key
    headers = {'x-api-key': register_one_user}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    resp = requests.post(config.url+'render/html', files=files, headers=headers)

    assert resp.status_code == 200
    assert resp.text == '''
    <!DOCTYPE html>
    <html>
        <head>
    
            <style>
                body {
                    margin: 120px;
                    font-family: Helvetica;
                }
                h1 {
                    font-size: 20px;
                }

                h2 {
                    font-size: 35px;
                    font-weight: bold;
                    padding-top: 12px;
                    padding-bottom: 12px;
                }
                p {
                    font-size: 15px;
                    line-height: 1.6px;
                }
                .inv_date_and_number {
                    display: inline-block;
                    padding-right: 135px;
                    padding-top: 30px;
                    padding-bottom: 30px;
                }

                table {
                    border: 1px solid black;
                    border-collapse: collapse;
                    width: 100%;
                }
                tr:nth-child(even) {
                    background-color: #dddddd;
                }

                th {
                    font-weight: bold;
                    text-align: left;
                }

                .total-container {
                    display: flex;
                }

                .empty {
                    flex-grow: 1;
                }

                .row-container {
                    display:flex;
                    flex-grow: 1;
                    margin-right: 5rem;
                }

                .right-text {
                    text-align: end;
                    flex-grow: 1;
                    margin-left: 3rem;
                }

                h4 {
                    font-size: x-large;
                    text-align: center;
                }
            </style>
    
        </head>
        <body>
            <h1> TO: </h1>
            <p> Awolako Enterprises Pty Ltd </p>
            <p> Suite 123 Level 45 </p>
            <p> 999 The Crescent </p>
            <p> Homebush West </p>
            <p> 2140 </p>
            <p> Australia </p>
            <br>
            <h2> INVOICE </h2>
            <h1> FROM: </h1>
            <p> Ebusiness Software Services Pty Ltd </p>
            <p> 100 Business St </p>
            <p> Dulwich Hill </p>
            <p> 2203 </p>
            <p> Australia </p>
            <p> Business No. 80647710156</p>

            <div class='inv_date_and_number'>
                <h3> Invoice Date </h3>
                <p> 2022-02-07 </p>
            </div>
            <div class='inv_date_and_number'>
                <h3> Invoice Number </h3>
                <p> EBWASP1002 </p>
            </div>
    
            <table>
                <tr>
                    <th> Quantity </th>
                    <th> Code </th>
                    <th> Description </th>
                    <th> Price </th>
                    <th> Amount </th>
                    <th> GST% </th>
                    <th> Total </th>
                </tr>
    
                    <tr>
                        <td> 500.0 </td>
                        <td> C62 </td>
                        <td> pencils </td>
                        <td> 0.20 AUD </td>
                        <td> 100.00 AUD </td>
                        <td> 10.0 </td>
                        <td> 110.0 AUD </td>
                    </tr>
        
            </table>

            <div class='total-container'>
                <div class='empty'></div>
                <div>
                    <div class='row-container'>
                        <h3> Total: </h3>
                        <h3 class='right-text'> 110.00 AUD </h3>
                    </div>
                    <div class='row-container'>
                        <h3> Payable amount: </h3>
                        <h3 class='right-text'> 110.00 AUD </h3>
                    </div>
                </div>
            </div>
            <h4> GST Summary </h4>

            <table>
                <tr>
                    <th style="width:38%"> Description </th>
                    <th style="width:20%"> Amount </th>
                    <th style="width:9%"> GST% </th>
                    <th style="width:24.5%"> GST </th>
                    <th> Total </th>
                </tr>
                <tr>
                    <td> Standard Rate </td>
                    <td> 100.00 AUD </td>
                    <td> 10.0 </td>
                    <td> 10.00 AUD </td>
                    <td> 110.00 AUD </td>
                </tr>
            </table>
        </body>
    </html>
    '''