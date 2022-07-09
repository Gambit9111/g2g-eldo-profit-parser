def start_parsing(inputfile, outputfile, headers):
    import requests
    import csv
    with open(outputfile, "w") as write_file:
        csv_writer = csv.writer(write_file, delimiter=' ')
        with open(inputfile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                url = row[0]
                # cut https://www.eldorado.gg/order/ out of the url
                order_id = url[30:]

                url_api = f"https://www.eldorado.gg/api/orders/me/{order_id}"
                # send a a request to the url and get a status 200
                response = requests.get(url_api, headers=headers)
                # save the response json 
                data = response.json()

                price = round((data['totalPrice']['amount']) * 0.91, 2)
                price = str(price) + "$"

                amount = (data['purchaseQuantity'])
                # turn amount into string and add a k letter to the end of it
                # create a list of names and get a random name from it
                server = (data['orderOfferDetails']['tradeEnvironmentProperties'][1]['value'])
                faction = (data['orderOfferDetails']['tradeEnvironmentProperties'][2]['value'])

                try:
                    csv_writer.writerow([amount, price, str(row[1]) + "/", server, faction, url])
                except: 
                    csv_writer.writerow([amount, price, server, faction, url])