<template>
  <!-- <div class="col p-1"> -->
  <div
    class="scroll"
    style="background-color: #ffffff00; color: white; height: 100%"
    id="box"
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

img {
  border-radius: 20px;
}

#box {
  width: 100%;
  height: 100%;
  border-radius: 8px;
  transition: all 0.1s cubic-bezier(0.42, 0, 0.58, 1);
}

#box:hover {
  transform: translateY(-10px);
}

#box .img {
  display: block;
  width: inherit;
  height: inherit;
  padding: 0;
}
</style>
