from random import Random
import copy

visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]

mastercardPrefixList = [
        ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    generator = Random()
    generator.seed()  
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result


# #     df_wrong = pd.DataFrame(columns = ["date","error","order_no","attribute"])
def Wrong(x):
    print("executed")
    df_wrong = pd.DataFrame(columns = ["date","orderNo","error"])
    small_array = []
    a = x.copy()
    a = x.copy()
    b = x.copy()
    c = x.copy()
    d = x.copy()
    e = x.copy()
    f = x.copy()
    g = x.copy()
    
    a["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    a["creditCardExpiry"] = "04/22"
    
    b["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    b["creditCardNumber"] = "worngNUM"
    
    c["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    c["cvv"] = c["cvv"]+str("11111")
    
    d["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    d["priceTotalInPence"] =  (d["priceTotalInPence"]/2)-3
      
#       invalid pizza count

    json_ilp = pd.read_json("https://webpagebucket77.s3.eu-west-1.amazonaws.com/restaurants")
    menus = json_ilp["menu"]
    single_menu = menus[random.randint(0,len(menus)-1)]
    item = single_menu[random.randint(0,len(single_menu)-1)]
    orderItems = []

    total = 0 
    menus = json_ilp["menu"]
    single_menu = menus[random.randint(0,len(menus)-1)]
    for i in range(4,random.randint(5,7)):
        item = single_menu[random.randint(0,len(single_menu)-1)]
        orderItems.append((item["name"]))
        total = total + (item["priceInPence"])

    total = total +100

    e["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    e["orderItems"] = orderItems
    e["priceTotalInPence"] = total

#       pizza not defined
    f["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    f["priceTotalInPence"] = 0
    f["orderItems"] = []
    
    
# multiple supliers
    json_ilp = pd.read_json("https://webpagebucket77.s3.eu-west-1.amazonaws.com/restaurants")
    menus = json_ilp["menu"]
    single_menu = menus[random.randint(0,len(menus)-1)]
    item = single_menu[random.randint(0,len(single_menu)-1)]
    orderItems = []

    total = 0 
    menus = json_ilp["menu"]
    for i in range(4,random.randint(5,7)):
        single_menu = menus[random.randint(0,len(menus)-1)]
        item = single_menu[random.randint(0,len(single_menu)-1)]
        orderItems.append((item["name"]))
        total = total + (item["priceInPence"])

    total = total +100

    g["orderNo"] = str(get_random_string(4))+str(random.randint(1001,9999))
    g["orderItems"] = orderItems
    g["priceTotalInPence"] = total

    small_array.append(a)
    small_array.append(b)
    small_array.append(c)
    small_array.append(d)
    small_array.append(e)
    small_array.append(f)
    small_array.append(g)
    
    
#     logging

    df_wrong = pd.DataFrame(columns = ["date","order_no","error"])

    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = a["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidExpiryDate"
    
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = b["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidCardNumber"
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = c["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidCvv"
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = d["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidTotal"
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = e["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidPizzaCount"
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = f["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidPizzaNotDefined"
    df_len = len(df_wrong)
    df_wrong.loc[df_len,"date"] = x["orderDate"]
    df_wrong.loc[df_len,"orderNo"] = g["orderNo"]
    df_wrong.loc[df_len,"error"] = "InvalidPizzaCombinationMultipleSuppliers"
    
    print(df_wrong)
    df_wrong.to_csv("Desktop/CreatedOrders/Invalidorders-"+x["orderDate"]+".csv")
    return small_array


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


import names
import ccard
import pandas as pd
import random
from random_word import RandomWords
import random
import string
import numpy as np
r = RandomWords()
# r.get_random_word()
# names.get_full_name()


def order(paramter,paramtertwo,num):
    y= 0
    order_array = []
    for y in range(num+1):
        randomlist = []
        
        creditcardnumber = ccard.visa()
        if y%2:
            creditcardnumber = ccard.mastercard()

        json_ilp = pd.read_json("https://webpagebucket77.s3.eu-west-1.amazonaws.com/restaurants")
        menus = json_ilp["menu"]
        single_menu = menus[random.randint(0,len(menus)-1)]
        item = single_menu[random.randint(0,len(single_menu)-1)]
        orderItems = []

        total = 0 
        menus = json_ilp["menu"]
        single_menu = menus[random.randint(0,len(menus)-1)]
        for i in range(1,random.randint(1,4)):
            item = single_menu[random.randint(0,len(single_menu)-1)]
            orderItems.append((item["name"]))
            total = total + (item["priceInPence"])

        total = total +100

        x = 0

        orderNo = str(get_random_string(4))+str(random.randint(1001,9999))
        orderDate = paramter
        monthord = paramtertwo 

        customer = names.get_full_name()
        creditcardexpirydateP1 = random.randint(24,30)
        
        part1 = str(random.randint(monthord,12))
        if (len(part1) ==1):
            part1 = "0" + str(part1)

        creditcardexpirydate = str(part1) +"/"+str(creditcardexpirydateP1)
        
        cvv = str(random.randint(101,999))

        import json
        # {"orderNo":"7C57E4E8",
        # "orderDate":"2023-04-01",
        #     "customer":"Herlinda Wynes",
        #         "creditCardNumber":"563792418",
        #             "creditCardExpiry":"01/26",
        #                 "cvv":"683",
        #                     "priceTotalInPence":2400,
        #                         "orderItems":["Super Cheese","All Shrooms"]}


        # a Python object (dict):
        x = {
          "orderNo": orderNo,
          "orderDate": orderDate,
          "customer": customer,
            "creditCardNumber": creditcardnumber,
            "creditCardExpiry" : creditcardexpirydate,
            "cvv" : cvv,
            "priceTotalInPence":total,
            "orderItems": orderItems
        }
        
        if(y >= num): 
            sd = Wrong(x)

            master_two = joinedlist = master + sd
            break
    
        order_array.append(x)
        master.append(x)
        
        # convert into JSON:
    y = json.dumps(master_two)

        # the result is a JSON string:
    return y
        
# Main
month="05"
array_dates = []
master = []

for i in range(27):
    if i+1<=9:
        day =  "0"+str(i+1)
    else:
        day = i +1
        
    date = "2024-"+str(month)+"-"+str(day)
    print(date)
    array_dates.append(date)
    
    numOrders = (random.randint(4,78))
    
    res = (order(date,5,numOrders))
    print(res)
    
    #open text file
    text_file = open("Desktop/CreatedOrders/"+date+".json", "w")
    #write string to file
    text_file.write(str(res))
    #close file
    text_file.close()
    

# sort master file
mst =json.dumps(master)
#open text file
text_file = open("Desktop/CreatedOrdersCreatedOrders/orders.json", "w")
#write string to file
text_file.write(str(mst))
#close file
text_file.close()
    