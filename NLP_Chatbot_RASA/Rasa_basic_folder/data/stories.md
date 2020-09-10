## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "delhi"}
    - utter_goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"cuisine": "chinese", "location": "varanasi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "varanasi"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "varanasi"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "varanasi"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "mumbai"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - utter_goodbye
    - action_restart


## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "delhikiraksha"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhikiraksha"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "delhikiraksha"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "mumbai"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "patli gali"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "patli gali"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "patli gali"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "mumbai"}
    - utter_goodbye
    - action_restart


## interactive_story_1
* restaurant_search{"cuisine": "chinese", "non_location": "Satara"}
    - slot{"cuisine": "chinese"}
    - slot{"non_location": "Satara"}
    - utter_nonoperational
    - action_restart
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "Pune"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"non_location": "Rishikesh"}
    - slot{"non_location": "Rishikesh"}
    - utter_nonoperational
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "Agra"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "Jamnagar"}
    - slot{"location": "Jamnagar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_price_range
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"location": "Jamnagar"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "Jamnagar"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"non_location": "kabootar"}
    - slot{"non_location": "kabootar"}
    - utter_nonoperational
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart


## interactive_story_3
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "hamariraksha"}
    - slot{"location": "hamariraksha"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "hamariraksha"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "mumbai"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"non_location": "Panwel"}
    - slot{"non_location": "Panwel"}
    - utter_nonoperational
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "chinese", "location": "ahmedabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "ahmedabad"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "ahmedabad"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "ahmedabad"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "south indian", "location": "noida"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "noida"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "noida"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "american", "non_location": "Panvel"}
    - slot{"cuisine": "american"}
    - slot{"non_location": "Panvel"}
    - utter_nonoperational
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "mexican", "non_location": "Jorhat"}
    - slot{"cuisine": "mexican"}
    - slot{"non_location": "Jorhat"}
    - utter_nonoperational
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "Noida"}
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "rome"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_send_mail
* affirm
    - utter_ask_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "pune"}
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"non_location": "Auckland"}
    - slot{"non_location": "Auckland"}
    - utter_nonoperational
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "japan"}
    - slot{"location": "japan"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "japan"}
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"non_location": "Auckland"}
    - slot{"non_location": "Auckland"}
    - utter_nonoperational
* restaurant_search{"location": "amritsar"}
    - slot{"location": "amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_price_range
* restaurant_search{"price": "2"}
    - slot{"price": "2"}
    - action_search_restaurants
    - slot{"location": "amritsar"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "amritsar"}
    - action_restart

## interactive_story_1
* restaurant_search{"location": "abrakadabra"}
    - slot{"location": "abrakadabra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_price_range
* restaurant_search{"price": "1"}
    - slot{"price": "1"}
    - action_search_restaurants
    - slot{"non_location": "abrakadabra"}
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "delhi"}
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_send_mail
* mail{"email": "harshitmakkar1@gmail.com"}
    - slot{"email": "harshitmakkar1@gmail.com"}
    - action_send_mail
    - slot{"location": "Delhi"}
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "italian", "non_location": "Auckland"}
    - slot{"cuisine": "italian"}
    - slot{"non_location": "Auckland"}
    - utter_nonoperational
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "jahsue"}
    - slot{"cuisine": "american"}
    - slot{"location": "jahsue"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "jahsue"}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_price_range
* restaurant_search{"price": "3"}
    - slot{"price": "3"}
    - action_search_restaurants
    - slot{"non_location": "mubaim"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_send_mail
* decline
    - utter_goodbye
    - action_restart
