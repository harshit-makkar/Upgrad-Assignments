from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import requests

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import mimetypes
from email import encoders
from email.message import Message

list_of_cities = ['ahmedabad','bengaluru','bangalore','bombay','mumbai','chennai','delhi','hyderabad','kolkata','mumbai','pune','agra','ajmer','aligarh','amravati','amritsar','asansol','aurangabad','bareilly','belgaum','bhavnagar','bhiwandi','bhopal','bhubaneswar','bikaner','bilaspur','bokaro steel city','chandigarh','coimbatore','cuttack','dehradun','dhanbad','bhilai','durgapur','dindigul','erode','faridabad','firozabad','ghaziabad','gorakhpur','gulbarga','guntur','gwalior','gurgaon','guwahati','hamirpur','hubli–dharwad','indore','jabalpur','jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kakinada','kannur','kanpur','kochi','kolhapur','kollam','kozhikode','kurnool','ludhiana','lucknow','madurai','malappuram','mathura','mangalore','meerut','moradabad','mysore','nagpur','nanded','nashik','nellore','noida','patna','pondicherry','purulia','prayagraj','raipur','rajkot','rajahmundry','ranchi','rourkela','salem','sangli','shimla','siliguri','solapur','srinagar','surat','thanjavur','thiruvananthapuram','thrissur','tiruchirappalli','tirunelveli','ujjain','bijapur','vadodara','varanasi','vasai-virar city','vijayawada','visakhapatnam','vellore','warangal']

