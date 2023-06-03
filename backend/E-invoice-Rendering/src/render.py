'''this module contains functions for rendering xml to different formats'''
import xmltodict
import xml.etree.ElementTree as ET
from src.database import add_render_to_bucket, add_render_to_db, get_render_id, api_key_check, access_db, access_dashboards, add_product, get_name
from src.country_codes import country_codes
from src.errors import InputError, AccessError, XMLError

def render_html(xml_file, api_key):
    
    '''Given an XML invoice, renders a human_readable HTML version of it,
    stores it in the database and returns the download URL.

    Arguments:
        xml: xml file
        api_key: str

    Exceptions:
        InputError when any of:
            - Input is empty
            - XML file is malformed

    Return value:
        {
            'url': url link to download HTML invoice,
            'render_id': ID of generated invoice
        }
    '''
    # If xml file is not xml or api key is empty then InputError
    if not xml_file or not api_key:
        raise InputError

    # Get registered name of user (either business or individual) with inputted api key
    name = get_name(api_key)
    file_name = create_html(xml_file, name, api_key)
    render_id = get_render_id()

    # Store invoice, file type and render_id in database and S3 bucket
    add_render_to_bucket(render_id, file_name, "html")
    url = add_render_to_db(render_id, "html", api_key)
    return {
            'url': url,
            'render_id': render_id
        }

