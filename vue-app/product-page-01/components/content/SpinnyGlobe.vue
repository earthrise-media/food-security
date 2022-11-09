<template>
  <section>
    <div ref="root" class="map-root" style="opacity: 0"></div>
  </section>
</template>

<script setup>
import * as mapboxgl from "mapbox-gl";
import {
  polygon,
  rewind,
  feature,
  point,
  featureCollection,
  bbox,
} from "@turf/turf";
// import * as h3Js from "h3-js";
// import { geojson2h3 } from "geojson2h3";
// import * as h3 from "../node_modules/h3-js/dist/browser/h3-js.js";
// import { h3 } from "h3-node";
// import { latLngToCell } from "h3-js";
const props = defineProps({
  data: {
    type: Object,
    default: () => ({}),
  },
  activeAsset: {
    type: Object,
    default: () => ({}),
  },
  secondsPerRevolution: {
    type: Number,
    default: 90,
  },
  maxSpinZoom: {
    type: Number,
    default: 5,
  },
  slowSpinZoom: {
    type: Number,
    default: 3,
  },
});

// top polluting assets URL
// https://earthrise-trace-places.herokuapp.com/assets.json?sql=SELECT%0D%0A+id%2C%0D%0A+asset_identifier%2C%0D%0A+asset_name%2C%0D%0A+sector%2C%0D%0A+iso3_country%2C%0D%0A+location%2C%0D%0A+type%2C%0D%0A+latitude%2C%0D%0A+longitude%2C%0D%0A+year%2C%0D%0A+total_CO2e_20yrGWP%2C%0D%0A+total_CO2e_100yrGWP%2C%0D%0A+total_CO2_emissions%2C%0D%0A+total_CH4_emissions%2C%0D%0A+total_N2O_emissions%0D%0AFROM+asset+a%0D%0AJOIN+rollup+r%0D%0A++ON+a.id+%3D+r.asset_id%0D%0A++WHERE+year+%3D+%3Ayear%0D%0A++AND+longitude+IS+NOT+NULL%0D%0A++AND+latitude+IS+NOT+NULL%0D%0AORDER+BY+total_CO2e_20yrGWP+DESC%0D%0ALIMIT+CASE+WHEN+cast%28%3Alimit+as+numeric%29+%3E+0+THEN+%3Alimit+ELSE+%271000%27+END&limit=250&year=2021&shape=array

const userInteracting = ref(false);
const spinEnabled = ref(true);

const map = ref(null);
const mapLoaded = ref(false);
const root = ref(null); // mapboxGL element

function buildAssetUrl(asset) {
  // URLs look like /USA/SUS00006
  // console.log("Building asset URL for", asset);
  const countryIso3 = asset.iso3_country;
  const assetId = asset.asset_identifier;
  return `/map/${countryIso3}/${assetId}`;
}