def send_mail_gmail(username,password,toaddrs_list,msg_text,fromaddr=None,subject=None,attachment_path_list=None,html_string=None):
    
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username, password)
    #s.set_debuglevel(1)
    msg = MIMEMultipart()
    sender = fromaddr
    recipients = toaddrs_list
    msg['Subject'] = subject
    if fromaddr is not None:
        msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    if html_string is not None:
        part2 = MIMEText(html_string,'html')
    if attachment_path_list is not None:
        for each_file_path in attachment_path_list:
                   
            file_name=each_file_path.split("/")[-1]
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(each_file_path, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
            msg.attach(part)
    
    msg.attach(MIMEText(msg_text,'plain'))
    if html_string is not None:
        msg.attach(part2)
    s.sendmail(sender, recipients, msg.as_string())


def query_restaurants(latit,longi,cuisine,start_from=1):
	config={ "user_key":"7578b21b2ec10ce2683a63ff359eea62"}
	zomato = zomatopy.initialize_app(config)
	results=zomato.restaurant_search("", latit, longi, cuisine, limit=20, start=start_from,sort='rating',order='desc')
	return(json.loads(results))        

class ActionSearchRestaurants(Action):
    try:
        def name(self):
            return 'action_search_restaurants'
            
        def run(self, dispatcher, tracker, domain):
            config={ "user_key":"XXXXXX0ce2683a63ff359eea62"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            location_detail=zomato.get_location(loc, 1)
            check_location = json.loads(location_detail)
            print(check_location)
            if ((len(check_location['location_suggestions'])==0) or (loc.lower() not in list_of_cities)):
                dispatcher.utter_message("We don't operate in this location! Enter the some other location")
                return [SlotSet('non_location',loc)]
            price_range = tracker.get_slot('price')
            print(price_range)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'american':1,'mexican':73,'chinese':25,'italian':55,'north indian':50,'south indian':85}
            response=""
            rating_dict={}
            if (int(price_range)==1):
                start=1
                while len(rating_dict)<5:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    if 'results_shown' in restaurants:
                        if restaurants['results_shown']==0:
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if int(restaurant['restaurant']['average_cost_for_two'])<300:
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict = "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"
                            if len(rating_dict)<5:
                                rating_dict[response_in_dict] = rating
                    start+=20
            elif (int(price_range)==3):
                start=1
                while len(rating_dict)<5:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    if 'results_shown' in restaurants:
                        if restaurants['results_shown']==0:
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if int(restaurant['restaurant']['average_cost_for_two'])>700:
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict = "Found " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"
                            if len(rating_dict)<5:
                                rating_dict[response_in_dict] = rating
                    start+=20
            elif (int(price_range)==2):
                start=1
                while len(rating_dict)<5:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    if 'results_shown' in restaurants:
                        if restaurants['results_shown']==0:
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            if len(rating_dict)>0:
                                dispatcher.utter_message("Zomato API Limit Exceeded and only the following results could be found - ")
                                break
                            elif len(rating_dict)==0:
                                dispatcher.utter_message("Zomato API Limit Exceeded. Please try again using /restart and put in some new price range or city")
                                break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if ((int(restaurant['restaurant']['average_cost_for_two'])>=300) and (int(restaurant['restaurant']['average_cost_for_two'])<700)):
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict = "Found " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"
                            if len(rating_dict)<5:
                                rating_dict[response_in_dict] = rating
                    start+=20
            if len(rating_dict)>0:
                for sorted_rest in sorted(rating_dict.items(),key=lambda x:x[1],reverse=True):
                    response=response+sorted_rest[0]
                dispatcher.utter_message("-----"+response)
            else:
                response="Unfortunately no restaurant was found in the price range you chose :("
                dispatcher.utter_message("-----"+response)
            return [SlotSet('location',loc)]
    
    except requests.Timeout as err:
        dispatcher.utter_message("Timeout happened. Either the results were taking too long to fetch or the zomato api hits have reached their limits. Please try again by typing - /restart")
        
    
class ActionSendMail(Action):
    try:
        def name(self):
            return 'action_send_mail'

        def run(self, dispatcher, tracker, domain):
            config={"user_key":"XXXXXX683a63ff359eea62"}
            zomato = zomatopy.initialize_app(config)
            loc = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            email = tracker.get_slot('email')
            price_range = tracker.get_slot('price')
            print(price_range)
            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            cuisines_dict={'american':1,'mexican':73,'chinese':25,'italian':55,'north indian':50,'south indian':85}
            response=""
            rating_dict={}
            if (int(price_range)==1):
                start=1
                while len(rating_dict)<10:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    if 'results_shown' in restaurants:
                        if restaurants['results_shown']==0:
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if int(restaurant['restaurant']['average_cost_for_two'])<300:
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict = "Name - "+restaurant['restaurant']['name']+ "\n"+ "Address -"+restaurant['restaurant']['location']['address']+"\n"+"Rating - "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\nAverage Price for Two - "+str(restaurant['restaurant']['average_cost_for_two'])+"\n\n"
                            if len(rating_dict)<10:
                                rating_dict[response_in_dict] = rating
                    start+=20
            elif (int(price_range)==3):
                start=1
                while len(rating_dict)<10:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    if 'results_shown' in restaurants:
                        if restaurants['results_shown']==0:
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if int(restaurant['restaurant']['average_cost_for_two'])>700:
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict="Name - "+restaurant['restaurant']['name']+ "\n"+ "Address -"+restaurant['restaurant']['location']['address']+"\n"+"Rating - "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\nAverage Price for Two - "+str(restaurant['restaurant']['average_cost_for_two'])+"\n\n"
                            if len(rating_dict)<10:
                                rating_dict[response_in_dict] = rating
                    start+=20
            elif (int(price_range)==2):
                start=1
                while len(rating_dict)<10:
                    restaurants = query_restaurants(latit=lat,longi=lon,cuisine = str(cuisines_dict.get(cuisine)),start_from=start)
                    print(restaurants)
                    if 'results_shown' in restaurants:
                        print("\nhere1")
                        if restaurants['results_shown']==0:
                            print("\nhere2")
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    elif 'message' in restaurants:
                        if restaurants['message']=='API limit exceeded':
                            response="*API Limit Exceeded and hence the required number of restaurants would not have been fetched*\n\n"
                            break
                    for restaurant in restaurants['restaurants']:
                        print(restaurant['restaurant']['average_cost_for_two'])
                        if ((int(restaurant['restaurant']['average_cost_for_two'])>=300) and (int(restaurant['restaurant']['average_cost_for_two'])<700)):
                            rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
                            response_in_dict="Name - "+restaurant['restaurant']['name']+ "\n"+ "Address -"+restaurant['restaurant']['location']['address']+"\n"+"Rating - "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\nAverage Price for Two - "+str(restaurant['restaurant']['average_cost_for_two'])+"\n\n"
                            if len(rating_dict)<10:
                                rating_dict[response_in_dict] = rating
                    start+=20       
            if len(rating_dict)>0:
                for sorted_rest in sorted(rating_dict.items(),key=lambda x:x[1],reverse=True):
                    response=response+sorted_rest[0]
                dispatcher.utter_message("Mail Sent!")
            else:
                response="Unfortunately no restaurant was found in the price range you chose :("
                dispatcher.utter_message("-----"+response)
            
            send_mail_gmail(username="youremail@gmail.com",password="upgradbot1!",toaddrs_list=[email],
                    msg_text="Found "+str(len(rating_dict))+" responses - \n\n"+response,fromaddr="youremail@gmail.com",subject=str(loc.title())+" - "+str(cuisine.title())+" Restaurant List")

            return [SlotSet('location',loc)]
    
    except requests.Timeout as err:
        dispatcher.utter_message("Timeout happened. Either the results were taking too long to fetch or the zomato api hits have reached their limits.Mail would have been sent still. Please check your inbox!")
        
