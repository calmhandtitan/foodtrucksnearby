function initialize() {
  var mapOptions = {
  	//center of SF
    center: new google.maps.LatLng(37.78116, -122.409178),
    zoom: 12
  };
  var mapDiv = document.getElementById("map-canvas");
  var map = new google.maps.Map(mapDiv, mapOptions);
  
  var pos = new google.maps.LatLng(37.78116, -122.409178);
  
	var infoWnd = new google.maps.InfoWindow({
    map: map,
    position: pos,
    draggable: true,
    content: '<p style="color:red">Select location</p>'
  });
  var lat = document.getElementById("id_latitude")
  lat.value = pos.lat()
  var lon = document.getElementById("id_longitude")
  lon.value = pos.lng()
      
  google.maps.event.addListener(map, "center_changed", function() {
    var cnt = map.getCenter();
    infoWnd.setPosition(cnt);
    lat = document.getElementById("id_latitude")
    lat.value = cnt.lat()
    lon = document.getElementById("id_longitude")
    lon.value = cnt.lng()
    infoWnd.open(map);
  });
      
//	map.setCenter(pos);

	renderFoodTrucks(map);

}

function renderFoodTrucks(map) {
  var fts = document.getElementsByClassName("ft-info")
  for (var i = 0; i < fts.length; ++i) {
    console.log("renderFoodTrucks")
        var name = fts[i].getAttribute("name")
        var addr = fts[i].getAttribute("address")
        var fooditems = fts[i].getAttribute("fooditems")
        var dist = fts[i].getAttribute("distance")
        var lat = fts[i].getAttribute("lat")
        var lng = fts[i].getAttribute("lng")
        var loc = new google.maps.LatLng(lat,lng);
				
				var contentString = '<div id="content" style="height:100px; width:400px;">' + 
												    '<b>Name:</b> ' + name + '<br>' + 
												    '<b>Distance:</b> ' + dist + ' miles <br>' +
														'<b>Address:</b> ' + addr + '<br>' +
												    '<b>FoodItems Available:</b> ' + fooditems + '<br>' +
												    '</div>';

        var marker = new google.maps.Marker({
          position: loc,
          map: map,
          animation: google.maps.Animation.DROP,
          content: name
        });
				marker['infowindow'] = new google.maps.InfoWindow({
						content: contentString
				});
				google.maps.event.addListener(marker, 'click', function() {
					this['infowindow'].open(map, this);
				});
    }
}
google.maps.event.addDomListener(window, 'load', initialize);
