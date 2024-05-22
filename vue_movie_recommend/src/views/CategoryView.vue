<template>
  <div class="text-color category-list">
    <RouterLink
      class="category-btn rounded m-0 px-3 py-1 m-2"
      v-for="category in store.categoryList"
      @click="store.recommendCategory(category.tmdb_id)"
      :key="category.name"
      :to="{
        name: 'CategoryRecommendMovie',
        params: { category_id: category.tmdb_id },
      }"
    >
      {{ category.name }}
    </RouterLink>
  </div>

  <RouterView />
</template>

<script setup>
import { onMounted } from "vue";
import { RouterLink, RouterView, useRouter } from "vue-router";
import { useMovieStore } from "@/stores/movie";

const store = useMovieStore();
const router = useRouter();

onMounted(() => {
  store.getCategoryList();

  if (store.recommendCategoryMovieList) {
    store.recommendCategoryMovieList = null;
  }

  if (router.currentRoute.value.path.length > 10) {
    store.recommendCategory(router.currentRoute.value.path.substring(10));
  }
});
</script>

<style scoped>
.category-list {
  display: flex;
  flex-wrap: wrap;
}

.category-btn {
  border: 1px solid #76abae;
  text-decoration: none;
  color: white;
}
</style>
