<template>
  <div ref="root" id="root" class="vh-100 w-100"></div>
</template>

<script setup>
import * as mapboxgl from "mapbox-gl";
// import * as d3 from "d3";
// import { centerOfMass } from "@turf/turf";

const map = ref(null);
const mapLoaded = ref(false);

const root = ref(null); // mapboxGL element

function initMap() {
  console.log("🌞 Initializing map");

  map.value = new mapboxgl.Map({
    accessToken:
      "pk.eyJ1IjoibWljY29saXMiLCJhIjoiY2w2ZHlmODQ5MGZtdTNlcHN1eHVyZHo4dyJ9.c7_lC5E1dnQZnsb22QaKnA",
    container: root.value,
    // style: "mapbox://styles/mapbox/streets-v9",
    style: "mapbox://styles/mapbox/satellite-streets-v11",
    projection: "globe",
    zoom: 3.2,
    // center on US
      center: [-95.712891, 37.09024],
  });

  map.value.on('load', () => {
    mapLoaded.value = true;
    console.log("🌞 Map loaded");
    updateMap();
  });

  
}
function updateMap() {
  console.log("🌞 Updating map");

    map.value.addSource("mapbox-dem", {
      type: "raster-dem",
      url: "mapbox://mapbox.mapbox-terrain-dem-v1",
      tileSize: 512,
      maxzoom: 14,
      
    });

    map.value.setTerrain({ source: "mapbox-dem", exaggeration: 2.5 });
    // Dark fog
    map.value.setFog({
      "horizon-blend": 0.2,
      "color": "#d8f2ff",
      "high-color": "#000000",
      "space-color": "#000000",
      "star-intensity": 1,
    });
}

function flyToAsset(asset) {
  console.log("🗺️ flying to asset", asset);
  if (map.value === null) {
    console.log("🗺️ map is null");
    return;
  }
  map.value.flyTo({
    center: [asset.longitude, asset.latitude],
    zoom: 16,
    screenSpeed: 0.45,
  });
}

// watch the activeAsset and fly the map to that asset

onMounted(() => {
  console.log("🌞 Map mounted");
  initMap();

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
<style>
</style>
