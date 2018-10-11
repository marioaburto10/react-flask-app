// Include the axios package for performing HTTP requests (promise based alternative to request)
import axios from "axios";

// Helper Functions
const helpers = {
	sendTextToWit: (text) => {
		console.log("text in axios: ", {text});
		return axios({
		  method: 'post',
		  url: '/api/text',
		  data: {
		    text
		  }
		})
		  .then(function (response) {
		    console.log(response);
		    return response
		  })
		  .catch(function (error) {
		    console.log(error);
		  });
	}
	// getLongAndLat: (zipCode) => {
	// 	console.log(zipCode);

	// 	// Figure out the geolocation
	//     const queryURL = "https://api.opencagedata.com/geocode/v1/json?query=" + zipCode + "&pretty=1&key=" + geocodeAPI;

	//     return axios.get(queryURL).then((response) => {
	//     	console.log("Axios response" , response.data.results);
	//     	return response.data.results[0].geometry;

	//     });
	// },

	// findVenues: (keyword, lat, lng, radius) => {
	// 	console.log(keyword, lat, lng, radius);
	// 	const searchTerms = {keyword: keyword,lat: lat,lng: lng, radius}

	// 	return axios.post("/api/places", searchTerms)
	//       .then(function(results) {
	//         console.log("axios results in findVenues", results.data.results);
	//         if (!results.data.results[0]) {
	//         	return "Sorry no matches found, please try a different keyword or radius."
	//         } else {
	//         	return results.data.results;
	//         }
	//       });

	// },

	// getVenueHours: (placeReference) => {
	// 	console.log(placeReference);

	// 	// const placeID = place.id;

	// 	return axios.post("/api/placeHourInfo", {placeReference: placeReference})
	//       .then(function(results) {
	//         console.log("axios results in getVenueHous", results.data.result.opening_hours.weekday_text);
	//       	if (!results.data.result.opening_hours.weekday_text[0]) {
	//         	return "Sorry there are no hours listed for this venue"
	//         } else {
	//         	return results.data.result.opening_hours.weekday_text;
	//         }
	//       });

	// },

	// // This will save new venues to the database
	// postSaved: function(name, icon, address, reference) {
	// 	var newVenue = { name: name, icon: icon, address: address, reference: reference };
	// 	return axios.post("/api/saved", newVenue)
	// 	  .then(function(response) {
	// 	    console.log("axios results", response.data._id);
	// 	    return response.data._id;
	// 	  });
	// },

	// // This will return any saved articles from the database
	// getSaved: function() {
	// 	return axios.get("/api/saved")
	// 	  .then(function(results) {
	// 	    console.log("axios results", results);
	// 	    return results;
	// 	  });
	// },

	// // This will remove saved articles from our database
	// deleteSaved: function(reference) {
	// 	return axios.delete("/api/saved", {
	// 	  params: {
	// 	    "reference": reference
	// 	  }
	// 	})
	// 	.then(function(results) {
	// 	  console.log("axios results", results);
	// 	  return results;
	// 	});
	// }
};

// Export the helpers function
export default helpers;