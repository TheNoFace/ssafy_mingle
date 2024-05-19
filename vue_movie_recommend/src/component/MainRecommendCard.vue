<template>
    <!-- <div class="col p-1"> -->
        <div class="scroll" style="background-color: #ffffff00; color: white; height: 100%">
            <img :src="imageURL" :alt="movie.title" height="300px" style="margin: 10px;">
        </div>
    <!-- </div> -->
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
    movie : Object
})

const imageURL = ref(
  `https://image.tmdb.org/t/p/original${props.movie.poster_path}`
);
</script>

<style scoped>
.scroll {
  display: inline-block;
}
</style>