<template>
  <section class="sans-serif pa2 relative">
    <h1>Fertilizer dashboard</h1>
    <!-- <MapboxMap /> -->

    <h2>Select a country</h2>
    <h2>Select your time period</h2>
    <!-- year only to start -->
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

    <section
      id="sort-by-controls"
      class="pa3 sticky bg-white bb bw2 b--light-gray"
    >
      <!-- v-model dropdown to select what metric to sort by -->
      <div class="form-group w-third pa3 v-top dib">
        <label for="sort-by">Fertilizer nutrient</label>
        <select class="form-control" id="sort-by" v-model="sortBy">
          <option value="nitrogen">Nutrient nitrogen N (total)</option>
          <option value="phosphate">Nutrient phosphate P2O5 (total)</option>
          <option value="potash">Nutrient potash K2O (total)</option>
        </select>
      </div>

      <!-- v-model dropdown to select what order to sort by -->
      <div class="form-group w-third pa3 v-top dib">
        <label for="sort-order">Sort order</label>
        <select class="form-control" id="sort-order" v-model="sortOrder">
          <option value="asc">Ascending</option>
          <option value="desc">Descending</option>
        </select>
      </div>

      <!-- v-model dropdown for sortbyelement -->
      <div class="form-group w-third pa3 v-top dib">
        <label for="sort-by-element">Sort by all-time </label>
        <select
          class="form-control"
          id="sort-by-element"
          v-model="sortByElement"
        >
          <option value="production">Production</option>
          <option value="import">Import Quantity</option>
          <option value="export">Export Quantity</option>
          <option value="use">Agricultural Use</option>
        </select>
      </div>

      <!-- make v-model dropdowns for startYear and endYear -->
      <div class="form-group w-third pa3 v-top dn">
        <label for="start-year">Start year</label>
        <select class="form-control" id="start-year" v-model="startYear">
          <option value="2019">2019</option>
          <option value="2018">2018</option>
          <option value="2017">2017</option>
          <option value="2016">2016</option>
          <option value="2015">2015</option>
          <option value="2014">2014</option>
          <option value="2013">2013</option>
          <option value="2012">2012</option>
          <option value="2011">2011</option>
          <option value="2010">2010</option>
          <option value="2009">2009</option>
          <option value="2008">2008</option>
          <option value="2007">2007</option>
          <option value="2006">2006</option>
          <option value="2005">2005</option>
          <option value="2004">2004</option>
          <option value="2003">2003</option>
          <option value="2002">2002</option>
          <option value="2001">2001</option>
          <option value="2000">2000</option>
          <option value="1999">1999</option>
          <option value="1998">1998</option>
          <option value="1997">1997</option>
          <option value="1996">1996</option>
          <option value="1995">1995</option>
          <option value="1994">1994</option>
          <option value="1993">1993</option>
          <option value="1992">1992</option>
          <option value="1991">1991</option>
          <option value="1990">1990</option>
          <option value="1989">1989</option>
          <option value="1988">1988</option>
          <option value="1987">1987</option>
          <option value="1986">1986</option>
          <option value="1985">1985</option>
          <option value="1984">1984</option>
          <option value="1983">1983</option>
          <option value="1982">1982</option>
          <option value="1981">1981</option>
          <option value="1980">1980</option>
          <option value="1979">1979</option>
          <option value="1978">1978</option>
          <option value="1977">1977</option>
          <option value="1976">1976</option>
          <option value="1975">1975</option>
          <option value="1974">1974</option>
          <option value="1973">1973</option>
          <option value="1972">1972</option>
          <option value="1971">1971</option>
          <option value="1970">1970</option>
        </select>
      </div>

      <div class="form-group w-third pa3 v-top dn">
        <label for="end-year">End year</label>
        <select class="form-control" id="end-year" v-model="endYear">
          <option value="2020">2020</option>
          <option value="2019">2019</option>
          <option value="2018">2018</option>
          <option value="2017">2017</option>
          <option value="2016">2016</option>
          <option value="2015">2015</option>
          <option value="2014">2014</option>
          <option value="2013">2013</option>
          <option value="2012">2012</option>
          <option value="2011">2011</option>
          <option value="2010">2010</option>
          <option value="2009">2009</option>
          <option value="2008">2008</option>
          <option value="2007">2007</option>
          <option value="2006">2006</option>
          <option value="2005">2005</option>
          <option value="2004">2004</option>
          <option value="2003">2003</option>
          <option value="2002">2002</option>
          <option value="2001">2001</option>
          <option value="2000">2000</option>
          <option value="1999">1999</option>
          <option value="1998">1998</option>
          <option value="1997">1997</option>
          <option value="1996">1996</option>
          <option value="1995">1995</option>
          <option value="1994">1994</option>
          <option value="1993">1993</option>
          <option value="1992">1992</option>
          <option value="1991">1991</option>
          <option value="1990">1990</option>
          <option value="1989">1989</option>
          <option value="1988">1988</option>
          <option value="1987">1987</option>
          <option value="1986">1986</option>
          <option value="1985">1985</option>
          <option value="1984">1984</option>
          <option value="1983">1983</option>
          <option value="1982">1982</option>
          <option value="1981">1981</option>
          <option value="1980">1980</option>
          <option value="1979">1979</option>
          <option value="1978">1978</option>
          <option value="1977">1977</option>
          <option value="1976">1976</option>
          <option value="1975">1975</option>
          <option value="1974">1974</option>
          <option value="1973">1973</option>
          <option value="1972">1972</option>
          <option value="1971">1971</option>
          <option value="1970">1970</option>
        </select>
      </div>
    </section>

    <section
      v-for="[countryCode, country] in sortedDataGroupedByCountry"
      :key="countryCode"
      class="pv2 ph4 mv0 w-third w-25-l dib"
    >
      <section class="">
        <!-- <h2>{{ getCountryName(countryCode) }}</h2> -->
        <!-- <h3 class="mv1">{{ country[0]?.Area }}</h3> -->
        <h2 class="mv2 f2" v-if="country[0]">
          <NuxtLink
            :to="getCountryLink(country[0])"
            class="link near-black underline"
          >
            <!-- {{ getCountryName(countryCode) }} -->
            {{ country[0]?.Area }}
          </NuxtLink>
        </h2>
        <h4 class="mv1 gray f3">
          {{ sortByToString(sortBy) }}
        </h4>
        <h5 class="mv0 gray f4">
          {{ sortElementToString(sortByElement) }} in 2020:
          <span class="mv1 dib pv1 ph2 bg-light-gray gray br2">
            {{ getLatestValue(country) ? getLatestValue(country) : 'N/A' }}
          </span>
        </h5>

        <div
          :id="`country-${countryCode}-chart`"
          class="country-chart w-100 ba b--light-gray pa0"
        ></div>
        <!-- <section class="cf">
        <div
          v-for="[year, countryYears] in country"
          class="ba b--red w-50 dib v-top"
        >
          <h2>{{ year }}</h2>
          <table v-for="countryYear in countryYears">
            <tr>
              <td>{{ countryYear.Element }}</td>

              <td>{{ countryYear.Value }}</td>

              <td>{{ countryYear.Unit }}</td>
            </tr>
          </table>
        </div>
      </section> -->
      </section>
    </section>
  </section>
