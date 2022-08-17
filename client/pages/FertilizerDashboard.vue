<template>
<section>
  <h1>Fertilizer dashboard</h1>
    <!-- <MapboxMap /> -->

  <h2>Select a country</h2>
  <h2>Select your time period</h2> <!-- year only to start -->
  <h2>Select your fertilizer</h2>


  <!-- <h2 class="o-50">Select your time unit</h2> day/month/year -->

  <h3>How much potash was used per time period?</h3>
  <!-- 

      bar chart with use per time period over all available

  -->
  <h3>How much are all countries using in a time period?</h3>

  <h3>Who is exporting potash?</h3>

  <h3>Who is importing potash?</h3>

  <h3>Where goes potash come from and go to? (Flow diagram)</h3>




  
  <section v-for="[countryCode, country] in potashData"
    :key="countryCode"
    class="pa3 mv2 ba">
    <h2>{{ getCountryName(countryCode) }}</h2>
    <section class="cf">
      <!-- <p>{{ country.get('2020') }}</p> -->
      <div v-for="[year, countryYears] in country" class="ba b--red w-50 dib v-top">
        <h2>{{year}}</h2>

      <div :html="makeLineChart(countryYears)"></div>
        
      <table v-for="countryYear in countryYears" >
        <!-- <p>{{ countryYear }}</p> -->
        <tr>

        <td>{{countryYear.Element }}</td>

        <td>{{countryYear.Value }}</td>

        <td>{{countryYear.Unit }}</td>
        
        </tr>
      </table>    
      </div>
      </section>
    </section>

</section>
</template>
<script setup>
import { csvParse, group, autoType } from 'd3'
import * as Plot from "@observablehq/plot";


// import country code json
import countryCodes from '@/assets/country-codes.json'
// "country-code" in countryCodes is equivalent to "Area Code (M49)" in the csv file

const { data: fertilizerData } = await useFetch('Inputs_FertilizersNutrient_E_All_Data_(Normalized).csv')
const parsedData = csvParse(fertilizerData.value, autoType)

const dataGroupedByCountry = group(parsedData, d => d['Area Code (M49)'])

const dataGroupedByCountryAndYear = group(parsedData, d => d['Area Code (M49)'], d => d['Year'])

const dataGroupedByItemCountryAndYear = group(parsedData, d => d['Item'], d => d['Area Code (M49)'], d => d['Year'])

const potashData = dataGroupedByItemCountryAndYear.get('Nutrient potash K2O (total)')

function makeLineChart(data) {
  // return Plot.plot({
  //   marks: [
  //     Plot.line(data, {x: 'Year', y: 'Value'})
  //     ]
  // })
  return `<div class="vh-100 w-100 bg-red white f1">hello world</div>`
}

function getCountryName(countryCode) {
  const country = countryCodes.find(d => +d['country-code'] === +countryCode)
  if(!country) return countryCode
  return country.name
}

onMounted(() => {
  console.log({ potashData })
})


</script>