def create_html(xml_file, name, api_key):
    """
    Creates a html invoice of the given xml file and places it inside the current working directory.

    Arguments:
        xml_file: xml file to be converted

    Return value:
        file_name: Name of the created html file
    """

    # Reads in XML file
    tree = ET.parse(xml_file)

    # Converts XML file to a str
    xml = ET.tostring(tree.getroot(), encoding='utf8', method='xml')

    # Converts XML str to dict
    data = xmltodict.parse(xml)['ns0:Invoice']

    # Check if XML has neccessary tags and is not malformed
    if (not data.get('ns2:AccountingCustomerParty') or
    not data.get('ns2:AccountingSupplierParty') or
    not data.get('ns2:InvoiceLine') or
    not data.get('ns2:LegalMonetaryTotal') or
    not data.get('ns2:TaxTotal') or
    not data.get('ns2:PaymentTerms')):
        raise XMLError("XML file is malformed.")

    # To-party data
    to_party = data['ns2:AccountingCustomerParty']['ns2:Party']
    to_party_address = to_party['ns2:PostalAddress']

    # From-party data
    from_party = data['ns2:AccountingSupplierParty']['ns2:Party']
    from_party_address = from_party['ns2:PostalAddress']

    # Item data
    items = data['ns2:InvoiceLine']

    # Totals data
    totals = data['ns2:LegalMonetaryTotal']

    # HTML to be written in new file
    head = '''
    <!DOCTYPE html>
    <html>
        <head>
    '''
    styles = '''
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
    '''
    addresses = '''
        </head>
        <body>
            <h1> TO: </h1>
            <p> {to_party} </p>
            <p> {to_street} </p>
            <p> {to_additional_st} </p>
            <p> {to_city} </p>
            <p> {to_post_code} </p>
            <p> {to_country} </p>
            <br>
            <h2> INVOICE </h2>
            <h1> FROM: </h1>
            <p> {from_party} </p>
            <p> {from_street} </p>
            <p> {from_city} </p>
            <p> {from_post_code} </p>
            <p> {from_country} </p>
            <p> Business No. {from_company_id}</p>

            <div class='inv_date_and_number'>
                <h3> Invoice Date </h3>
                <p> {date} </p>
            </div>
            <div class='inv_date_and_number'>
                <h3> Invoice Number </h3>
                <p> {inv_no} </p>
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
    '''.format(
                # To-party variables
                to_party=to_party['ns2:PartyName']['ns1:Name'],
                to_street=to_party_address['ns1:StreetName'],
                to_additional_st=to_party_address['ns1:AdditionalStreetName'],
                to_city=to_party_address['ns1:CityName'],
                to_post_code=to_party_address['ns1:PostalZone'],
                to_country=country_codes[to_party_address['ns2:Country']['ns1:IdentificationCode']['#text']],
                # From-party variables
                from_party=from_party['ns2:PartyName']['ns1:Name'],
                from_street=from_party_address['ns1:StreetName'],
                from_city=from_party_address['ns1:CityName'],
                from_post_code=from_party_address['ns1:PostalZone'],
                from_country=country_codes[from_party_address['ns2:Country']['ns1:IdentificationCode']['#text']],
                from_company_id=from_party['ns2:PartyLegalEntity']['ns1:CompanyID']['#text'],
                # Date variables
                date=data['ns1:IssueDate'],
                inv_no=data['ns1:BuyerReference'])
    table = ''
    # If there are more than 1 invoice items then it is a list
    # which needs to be traversed, else it is a dict and can be accessed immediately
    if isinstance(items, list):
        for item in items:
            table += '''
                    <tr>
                        <td> {quantity} </td>
                        <td> {unit_code} </td>
                        <td> {item_name} </td>
                        <td> {single} {single_currency} </td>
                        <td> {amount} {amount_currency} </td>
                        <td> {tax_percent} </td>
                        <td> {item_total} {amount_currency} </td>
                    </tr>
        '''.format(# Items and quantity variables
                    quantity=item['ns1:InvoicedQuantity']['#text'],
                    unit_code=item['ns1:InvoicedQuantity']['@unitCode'],
                    item_name=item['ns2:Item']['ns1:Name'],
                    single=item['ns2:Price']['ns1:PriceAmount']['#text'],
                    single_currency=item['ns2:Price']['ns1:PriceAmount']['@currencyID'],
                    amount=item['ns1:LineExtensionAmount']['#text'],
                    amount_currency=item['ns1:LineExtensionAmount']['@currencyID'],
                    tax_percent=item['ns2:Item']['ns2:ClassifiedTaxCategory']['ns1:Percent'],
                    item_total=round(float(item['ns1:LineExtensionAmount']['#text'])*((float(item['ns2:Item']['ns2:ClassifiedTaxCategory']['ns1:Percent'])/100)+1),2))

            # Required product details to be extracted and stored in database
            item_name = item['ns2:Item']['ns1:Name']
            quantity = item['ns1:InvoicedQuantity']['#text']
            amount = item['ns1:LineExtensionAmount']['#text']

            # Extract from invoice: Name of party sending the invoice
            sender = from_party['ns2:PartyName']['ns1:Name']

            # If the sender is the user, then product type for current invoice be 'earnings'
            if name == sender:
                product_type = 'earnings'
            else:
                product_type = 'expenses'

            # Add each product to user's dashboard database in MongoDB
            add_product(api_key, product_type, item_name, quantity, amount)
            
    else:
        table = '''
                    <tr>
                        <td> {quantity} </td>
                        <td> {unit_code} </td>
                        <td> {item_name} </td>
                        <td> {single} {single_currency} </td>
                        <td> {amount} {amount_currency} </td>
                        <td> {tax_percent} </td>
                        <td> {item_total} {amount_currency} </td>
                    </tr>
        '''.format(# Items and quantity variables
                    quantity=items['ns1:InvoicedQuantity']['#text'],
                    unit_code=items['ns1:InvoicedQuantity']['@unitCode'],
                    item_name=items['ns2:Item']['ns1:Name'],
                    single=items['ns2:Price']['ns1:PriceAmount']['#text'],
                    single_currency=items['ns2:Price']['ns1:PriceAmount']['@currencyID'],
                    amount=items['ns1:LineExtensionAmount']['#text'],
                    amount_currency=items['ns1:LineExtensionAmount']['@currencyID'],
                    tax_percent=items['ns2:Item']['ns2:ClassifiedTaxCategory']['ns1:Percent'],
                    item_total=round(float(items['ns1:LineExtensionAmount']['#text'])*((float(items['ns2:Item']['ns2:ClassifiedTaxCategory']['ns1:Percent'])/100)+1),2))
        
        # Required product details to be extracted and stored in database
        item_name = items['ns2:Item']['ns1:Name']
        quantity=items['ns1:InvoicedQuantity']['#text']
        amount = items['ns1:LineExtensionAmount']['#text']

        # Extract from invoice: Name of party sending the invoice
        sender = from_party['ns2:PartyName']['ns1:Name']

        # If the sender is the user, then product type for current invoice be 'earnings'
        if name == sender:
            product_type = 'earnings'
        else:
            product_type = 'expenses'

        # Add each product to user's dashboard database in MongoDB
        add_product(api_key, product_type, item_name, quantity, amount)

    summary = '''
            </table>

            <div class='total-container'>
                <div class='empty'></div>
                <div>
                    <div class='row-container'>
                        <h3> Total: </h3>
                        <h3 class='right-text'> {total} {total_currency} </h3>
                    </div>
                    <div class='row-container'>
                        <h3> Payable amount: </h3>
                        <h3 class='right-text'> {payable} {payable_currency} </h3>
                    </div>
                </div>
            </div>
            <h4> {tax_scheme} Summary </h4>

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
                    <td> {sum_no_tax} {sum_no_tax_currency} </td>
                    <td> {total_tax_percent} </td>
                    <td> {total_tax} {total_tax_currency} </td>
                    <td> {total} {total_currency} </td>
                </tr>
            </table>
        </body>
    </html>
    '''.format(
                # Total amounts variables
                total=totals['ns1:TaxInclusiveAmount']['#text'],
                total_currency=totals['ns1:TaxInclusiveAmount']['@currencyID'],
                payable=totals['ns1:PayableAmount']['#text'],
                payable_currency=totals['ns1:PayableAmount']['@currencyID'],

                # GST Summary variables
                tax_scheme=data['ns2:TaxTotal']['ns2:TaxSubtotal']['ns2:TaxCategory']['ns2:TaxScheme']['ns1:ID']['#text'],
                sum_no_tax=data['ns2:LegalMonetaryTotal']['ns1:TaxExclusiveAmount']['#text'],
                sum_no_tax_currency=data['ns2:LegalMonetaryTotal']['ns1:TaxExclusiveAmount']['@currencyID'],
                total_tax_percent=data['ns2:TaxTotal']['ns2:TaxSubtotal']['ns2:TaxCategory']['ns1:Percent'],
                total_tax=data['ns2:TaxTotal']['ns2:TaxSubtotal']['ns1:TaxAmount']['#text'],
                total_tax_currency=data['ns2:TaxTotal']['ns2:TaxSubtotal']['ns1:TaxAmount']['@currencyID']
                )
    text = head + styles + addresses + table + summary

    # Generate HTML file
    file_name = "invoice_render.html"
    new_file = open(file_name,"w")
    new_file.write(text)
    new_file.close()
    return file_name

def render_view(render_id, api_key):
    """
    Given the ID of a rendered invoice and the user's API key, 
    return and view their rendered invoice file. 
    Arguments:
        render_id - (int)
        api_key - (str)
    Exceptions:
        InputErrors:
            - render_id is invalid
            - api_key is not given
        AccessErrors:
            - api_key does not exist
            - render_id belongs to an invoice the user did not create
    Returns:
        URL of the rendered invoice
    """
    if not api_key:
        raise InputError("API key required")
    if (type(render_id)) == str:
        if not render_id.isdigit():
            raise InputError("Render ID must be an integer")
    else:
        if (type(render_id)) != int:
            raise InputError("Render ID must be an integer")
    if api_key_check(api_key) is False:
        raise AccessError("API key does not exist")

    collection = access_db()
    
    results = collection.find({'render_id': render_id})

    file_url = ''
    for obj in results:
        # Raise AccessError if invoice does not belong to user
        if api_key != obj['api_key']:
            raise AccessError
        file_url = obj['file_url']
    
    return file_url
