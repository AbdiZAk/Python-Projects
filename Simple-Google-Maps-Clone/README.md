 **Summary of Project**
 
 In this project I used Python Folium map and six diffrent APIS to creat a map that shows the user the city they choose.
 The map gets populated with Icons of place types that the user searches for for example Restaurants, museum, Zoo and many more.
 Then the current weather of the city is shown to the user on the top righ corner of the map.
 If the user clicks on one of the places icons it will show more details about it like
 phone, address, rating, hours and more.
 
 **APIS USED**
 
 **GoogleGeoCode API** - With this API I get the lat and lng of a given location which then is used 
  with the GooglePlacesAPi and OpenWeatherMapAPI. 
 
 **GooglePlacesSearch API** - Using googleplace API you can find all perticular placetypes (Gym,Zoo)
  of a given location. Google has a list of all the placetypes accepted in this API call here https://developers.google.com/maps/documentation/places/web-service/supported_types
  
  **GooglePlacesDetails API** - I use googleplacesdetails API to get the details of each placetype found
   I extract the Name, Phone Number, Address, Hours and Website of the place.
  
  **OpenWeather API** - Using openweather API I get the current temperature and the weather Icon of the location that the user chooses.
  
  **Geoapify API** - Using geoapify I get an autocompelete of addresses that match the location the  user starts to type. 
   After the user types in at least four charecters or more the autocomplete suggestions are shown.
  
  **Apitemplete API** - This API lets you create or edit any image to add text to it. I send the current weather icon and the temperature of the location
   to this api. Then it compines it into one img which I can put on the folium map. Folium map in python only alows floating img on the map and not text. 
  
  