</template>
<script setup>
import { csvParse, group, autoType, format } from 'd3'
import * as Plot from '@observablehq/plot'
// import country code json
import countryCodes from '@/assets/country-codes.json'
// "country-code" in countryCodes is equivalent to "Area Code (M49)" in the csv file

const sortOrder = ref('desc')
const sortBy = ref('potash')
const sortByElement = ref('production')

const startYear = ref('1970')
const endYear = ref('2020')

const numberFormat = format('.3s')

function getCountryLink(country) {
  if (!country) return '/'
  const code = country['Area Code (M49)']
  if (!code) return '/'
  return `country-${code.toString()}/`
}

function sortByToString(sortBySlug) {
  //   <option value="nitrogen">Nutrient nitrogen N (total)</option>
  // <option value="phosphate">Nutrient phosphate P2O5 (total)</option>
  // <option value="potash">Nutrient potash K2O (total)</option>
  switch (sortBySlug) {
    case 'nitrogen':
      return 'Nutsrient nitrogen N (total)'
    case 'phosphate':
      return 'Nutrient phosphate P2O5 (total)'
    case 'potash':
      return 'Nutrient potash K2O (total)'
    default:
      return 'Nutrient potash K2O (total)'
  }
}

function sortElementToString(elementString) {
  switch (elementString) {
    case 'production':
      return 'Production'
    case 'import':
      return 'Import Quantity'
    case 'export':
      return 'Export Quantity'
    case 'use':
      return 'Agricultural Use'
    default:
      return 'Production'
  }
}

function getLatestValue(country) {
  const foundCountry = country.filter(
    (item) =>
      item.Year === 2020 &&
      item.Element === sortElementToString(sortByElement.value)
  )[0]
  if (!foundCountry) return
  return `${numberFormat(foundCountry.Value)} ${foundCountry.Unit}`
}

