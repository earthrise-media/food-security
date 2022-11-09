<template>
<div>
      <h1 :class="combinedClass">
      <slot />
    </h1>
</div>
</template>
<script setup>
const props = defineProps({
  class: {
    type: String,
    required: false,
  },
})

const defaultClass = 'intro mv0 f-headline lh-title pa5 vh-80 flex items-center justify-center'

const combinedClass = computed(() => {
  return defaultClass + ' ' + props.class
})
</script>
<style scoped>
p {
  margin: 0 !important;
  padding: 0 !important;
  width: auto;

}
</style>