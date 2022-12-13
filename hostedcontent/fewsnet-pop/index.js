mapboxgl.accessToken =
  "pk.eyJ1IjoiaGlnaGVzdHJvYWQiLCJhIjoiY2w4YWRueTN5MDRhZjNvbWhmb2hlNXFsZyJ9.o7eX3yCdCqUt0VZxpofVoQ";
const map = new mapboxgl.Map({
  container: "map", // container ID
  // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
  style: "mapbox://styles/highestroad/clbjz05by000a15posi075rb4", // style URL
  center: [29.553, 9.389], // starting position [lng, lat]
  zoom: 7, // starting zoom
  hash: true,
});

var popStyle = [
  "interpolate",
  ["exponential", 1.99],
  ["zoom"],
  4,
  ["interpolate", ["linear"], ["get", "population"], 1, 0.1, 20000, 1],
  11,
  ["interpolate", ["linear"], ["get", "population"], 1, 12.5, 20000, 125],
];

var standardStyle = [
  "interpolate",
  ["exponential", 1.99],
  ["zoom"],
  4,
  1,
  11,
  125,
];

// map.setFilter('fewsnet', ['==', 'report', reportvar])

map.on("load", () => {
  $('input[type="checkbox"]').change(function () {
    var checkboxName = $(this).attr("name");
    if (this.checked) {
      if (checkboxName == "population Layer") {
        map.setFilter(checkboxName, ["has", "population"]);
        map.setPaintProperty(checkboxName, "circle-radius", popStyle);
        console.log("population-layer");
      }
      if (checkboxName == "satellite-layer") {
        map.setLayoutProperty(checkboxName, "visibility", "visible");
        console.log("satellite-layer");
      }
      // checkbox was checked
      console.log("Checkbox with name '" + checkboxName + "' was checked");
    } else {
      if (checkboxName == "population Layer") {
        map.setFilter(checkboxName, null);
        map.setPaintProperty(checkboxName, "circle-radius", standardStyle);
        console.log("population-layer");
      }
      if (checkboxName == "satellite-layer") {
        map.setLayoutProperty(checkboxName, "visibility", "none");
        console.log("satellite-layer");
      }
      // checkbox was unchecked
      console.log("Checkbox with name '" + checkboxName + "' was unchecked");
    };
  });
  map.on("click", "population Layer", (e) => {
    new mapboxgl.Popup()
      .setLngLat(e.lngLat)
      .setHTML("Population: " + e.features[0].properties.population)
      .addTo(map);
  });

  // Change the cursor to a pointer when
  // the mouse is over the states layer.
  map.on("mouseenter", "population Layer", () => {
    map.getCanvas().style.cursor = "pointer";
  });

  // Change the cursor back to a pointer
  // when it leaves the states layer.
  map.on("mouseleave", "population Layer", () => {
    map.getCanvas().style.cursor = "";
  });
});