function initMap() {
  console.log("🌞 Initializing map");

  map.value = new mapboxgl.Map({
    container: root.value,
    // style: "mapbox://styles/mapbox/streets-v9",
    // style: "mapbox://styles/mapbox/satellite-streets-v11",
    // style: "mapbox://styles/mapbox/satellite-v9",
    style: "mapbox://styles/ejfox/cl7p0rxav000o15p0dnsl8jen",
    accessToken:
      "pk.eyJ1IjoiZWpmb3giLCJhIjoiY2lyZjd0bXltMDA4b2dma3JzNnA0ajh1bSJ9.iCmlE7gmJubz2RtL4RFzIw",
    projection: "globe",
    zoom: 2,
    // antialias: true,
    // preserveDrawingBuffer: true,
  });

  map.value.addControl(new mapboxgl.NavigationControl());

  // map.value.dragPan.disable();

  function spinGlobe() {
    const zoom = map.value.getZoom();
    if (
      spinEnabled.value &&
      !userInteracting.value &&
      zoom < props.maxSpinZoom
    ) {
      let distancePerSecond = 360 / props.secondsPerRevolution;
      if (zoom > props.slowSpinZoom) {
        const zoomDif =
          (props.maxSpinZoom - zoom) / (props.maxSpinZoom - props.slowSpinZoom);
        distancePerSecond *= zoomDif;
      }
      const center = map.value.getCenter();
      center.lng += distancePerSecond;
      map.value.easeTo({
        center,
        duration: 1000,
        easing: (t) => t,
      });
    }
  }

  // Pause spinning on interaction
  map.value.on("mousedown", () => {
    userInteracting.value = true;
  });

  // Restart spinning the globe when interaction is complete
  map.value.on("mouseup", () => {
    userInteracting.value = false;
    spinGlobe();
  });

  // These events account for cases where the mouse has moved
  // off the map, so 'mouseup' will not be fired.
  map.value.on("dragend", () => {
    userInteracting.value = false;
    spinGlobe();
  });
  map.value.on("pitchend", () => {
    userInteracting.value = false;
    spinGlobe();
  });
  map.value.on("rotateend", () => {
    userInteracting.value = false;
    spinGlobe();
  });

  // When animation is complete, start spinning if there is no ongoing interaction
  map.value.on("moveend", () => {
    spinGlobe();
  });

  spinGlobe();
  updateMap();
}
function updateMap() {
  console.log("🌞 Updating map");

  map.value.on("load", () => {
    mapLoaded.value = true;
    console.log("🗺️ map loaded");

    // set opacity of map root element to 1
    root.value.style.opacity = 1;

    // set center to US
    map.value.flyTo({
      center: [-98.5795, 39.8283],
      speed: 0.8,
      easing: (t) => t,
    });

    // add mapboxgl fog
    map.value.setFog({
      range: [-1, 2],
      "horizon-blend": 0.9,
      color: "#FFFFFF",
      "high-color": "#FFFFFF",
      "space-color": "#FFFFFF",
      "star-intensity": 0,
    });
  });

  // console.log("🗺️ world map data:", props.data);

  map.value.on("load", () => {
    const assets = props.data;
    console.log({ assets });

    // add a custom vector tile layer
    // from https://api.dev.climatetrace.org/v0/tiles/assets/{z}/{x}/{y}

    map.value.addSource("assets", {
      type: "vector",
      tiles: ["https://api.dev.climatetrace.org/v0/tiles/assets/{z}/{x}/{y}"],
      minzoom: 0,
      maxzoom: 14,
    });

    // display points as red circles, but filter out any with the sector "road-transportation"
    map.value.addLayer({
      id: "assets",
      type: "circle",
      source: "assets",
      "source-layer": "default",
      paint: {
        // "circle-radius": 1,
        // draw circle radius at 1 at all zoom levels
        "circle-radius": {
          stops: [
            [3, 1.2],
            [20, 12],
          ],
        },
        // "circle-color": "#FF0000",
        "circle-color": [
          "match",
          ["get", "sector"],
          "steel", // yellow
          "#fbb03b",
          "solid-waste-disposal", // dark blue
          "#223b53",
          "cement", // red
          "#e55e5e",
          "domestic-aviaton", // blue
          "#3bb2d0",
          "international-aviation", // green
          "#6baed6",

          /* other */ "#ccc",
        ],
        "circle-opacity": 0.85,
      },
      filter: ["!=", "sector", "road-transportation"],
    });

    map.value.addLayer({
      id: "assets-outer-circle",
      type: "circle",
      source: "assets",
      "source-layer": "default",
      paint: {
        // "circle-radius": 2.5,
        "circle-radius": {
          stops: [
            [2, 2.8],
            [18, 30],
          ],
        },
        // "circle-color": "#FF0000",
        "circle-color": [
          "match",
          ["get", "sector"],
          "steel", // yellow
          "#fbb03b",
          "solid-waste-disposal", // dark blue
          "#223b53",
          "cement", // red
          "#e55e5e",
          "domestic-aviaton", // blue
          "#3bb2d0",
          "international-aviation", // green
          "#6baed6",

          /* other */ "#ccc",
        ],
        "circle-opacity": 0.15,
      },
      filter: ["!=", "sector", "road-transportation"],
    });

    // set modelOrigin to manhattan's lat/lng coordinates
    // const modelOrigin = [-73.9712, 40.7831];
    // const modelAltitude = 0;
    // const modelRotate = [Math.PI / 2, 0, 0];

    // const modelAsMercatorCoordinate = mapboxgl.MercatorCoordinate.fromLngLat(
    //   modelOrigin,
    //   modelAltitude
    // );

    // // transformation parameters to position, rotate and scale the 3D model onto the map
    // const modelTransform = {
    //   translateX: modelAsMercatorCoordinate.x,
    //   translateY: modelAsMercatorCoordinate.y,
    //   translateZ: modelAsMercatorCoordinate.z,
    //   rotateX: modelRotate[0],
    //   rotateY: modelRotate[1],
    //   rotateZ: modelRotate[2],
    //   /* Since the 3D model is in real world meters, a scale transform needs to be
    //    * applied since the CustomLayerInterface expects units in MercatorCoordinates.
    //    */
    //   scale: modelAsMercatorCoordinate.meterInMercatorCoordinateUnits(),
    // };

    // // add a three js scene but with a simple sphere instead of a model
    // const THREE = window.THREE;

    // const customLayer = {
    //   id: "3d-model",
    //   type: "custom",
    //   renderingMode: "3d",
    //   onAdd: function (map, gl) {
    //     this.camera = new THREE.Camera();
    //     this.scene = new THREE.Scene();

    //     // create two three.js lights to illuminate the model
    //     const directionalLight = new THREE.DirectionalLight(0xffffff);
    //     directionalLight.position.set(0, -70, 100).normalize();
    //     this.scene.add(directionalLight);

    //     const directionalLight2 = new THREE.DirectionalLight(0xffffff);
    //     directionalLight2.position.set(0, 70, 100).normalize();
    //     this.scene.add(directionalLight2);

    //     // use the three.js GLTF loader to add the 3D model to the three.js scene
    //     // const loader = new THREE.GLTFLoader();
    //     // loader.load(
    //     //   "https://docs.mapbox.com/mapbox-gl-js/assets/34M_17/34M_17.gltf",
    //     //   (gltf) => {
    //     //     this.scene.add(gltf.scene);
    //     //   }
    //     // );
    //     // add a sphere with transparency and shading
    //     const geometry = new THREE.SphereGeometry(100000, 16, 16);
    //     const material = new THREE.MeshPhongMaterial({
    //       color: 0xffff00,
    //       specular: 0x555555,
    //       shininess: 30,
    //       transparent: true,
    //       opacity: 0.5,
    //     });
    //     const sphere = new THREE.Mesh(geometry, material);
    //     this.scene.add(sphere);

    //     this.map = map;

    //     // use the Mapbox GL JS map canvas for three.js
    //     this.renderer = new THREE.WebGLRenderer({
    //       canvas: map.getCanvas(),
    //       context: gl,
    //       antialias: true,
    //     });

    //     this.renderer.autoClear = false;
    //   },
    //   render: function (gl, matrix) {
    //     const rotationX = new THREE.Matrix4().makeRotationAxis(
    //       new THREE.Vector3(1, 0, 0),
    //       modelTransform.rotateX
    //     );
    //     const rotationY = new THREE.Matrix4().makeRotationAxis(
    //       new THREE.Vector3(0, 1, 0),
    //       modelTransform.rotateY
    //     );
    //     const rotationZ = new THREE.Matrix4().makeRotationAxis(
    //       new THREE.Vector3(0, 0, 1),
    //       modelTransform.rotateZ
    //     );

    //     const m = new THREE.Matrix4().fromArray(matrix);
    //     const l = new THREE.Matrix4()
    //       .makeTranslation(
    //         modelTransform.translateX,
    //         modelTransform.translateY,
    //         modelTransform.translateZ
    //       )
    //       .scale(
    //         new THREE.Vector3(
    //           modelTransform.scale,
    //           -modelTransform.scale,
    //           modelTransform.scale
    //         )
    //       )
    //       .multiply(rotationX)
    //       .multiply(rotationY)
    //       .multiply(rotationZ);

    //     this.camera.projectionMatrix = m.multiply(l);
    //     this.renderer.resetState();
    //     this.renderer.render(this.scene, this.camera);
    //     this.map.triggerRepaint();
    //   },
    // };

    // map.value.addLayer(customLayer);

    // add text labels for all text
    // map.value.addLayer({
    //   id: "assets-labels",
    //   type: "symbol",
    //   source: "assets",
    //   "source-layer": "default",
    //   layout: {
    //     "text-field": ["get", "sector"],
    //     "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
    //     "text-size": 12,
    //   },
    //   // only show when zoomed in

    //   paint: {
    //     // "text-color": "#000",
    //     // use sector for text-color
    //     "text-color": [
    //       "match",
    //       ["get", "sector"],
    //       "steel", // yellow
    //       "#fbb03b",
    //       "solid-waste-disposal", // dark blue
    //       "#223b53",
    //       "cement", // red
    //       "#e55e5e",
    //       "domestic-aviaton", // blue
    //       "#3bb2d0",
    //       "international-aviation", // green
    //       "#6baed6",

    //       /* other */ "#ccc",
    //     ],
    //     "text-halo-color": "#fff",
    //     "text-halo-width": 2,
    //   },
    //   filter: ["!=", "sector", "road-transportation"],
    // });

    // add text labels for all text that show between zooms 8 and 18
    // map.value.addLayer({
    //   id: "assets-labels",
    //   type: "symbol",
    //   source: "assets",
    //   "source-layer": "default",
    //   layout: {
    //     "text-field": ["get", "sector"],
    //     "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
    //     "text-radial-offset": 0.5,
    //     "text-justify": "auto",
    //     "text-variable-anchor": ["top", "bottom", "left", "right"],
    //     // "text-size": 12,
    //     // interpolate text size with zoom
    //     "text-size": [
    //       "interpolate",
    //       ["linear"],
    //       ["zoom"],
    //       0,
    //       0,
    //       //
    //       6,
    //       0,
    //       //
    //       9,
    //       11,
    //     ],
    //   },
    //   // only show when zoomed in
    //   filter: ["all", ["!=", "sector", "road-transportation"]],
    //   paint: {
    //     // "text-color": "#000",
    //     // use sector for text-color
    //     "text-color": [
    //       "match",
    //       ["get", "sector"],
    //       "steel", // yellow
    //       "#fbb03b",
    //       "solid-waste-disposal", // dark blue
    //       "#223b53",
    //       "cement", // red
    //       "#e55e5e",
    //       "domestic-aviaton", // blue
    //       "#3bb2d0",
    //       "international-aviation", // green
    //       "#6baed6",

    //       /* other */ "#ccc",
    //     ],
    //     // "text-halo-color": "#000",
    //     // "text-halo-width": 1,
    //     "text-halo-width": 0,
    //   },
    // });

    // add a layer for the tile source
    // to display features with a red fill
    // map.value.addLayer({
    //   id: "assets-fill",
    //   type: "fill",
    //   source: "assets",
    //   "source-layer": "assets",
    //   paint: {
    //     "fill-color": "#FF0000",
    //     "fill-opacity": 0.5,
    //   },
    // });

    // h3 stuff
    // const h3Scale = 5;

    // generate h3 hexagons from asset data
    // const hexagons = {};
    // assets.forEach((asset) => {
    //   const lat = asset.latitude;
    //   const lng = asset.longitude;
    //   const h3Index = h3.latLngToCell(lat, lng, h3Scale);
    //   if (hexagons[h3Index]) {
    //     hexagons[h3Index].push(asset);
    //   } else {
    //     hexagons[h3Index] = [asset];
    //   }
    // });

    // simplify to a map of hexagon ids and the number of assets in each
    // const hexagonCountMap = {};
    // Object.keys(hexagons).forEach((h3Index) => {
    //   hexagonCountMap[h3Index] = hexagons[h3Index].length;
    // });

    // create geojson style hexagon geometries from h3 hexagons
    // const hexCoords = h3.cellsToMultiPolygon(
    //   Object.keys(hexagonCountMap),
    //   true
    // );

    // create a new featurecollection with the hexCoords, but using turf to add the count to the property of the feature
    // using feature and featureCollection from turf
    // use the index to lookup the correct geometry from hexCoords
    // const hexFeatures = featureCollection(
    //   Object.keys(hexagonCountMap).map((h3Index, index) => {
    //     const count = hexagonCountMap[h3Index];
    //     const hexPolygon = hexCoords[index];
    //     console.log({ hexagonCountMap, hexPolygon, count });
    //     return polygon(polygon, { count });
    //   })
    // );

    // add hexGeoJson to mapbox map
    // map.value.addSource("hexagons", {
    //   type: "geojson",
    //   data: hexFeatures,
    // });

    // // style the hexagons to use count for the fill, from white to red
    // map.value.addLayer({
    //   id: "hexagons",
    //   type: "fill",
    //   source: "hexagons",
    //   paint: {
    //     "fill-color": [
    //       "interpolate",
    //       ["linear"],
    //       ["get", "count"],
    //       0,
    //       "#FFFFFF",
    //       100,
    //       "#FF0000",
    //     ],
    //     "fill-opacity": 0.5,
    //   },
    // });
  });

  // make a marker for every asset in data
  // props.data.forEach((asset) => {
  //   const marker = new mapboxgl.Marker({
  //     color: "red",
  //     draggable: false,
  //   })
  //     // .setLngLat([asset.latitude, asset.longitude])
  //     .setLngLat([asset.longitude, asset.latitude])
  //     .setPopup(
  //       new mapboxgl.Popup().setHTML(
  //         `<a href="${buildAssetUrl(
  //           asset
  //         )}" class="link blue underline f4 lh-title ma0 pa0 outline-0 bn">
  // ${asset.asset_name ? asset.asset_name : asset.asset_identifier}
  //           </a>`
  //       )
  //     )
  //     .addTo(map.value);
  // });
}

