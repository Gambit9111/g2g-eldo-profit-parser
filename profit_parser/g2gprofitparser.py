def start_parsing(inputfile, outputfile, headers):
    import requests
    from bs4 import BeautifulSoup
    import csv

    with open(outputfile, "w") as write_file:
        csv_writer = csv.writer(write_file, delimiter=' ')

        with open(inputfile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                url = row[0]
                delivered_by_me = int(row[1])

                req = requests.get(url, headers=headers)
                src = req.text
                soup = BeautifulSoup(src, "lxml")
                print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                # TOTAL PAID AMOUNT
                payable_amount = float(soup.find("td", class_="sales-history__table-amount").text.replace("US $", "").replace("\t", "").replace("\n", ""))
                print('\n payable_amount: ', payable_amount, type(payable_amount))
                print('\n')
                #DELIVERY STATUS
                m = soup.find("span", class_="delivery-status__count").text.replace("Delivered", "").replace(",", "").replace("\t", "").replace("\n", "")
                #####
                delivery_status = int(m.split(' / ')[0])
                print('\n delivery_status: ', delivery_status, type(delivery_status))
                print('\n')

                # TOTAL PAID AMOUNT * DELIVERY STATUS
                price_per_unit = payable_amount / delivery_status
                print('\n price_per_unit: ', price_per_unit, type(price_per_unit))
                print('\n')

                # CALCULATED AMOUNT
                calculated_amount = round(price_per_unit * delivered_by_me, 2)
                print('\n delivered_by_me: ', delivered_by_me, type(delivered_by_me))
                print('\n')
                print('\n calculated_amount: ', calculated_amount, type(calculated_amount))
                print('\n')

                purchase_title = soup.find("span", class_="purchase-title").text.replace("\t", "").replace("\n", "").replace("World Of Warcraft", "").replace("(K Gold)", "").replace(" > ", "").replace("World of Warcraft Burning Crusade Classic", "").replace("US", "").replace("(US)", "").replace("[US]", "").replace("-", "").replace("(Gold)", "").replace("()", "").replace("[]", "").replace("                ", "")
                print('\n calculated_amount: ', purchase_title, type(purchase_title))

                print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                line_count += 1

                # turn calculated_amount into string and add dollar sign to it
                calculated_amount = str(calculated_amount) + "$"
                # turn delivered_by_me into string and add k letter to the end of it

                try:
                    csv_writer.writerow([delivered_by_me, calculated_amount, str(row[2]) + "/", purchase_title, url])
                except: 
                    csv_writer.writerow([delivered_by_me, calculated_amount, purchase_title, url])

                #paid_amount = float(soup.find("td", class_="sales-history__table-amount").text.replace("US $", "").replace("\t", "").replace("\n", ""))
                #print('\n paid_amount: ', paid_amount, type(paid_amount))

                #purchase_title = soup.find("span", class_="purchase-title").text.replace("\t", "").replace("\n", "")
                #print('\n', purchase_title, type(purchase_title))
            
                #m = soup.find("span", class_="delivery-status__count").text.replace("Delivered", "").replace(",", "").replace("\t", "").replace("\n", "")
                #####
                #delivered_amount = int(m.split(' / ')[0])
                #
                #print('\ndelivered_amount: ', delivered_amount, type(delivered_amount))

                # Calculations
                #unitprice = round(paid_amount / delivered_amount, 2)
                #print("\nprice/unit: ", unitprice)

                #total_price = round(unitprice * delivered_by_me, 2)
                #print("\ntotal_price: ", total_price)

                #print("\ndelivered_by_me: ", delivered_by_me)

                #line_count += 1




                #if line_count == 0:
                #   print(f'Column names are {", ".join(row)}')
                #  line_count += 1
                #else:
                #   print(f'\t URL : {row[0]} \n AMOUNT : {row[1]}.')
                #  try:
                #     print(f'\t DELIVERED BY ME : {row[2]}.')
                    #except:
                    #   pass
            print(f'Processed {line_count} lines.')









#url = input("Input URL: ")
#delivered_by_me = int(input("\nAmount delivered by me: "))


#headers = {
 #   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  #  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
   # "cookie": "_gcl_au=1.1.549214390.1655910190; noticebar_cookie=1; active_device_token=98cac07f99563b3f271fcb2deb2377b9; _gid=GA1.2.780909001.1656514509; history_offers=%5B%2211963923%22%2C%2211677598%22%2C%2220804142%22%2C%2223952467%22%5D; long_lived_token=d16a0c0caefbc53faff4e21e7efc2401; refresh_token=5319262.e0f819c97158df1d936e6fb696ce357d; _clck=v4ig5r|1|f2z|0; G2GSESID_V4=fhja4chk365s4hoqssdhm072r3; g2g_regional=%7B%22country%22%3A%22LT%22%2C%22currency%22%3A%22USD%22%2C%22language%22%3A%22en%22%7D; _ga_MESX7PR0C0=GS1.1.1657309374.92.1.1657310273.0; _ga=GA1.2.1058493214.1655910190; _clsk=sbm1ou|1657310274625|7|0|j.clarity.ms/collect"
#}

#req = requests.get(url, headers=headers)
#src = req.text
#print(src)

#with open("index.html", "w") as file:
#    file.write(src)

#with open("index.html") as file:
#    src = file.read()


#soup = BeautifulSoup(src, "lxml")
#price = soup.find("td", class_="sales-history__table-service")
#x = price.text.replace("US $", "")
#print(x)

#quantity = soup.find_all(class_="sales-history__table-quantity")
#quantity2 = quantity[1].text
#a = quantity[1].text.replace(",", "")
#print(a)

#paid_amount = float(soup.find("td", class_="sales-history__table-amount").text.replace("US $", "").replace("\t", "").replace("\n", ""))
#print('\n paid_amount: ', paid_amount, type(paid_amount))


#purchase_title = soup.find("span", class_="purchase-title").text.replace("\t", "").replace("\n", "")
#print('\n', purchase_title, type(purchase_title))


#m = soup.find("span", class_="delivery-status__count").text.replace("Delivered", "").replace(",", "").replace("\t", "").replace("\n", "")
#####
#delivered_amount = int(m.split(' / ')[0])
#
#print('\ndelivered_amount: ', delivered_amount, type(delivered_amount))


# Calculations
#unitprice = float(paid_amount / delivered_amount)
#print("\nprice/unit: ", unitprice)

#total_price = round(unitprice * delivered_by_me, 2)
#print("\ntotal_price: ", total_price)