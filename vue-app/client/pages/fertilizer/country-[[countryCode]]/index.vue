<template>
  <section class="pa4 pa5-l sans-serif">
    <NuxtLink class="db pa2 link black" to="/fertilizer/"
      >⬅️ back to all countries</NuxtLink
    >
    <h1 class="mv1 f-headline">{{ activeCountry[0]['Area'] }}</h1>

    <div
      :id="`country-${countryCode}-chart`"
      class="country-chart w-100 mv1 pa0"
    ></div>
  </section>
</template>
<script setup>
import * as Plot from '@observablehq/plot'
import { csvParse, group, autoType, format } from 'd3'

const route = useRoute()
const countryCode = route.params.countryCode

function makeBarChart(data) {
  if (!data || data.length === 0) {
    return
  }

  const width = window.innerWidth
  const height = window.innerHeight

  const chart = Plot.plot({
    marginLeft: 72,
    width,
    height: height * 0.8,
    y: { grid: true },
    x: { nice: true },
    color: {
      type: 'categorical',
      legend: true,
    },
    facet: {
      data,
      x: 'Item',
      y: 'Element',
      marginRight: 100,
    },
    marks: [
      Plot.barY(data, {
        x: 'Year',
        y: 'Value',
        // fill: 'Value',
        // fill: 'Element',
        fill: 'Item',
        title: (d) => d.Year,
      }),
      Plot.ruleY([0]),
    ],
  })
  return chart
}

const { data: fertilizerData } = await useFetch(
  '/Inputs_FertilizersNutrient_E_All_Data_(Normalized).csv'
)

// parse and remove "world" area
const parsedData = csvParse(fertilizerData.value, autoType).filter(
  (item) => item?.Area !== 'World'
)

const dataGroupedByCountry = group(parsedData, (d) => d['Area Code (M49)'])

const activeCountry = computed(() => {
  return dataGroupedByCountry.get(+countryCode)
})

onMounted(() => {
  // instead of creating a new chart for each country, just create a single chart for the country determined by the route param countryCode
  const countryData = dataGroupedByCountry.get(+countryCode)
  const barChart = makeBarChart(countryData)
  nextTick(() => {
    const countryChartEl = document.getElementById(
      `country-${countryCode}-chart`
    )
    countryChartEl.appendChild(barChart)
  })
})
</script>
