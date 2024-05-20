<template>
    <div class="text-color category-list">
        <RouterLink 
        class="category-btn rounded m-0 px-3 py-1 m-2"
        v-for="category in store.categoryList"
        :key="category.name"
        :category="category"
        :to="{ name : 'CategoryRecommendMovie', params : { category_id : category.tmdb_id} }"
        >{{ category.name }}</RouterLink>
    </div>

    <RouterView/>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

onMounted(() => {
    store.getCategoryList()
})
</script>

<style scoped>
.category-list {
    display: flex;
    flex-wrap: wrap;
}

.category-btn {
    border: 1px solid #76ABAE;
    text-decoration: none;
    color: white
}
</style>
