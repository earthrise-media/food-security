var config = {
  style: "mapbox://styles/highestroad/clagdhi60000v14royyoi5w1m",
  accessToken: "pk.eyJ1IjoiaGlnaGVzdHJvYWQiLCJhIjoiY2w4YWRueTN5MDRhZjNvbWhmb2hlNXFsZyJ9.o7eX3yCdCqUt0VZxpofVoQ",
  showMarkers: false,
  markerColor: "#3FB1CE",
  //projection: 'equirectangular',
  //Read more about available projections here
  //https://docs.mapbox.com/mapbox-gl-js/example/projections/
  inset: false,
  theme: "light",
  use3dTerrain: false, //set true for enabling 3D maps.
  auto: false,
  title: "",
  subtitle: "",
  byline: "",
  footer: "<a href='https://theplotline.org/'>The Plotline</a>",
  chapters: [
    {
      id: "ch1",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods4.jpg",
      description:
        "Pakistan is at the center of a global climate crisis. A series of meteorological disasters in 2022 included glacial outbursts in the Upper Indus Basin, urban flooding in Karachi and Hyderabad, torrential rains and runoffs in Balochistan, flash floods in southern Punjab, and unprecedented rains in central Sindh.",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        {layer: "pk-big-label", "opacity": 0 },
        {layer: "indus-label", "opacity": 0 },
        {layer: "balochistan-label", "opacity": 0 },
        {layer: "nhighlands-label", "opacity": 0 },
        {layer: "lahore-label", "opacity": 0 },
        {layer: "karachi-label", "opacity": 0 },
        {layer: "agflood0-grid", "opacity": 0 },
        {layer: "agflood0-grid", "opacity": 0 },
        {layer: "agflood-grid", "opacity": 0 },
        {layer: "agpop-grid", "opacity": 0 },
        {layer: "ag-grid", "opacity": 0 },
        {layer: "3d-pop-purple", "opacity": 0 },
        {layer: "3d-pop", "opacity": 0 },
        {layer: "flood-population", "opacity": 0 },
        {layer: "flood-3d", "opacity": 0 },
    ],
      onChapterExit: [

      ],
    },
    {
      id: "ch2",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods1.jpg",
      description: "The flooding was unprecedented and has had a devastating impact on the people, infrastructure, and agriculture of Pakistan",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [],
      onChapterExit: [],
    },
    {
      id: "ch3",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The Plotline team analyzed data derived from satellite imagery by Vienna University of Technology to explore the extent of this flooding and better understand the potential impact of this unprecedented flooding.",
      location: { center: [70.02729, 30.24777],
        zoom: 4.41,
        pitch: 0.00,
        bearing: 0.00 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "pk-big-label", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch4",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "To put this flooding in context we need to better understand the geography of Pakistan as a country.",
      location: { center: [68.79775, 26.94317],
        zoom: 5.7,
        pitch: 44.50,
        bearing: -19.20 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        { layer: "pk-big-label", "opacity": 1 }, { layer: "3d-pop", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch5",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Pakistan is the world's fifth most populous country with a population of ~243 million people. This map illustrates Pakistan's population by height; the taller the bar, the more people that live in a location.",
      location: { center: [68.345,25.506], zoom: 6.88, pitch: 70, bearing: 15.2},
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "3d-pop", "opacity": 1 }, { layer: "karachi-label", "opacity": 0 } ],
      onChapterExit: [],
    },
    {
      id: "ch6",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Pakistan's most populous cities are, Karachi in the South with a population of  ~15 million...  ",
      location: { center: [67.072,25.52], zoom: 7.3, pitch: 64, bearing: -26.2 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "3d-pop", "opacity": 1 }, { layer: "karachi-label", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch7",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "And Lahore in the North with a population of ~11 million.",
      location: { center: [73.838,31.78], zoom: 7.66, pitch: 70, bearing: -143 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "3d-pop", "opacity": 1 }, { layer: "karachi-label", "opacity": 1 }, { layer: "lahore-label", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch8",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Together these cities account 10% of Pakistan's total population of ~243 million people.",
      location: { center: [71.373,32.281], zoom: 6.11, pitch: 53, bearing: -146.5 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "3d-pop", "opacity": 1 }, { layer: "karachi-label", "opacity": 0 }, { layer: "lahore-label", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch9",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "From a geography perspective, Pakistan is a blend of landscapes. ",
      location: { center: [71.02,31.89], zoom: 4.94, pitch: 12, bearing: -55.3 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "3d-pop", "opacity": 0 },
      {layer: "nhighlands-label", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch10",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "There are the northern highlands of the Himalayas with some of the world's tallest mountains like K2. ",
      location: { center: [76.4035,35.6764], zoom: 10.62, pitch: 79, bearing: -34.8 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      map3d: true,
      callback: "",
      onChapterEnter: [
        {layer: "nhighlands-label", "opacity": 1 },],
      onChapterExit: [{layer: "nhighlands-label", "opacity": 0 }],
    },
    {
      id: "ch11",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "There is the Balochistan region in the southwest",
      location: { center: [64.889,28.621], zoom: 7.57, pitch: 30, bearing: -47.8 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{layer: "nhighlands-label", "opacity": 0 }, {layer: "balochistan-label", "opacity": 1},],
      onChapterExit: [{layer: "balochistan-label", "opacity": 0}],
    },
    {
      id: "ch12",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "And of course, the Indus river basin with a catchment area of almost 1 million square kilometers. This is the location of the ancient Indus Valley Civilization a cradle of ancient humanity that has been populated for more than 5,000 years.",
      location: { center: [69.9858,28.8151], zoom: 8.89, pitch: 75, bearing: 49.5 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{layer: "balochistan-label", "opacity": 0}, {layer: "indus-label", "opacity": 1},],
      onChapterExit: [{layer: "indus-label", "opacity": 0}, { layer: "pk-big-label", "opacity": 0}],
    },
    {
      id: "ch13",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods7.jpg",
      description: "Because of Pakistan's geography it's susceptible to natural disasters exacerbated by climate change; particularly, it's very susceptible to devastating floods. ",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{layer: "indus-label", "opacity": 0}, { layer: "pk-big-label", "opacity": 0 }, { layer: "flood3d", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch15",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods5.jpg",
      description: "This summer, on the heels of an above average rainy spring, there was a deluge lasting almost a month, drenching the southwest in unprecedented rain. ",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        { layer: "flood3d", "opacity": 1 },
      ],
      onChapterExit: [],
    },
    {
      id: "ch16",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Scroll down the page to see an illustration of flooding spread across the region over a four week period. Note, monitoring of flooded areas started after much of the region had already received a large amount of precipitation.",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        { layer: "flood3d", "fill-extrusion-opacity": "1" },
        { layer: "flood3d", "fill-extrusion-height": "flat" }
    ],
      onChapterExit: [],
    },
    { id: "ch17", alignment: "left", hidden: false, title: "August 18", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 1 },], onChapterExit: [] },
    {
      id: "ch18",
      alignment: "left",
      hidden: false,
      title: "August 22",
      image: "",
      date: true,
      description: "",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        { layer: "flood3d", "fill-extrusion-opacity": "1" },
        { layer: "flood3d", "fill-extrusion-height": 2 },
      ],
      onChapterExit: [],
    },
    {
      id: "ch18a",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The height  of the bars represent the extent of flooding in each area",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [
        { layer: "flood3d", "fill-extrusion-opacity": "1" },
        { layer: "flood3d", "fill-extrusion-height": 2 },
      ],
      onChapterExit: [],
    },
    { id: "ch19", alignment: "left", hidden: false, title: "August 27", image: "", date: true, description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 3 },], onChapterExit: [] },
    { id: "ch20", alignment: "left", hidden: false, title: "August 30", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -38 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 4 },], onChapterExit: [] },
    { id: "ch21", alignment: "left", hidden: false, title: "September 3", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -48 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 5 },], onChapterExit: [] },
    { id: "ch22", alignment: "left", hidden: false, title: "September 6", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -58 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 6 },], onChapterExit: [] },
    { id: "ch23", alignment: "left", hidden: false, title: "September 8", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -68 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 7 },], onChapterExit: [] },
    { id: "ch24", alignment: "left", hidden: false, title: "September 10", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -78 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 8},], onChapterExit: [] },
    { id: "ch25", alignment: "left", hidden: false, title: "September 11", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -88 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 9 },], onChapterExit: [] },
    { id: "ch26", alignment: "left", hidden: false, title: "September 15", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -98 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 10 },], onChapterExit: [] },
    { id: "ch27", alignment: "left", hidden: false, title: "September 18", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -108 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 11 },], onChapterExit: [] },
    { id: "ch28", alignment: "left", hidden: false, title: "September 20", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -118 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 12 },], onChapterExit: [] },
    { id: "ch29", alignment: "left", hidden: false, title: "September 22", image: "", date: true,description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -128 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 13 },], onChapterExit: [] },
    { id: "ch30", alignment: "left", hidden: false, title: "September 23", image: "", date: true, description: "", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -138 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 14 },], onChapterExit: [] },
    { id: "ch31", alignment: "left", hidden: false, title: "", image: "", description: "By the end of the flooding, one third of Pakistan's landmass was underwater, 33 million people were impacted, and more than US$30 billion in infrastructure was lost.", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -148 }, mapAnimation: "flyTo", rotateAnimation: true, callback: "", onChapterEnter: [{ layer: "flood3d", "fill-extrusion-opacity": "1" },
    { layer: "flood3d", "fill-extrusion-height": 14 }, { layer: "flood-population", "opacity": 0 }], onChapterExit: [] },
    {
      id: "ch32",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The flooding also coincided with many highly populated areas. The colors of these bars represent the population in flooded areas. The darker red, the more people that live in that location.",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "flood3d", "opacity": 0 }, { layer: "flood-population", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch33",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Of the 33 million people impacted, 7.3 million were displaced, and over 1,500 were confirmed dead. A third of the mortalities were children.",
      location: {center: [69.086, 26.067], zoom: 7, pitch: 55 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "flood-population", "opacity": 1 }],
      onChapterExit: [{ layer: "sat-color", "opacity": 0 }, { layer: "sat-muted", "opacity": 1}],
    },
    {
      id: "ch34",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The true impact of such a disaster is hard to fathom, but let's look at how flooding may have impacted Pakistan's agriculture, to better understand their ongoing risk for food insecurity.",
      location: { center: [68.39, 26.824], zoom: 6.55, pitch: 0, bearing: 0, speed: 2,
        curve: 2},
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "sat-color", "opacity": 1 }, { layer: "sat-muted", "opacity": 0}, { layer: "flood-population", "opacity": 1 }, { layer: "ag-grid", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch35",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "This map shows where farming happens in Pakistan.",
      location: { center: [69.328,26.363], zoom: 7.01, pitch: 57, bearing: 26.9 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "sat-muted", "opacity": 1 }, { layer: "sat-color", "opacity": 0}, { layer: "flood-population", "opacity": 0 }, { layer: "ag-grid", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch35a",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The bigger the circle, the more of that area that is dedicated to cropland. ",
      location: { center: [68.4515,26.7216], zoom: 10.43, pitch: 0, bearing: 0},
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "sat-muted", "opacity": 1 }, { layer: "sat-color", "opacity": 0}, { layer: "flood-population", "opacity": 0 }, { layer: "ag-grid", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch36",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Note the heavy concentration in the Indus River Basin.",
      location: { center: [68.299,27.509], zoom: 7.69, pitch: 53, bearing: 53.4 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "sat-color", "opacity": 0 }, { layer: "sat-muted", "opacity": 1}, { layer: "ag-grid", "opacity": 1 },{ layer: "agflood-grid", "opacity": 0 }, { layer: "agflood0-grid", "opacity": 0 } ],
      onChapterExit: [],
    },
    {
      id: "ch37",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Now compare to where there was major flooding. The deeper red of the circle, the more flooding in that area.",
      location: { center: [68.299,27.509], zoom: 7.69, pitch: 53 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "sat-bw", "opacity": 0 }, { layer: "sat-muted", "opacity": 1 }, { layer: "ag-grid", "opacity": 0 }, { layer: "agflood-grid", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 1 } ],
      onChapterExit: [],
    },
    {
      id: "ch38",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Experts estimate that more than 3.6 million acres of crops were lost and 750,000 livestock killed.",
      location: { center: [68.454,26.576], zoom: 6.5, pitch: 1, bearing: -7.1},
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [{ layer: "sat-bw", "opacity": 1 }, { layer: "sat-muted", "opacity": 0 }, { layer: "agflood-grid", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch39",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "The food price inflation measured in August 2022 was at its highest value since May 1975 and was expected to surge by another 30%. The cost of edible commodities increased by 400-500%.",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "sat-bw", "opacity": 1 }, { layer: "sat-muted", "opacity": 0 }, { layer: "agflood-grid", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch40",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "With Ukrainian grain exports greatly diminished due to the war with Russia, <a href='https://www.ipcinfo.org/ipc-country-analysis/details-map/en/c/1156103/?iso3=PAK'> Pakistan is at risk of significant food insecurity.</a>",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55 },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "sat-bw", "opacity": 1 }, { layer: "sat-muted", "opacity": 0 }, { layer: "agflood-grid", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 1 }, { layer: "flood-3d", "opacity": 0 }],
      onChapterExit: [],
    },
    {
      id: "ch41",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "Reviewing the extent of the flooding",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, },
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "sat-bw", "opacity": 0 }, { layer: "sat-color", "opacity": 1 }, { layer: "agflood-grid", "opacity": 0 }, { layer: "agflood0-grid", "opacity": 0 }, { layer: "flood-3d", "opacity": 1 }, { layer: "flood-population", "opacity": 0 },],
      onChapterExit: [],
    },
    { id: "ch42", alignment: "left", hidden: false, title: "", image: "", description: "The human impact", location: { center: [69.086, 26.067], zoom: 7, pitch: 55 }, mapAnimation: "flyTo", rotateAnimation: true, callback: "", onChapterEnter: [{ layer: "flood-3d", "opacity": 0 }, { layer: "flood-population", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 0 }, { layer: "agflood-grid", "opacity": 0 }], onChapterExit: [] },
    {
      id: "ch43",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      description: "And detrimental impact on Pakistan's agriculture and food security...",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55},
      mapAnimation: "flyTo",
      rotateAnimation: true,
      callback: "",
      onChapterEnter: [{ layer: "flood-population", "opacity": 0 }, { layer: "agflood-grid", "opacity": 1 }, { layer: "agflood0-grid", "opacity": 1 }],
      onChapterExit: [],
    },
    {
      id: "ch44",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods6.jpg",
      description: "A sobering reality is that this type of flooding is going to happen more, and more often, due to climate change.",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [],
      onChapterExit: [],
    },
    {
      id: "ch45",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods8.jpg",
      description: "Scientists determined that rain across Pakistan is  about <a href='https://www.worldweatherattribution.org/wp-content/uploads/Pakistan-floods-scientific-report.pdf'> 75% more intense than it would have been without the currently recorded 1.2C warming.</a>",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [],
      onChapterExit: [],
    },
    { id: "ch46", alignment: "left", hidden: false, title: "", image: "", fullPhoto: "./assets/floods3.jpg", description: "Even as the likelihood of major rains increases, so does the variability in weather cycles. This means that drought cycles will likely increase as <a href='https://www.npr.org/2022/09/19/1123798981/climate-change-likely-helped-cause-deadly-pakistan-floods-scientists-find'>monsoon rainfall becomes less reliable.</a>", location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 }, mapAnimation: "flyTo", rotateAnimation: false, callback: "", onChapterEnter: [], onChapterExit: [] },
    {
      id: "ch47",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods9.jpg",
      description: "As the acute impact of the flooding subsides, food security remains tenuous and agriculture infrastructure is slow to rebound. ",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [],
      onChapterExit: [],
    },
    {
      id: "ch48",
      alignment: "left",
      hidden: false,
      title: "",
      image: "",
      fullPhoto: "./assets/floods2.jpg",
      description: "To contribute to ongoing flood relief efforts in Pakistan visit <a href='https://uhrelief.org/product/pakistan-emergency-flood-food-parcels/'>United Hands Relief and Development</a>",
      location: { center: [69.086, 26.067], zoom: 7, pitch: 55, bearing: -28 },
      mapAnimation: "flyTo",
      rotateAnimation: false,
      callback: "",
      onChapterEnter: [],
      onChapterExit: [],
    },
  ],
};
