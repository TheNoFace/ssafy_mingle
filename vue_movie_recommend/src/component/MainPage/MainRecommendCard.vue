<template>
  <!-- <div class="col p-1"> -->
  <div
    class="scroll"
    style="background-color: #ffffff00; color: white; height: 100%"
  >
    <img
      :src="imageURL"
      :alt="movie.title"
      height="300px"
      style="margin: 10px"
      @click="godetail(movie.tmdb_id)"
    />
  </div>
  <!-- </div> -->
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const props = defineProps({
  movie: Object,
});

const imageURL = ref(
  `https://image.tmdb.org/t/p/original${props.movie.poster_path}`
);

const godetail = function (tmdb_id) {
  router.push({ name: "DetailView", params: { tmdb_id: tmdb_id } });
};
</script>

<style scoped>
.scroll {
  display: inline-block;
}
</style>