const { data: fertilizerData } = await useFetch(
  '/Inputs_FertilizersNutrient_E_All_Data_(Normalized).csv'
)

// parse and remove "world" area
const parsedData = csvParse(fertilizerData.value, autoType).filter(
  (item) => item?.Area !== 'World'
)

const dataGroupedByCountry = group(parsedData, (d) => d['Area Code (M49)'])

const sortedDataGroupedByCountry = computed(() => {
  let data = dataGroupedByCountry
  // data is a map of country codes whose value is an array of objects
  // each object has a year and a value for the nutrient

  // we want to sort the array of objects by the total value for a nutrient across all years
  const sortedData = new Map(
    [...data]
      .map((country, key) => {
        // console.log({ country, key })
        country[1] = country[1].filter((item) => {
          const entries = item[1]
          return +item.Year >= +startYear.value && +item.Year <= +endYear.value
        })
        return country
      })
      .sort((a, b) => {
        const aEntries = a[1]
        const bEntries = b[1]
        // sum the Value of all entries for a country where Item = sortBy.value
        const aValue = aEntries.reduce((acc, entry) => {
          if (
            entry.Item === sortByToString(sortBy.value) &&
            entry.Element === sortElementToString(sortByElement.value)
          ) {
            return acc + entry.Value
          } else {
            return acc
          }
        }, 0)

        const bValue = bEntries.reduce((acc, entry) => {
          if (
            entry.Item === sortByToString(sortBy.value) &&
            entry.Element === sortElementToString(sortByElement.value)
          ) {
            return acc + entry.Value
          } else {
            return acc
          }
        }, 0)

        // console.log({ a, b }, { aValue, bValue })
        if (sortOrder.value === 'asc') {
          return aValue - bValue
        } else {
          return bValue - aValue
        }

        // return aValue - bValue
      })
  )

  console.log({ sortedData })
  return sortedData
})

const dataGroupedByCountryAndYear = group(
  parsedData,
  (d) => d['Area Code (M49)'],
  (d) => d['Year']
)

const dataGroupedByItemCountryAndYear = group(
  parsedData,
  (d) => d['Item'],
  (d) => d['Area Code (M49)'],
  (d) => d['Year']
)

const potashData = dataGroupedByItemCountryAndYear.get(
  'Nutrient potash K2O (total)'
)

function makeBarChart(data) {
  if (!data || data.length === 0) {
    return
  }
  const chart = Plot.plot({
    marginLeft: 72,
    y: { grid: true },
    x: { nice: true },
    color: {
      type: 'categorical',
      scheme: 'greys',
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
        fill: 'Value',
        title: (d) => d.Year,
      }),
      Plot.ruleY([0]),
    ],
  })
  return chart
}

function makeLineChart(data) {
  if (!data || data.length === 0) {
    return
  }
  // filter data to only sortBy.value
  // const filteredData = data.filter(
  //   (d) => d.Item === sortByToString(sortBy.value)
  // )

  // filter data to only sortByElement
  const filteredData = data
    .filter((d) => d.Element === sortElementToString(sortByElement.value))
    .filter((d) => d.Item === sortByToString(sortBy.value))

  const chart = Plot.plot({
    // y: { grid: true, domain: [0, 10000000] },
    y: { grid: true },
    marginLeft: 72,
    marginRight: 0,
    marginBottom: 18,
    marginTop: 0,
    width: 300,
    height: 200,
    color: {
      type: 'categorical',
      // legend: true,
    },
    marks: [
      Plot.line(filteredData, {
        x: 'Year',
        y: 'Value',
        stroke: 'Item',
      }),
    ],
  })
  return chart
}

function getCountryName(countryCode) {
  const country = countryCodes.find((d) => +d['country-code'] === +countryCode)
  if (!country) return countryCode
  return country.name
}

onMounted(() => {
  console.log({ dataGroupedByCountry })
  console.log('--sorted', sortedDataGroupedByCountry.value)
  sortedDataGroupedByCountry.value.forEach((country, key) => {
    const countryCode = key
    // const countryName = getCountryName(countryCode)
    const countryData = country
    // console.log({ countryCode, countryData })
    const barChart = makeBarChart(countryData)
    const lineChart = makeLineChart(countryData)

    if (!barChart) return
    const countryChartEl = document.getElementById(
      `country-${countryCode}-chart`
    )

    countryChartEl.appendChild(lineChart)
    // countryChartEl.appendChild(barChart)
  })
})
</script>
<style>
.sticky {
  position: sticky;
  top: 0;
  z-index: 1;
}
</style>
