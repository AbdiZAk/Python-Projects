 **Summary of Project**
 
 In this project I used Folium map to creat a map that shows the user the city they choose.
 The map gets populated with Icons of place types that the user searches for for example Restaurants, museum, Zoo and many more.
 Then the current weather of the city is shown to the user on the top righ corner of the map.
 If the user clicks on one of the places icons it will show more details about it like
 phone, address, rating, hours and more.
 
 **APIS USED**
 
 **GoogleGeoCodeAPI** - With this API I get the lat and lng of a given location which then is used 
 with the GooglePlacesAPi and OpenWeatherMapAPI. 
 
 **GooglePlacesSearchAPi** - Using googleplace API you can find all perticular placetypes (Gym,Zoo)
  of a given location. Google has a list of all the placetypes accepted in this API call here https://developers.google.com/maps/documentation/places/web-service/supported_types
  
  **GooglePlacesDetails** - I use googleplacesdetails API to get the details of each placetype found
  I extract the Name, Phone Number, Address, Hours and Website of the place.
  
  
  