function makeFeatureCollectionFromAssets(data) {
  // const fc = {
  //   type: "FeatureCollection",
  //   features: [],
  // };

  // data.forEach((asset) => {
  //   if (!asset) return;
  //   if (!asset.latitude || !asset.longitude) return;
  //   const pt = turf.point([asset.longitude, asset.latitude]);
  //   let radius = 10;
  //   if (asset["total_CO2_emissions"] !== 0)
  //     radius = Math.sqrt(asset["total_CO2_emissions"]) * 0.005;

  //   const circle = turf.circle(pt, radius, { units: "kilometers" });
  //   fc.features.push(circle);
  // });

  // return fc;
  return featureCollection(data);
}

function flyToAsset(asset) {
  console.log("🗺️ flying to asset", asset);
  // map.value.on("moveend", () => {
  //   console.log("fly end");
  // });
  if (map.value === null) {
    console.log("🗺️ map is null");
    return;
  }
  map.value.flyTo({
    // center: [asset.latitude, asset.longitude],
    center: [asset.longitude, asset.latitude],
    // screenSpeed: 1,
    screenSpeed: 0.45,
  });
}

onMounted(() => {
  console.log("🌞 Map mounted");
  initMap();
  map.value.scrollZoom.disable();

  const resizeObserver = new ResizeObserver(() => {
    map.value.resize();
  });
  resizeObserver.observe(root.value);
  onUnmounted(() => {
    resizeObserver.disconnect();
    map.value.remove();
  });
});
</script>
<style scoped>
.map-root {
  background-color: #1a1a1a;
  width: 100%;
  height: 72vh;
  min-height: 320px;
  cursor: default;
  transition: opacity 2.2s cubic-bezier(0.5, 1, 0.89, 1);
}
</style>
