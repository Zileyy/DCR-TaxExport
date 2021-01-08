#imports
import csv
import api

#variables
inputFileName = str(input('Enter input file name: '))   #Input for name of the file that you're getting data of
outputFileName = str(input('Enter output file name: ')) #Input for how would you like your new file to be called
requestToApi = 0
rows = []

#functions
#function that converts from YYYY-MM-DD to DD-MM-YY and removes time
def dateConvert(datetime):
    date_temp = datetime
    row[0] = date_temp[0:10]
    date_temp = date_temp[0:10]
    return date_temp[-2]+date_temp[-1]+'-'+date_temp[-5]+date_temp[-4]+'-'+date_temp[0:4]

#function that outputs data to new CSV file
def export(rows):
    with open(str(outputFileName), 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(rows)

#open CSV file and read it
with open(str(inputFileName), 'r') as file:
    reader = csv.reader(file)
    #reading row by row
    for row in reader:
        #filtering rows with status 'expired'
        if str(row[2]) == 'expired':
            row = ''
        #Every row with status 'voted' gets date extracted (dateTtime -> date)
        else: 
            #changing to only date for date of buying
            buy = dateConvert(row[0])
            
            #changing to only date for date of selling
            sell = dateConvert(row[1])

            #declaring other rows in CSV in more readable form

            #DCR
            ticket_price_buy_DCR = round(float(row[5]),2)
            ticket_price_back_DCR = round(float(row[6]),2)
            ticket_profit_DCR = ticket_price_back_DCR-ticket_price_buy_DCR

            #EUR
            ticket_price_buy_EUR = api.getPriceInEur(buy)
            ticket_price_back_EUR = api.getPriceInEur(sell)
            ticket_profit_EUR = round(ticket_price_back_EUR-ticket_price_buy_EUR,2)

            #Pausing process for preventing program passing 100 requests per minute
            requestToApi += 2
            if requestToApi >= 90:
                api.wait()
                requestToApi = 0

            #row_temp is new row made for new CSV
            row_temp = [buy ,sell,str(ticket_price_buy_DCR)+' DCR',str(ticket_price_back_DCR)+' DCR',str(ticket_profit_DCR)+' DCR',str(ticket_profit_EUR)+' EUR']
            export(row_temp)
    
    