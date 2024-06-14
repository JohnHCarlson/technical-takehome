

<template>
    <div>

        <h1>Counter: {{count}}</h1>
        <button @click="increment">Increment</button>
        <button @click="decrement">Decrement</button>
        <button @click="reset">Reset</button>
    </div>
</template>

<!-- Uncomment to use JavaScript instead of TypeScript. -->
<!-- <script> -->
<!-- If you'd like to use the options API, remove the 'setup' keyword. -->
<script setup lang="ts">
/*
    Refer to the following Vue.js documentation to implement the functionality:

    - Refs for reactive variables: https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref
    - Handling Events: https://vuejs.org/guide/essentials/event-handling.html#inline-handlers

    Suggested steps:
    1. Define a reactive variable for the count using ref.
    2. Implement methods to increment, decrement, and reset the count.
    3. Use the @click directive to call these methods when the buttons are clicked.
*/

import {ref} from 'vue'

const count = ref(0)

function increment(){
  count.value++
}

function decrement(){
  count.value--
}

function reset(){
  count.value = 0
}

</script>