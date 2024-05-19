<template>
    <div>
        <h4 class="m-0 my-3" style="color: white;">카테고리별 추천 영화</h4>
        <div class="my-3" v-for="(movieList, idx) in store.categoryMovieList" :key="idx">
            <h5 class="category-name rounded" style="color: white; margin: 0">{{ movieList[0] }}</h5>
            <div class="scroll-container">
                <MainRecommendCard 
                v-for="movie in movieList[1]"
                :key="movie.title"
                :movie="movie"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
import MainRecommendCard from '@/component/MainRecommendCard.vue'
import { useMovieStore } from '@/stores/movie'
import { ref, onMounted } from 'vue'

const store = useMovieStore()

onMounted(() => {
store.getMovieList('category')
})
</script>

<style scoped>
.scroll-container {
  overflow-x: scroll;
  overflow-y: hidden;
  display: flex;
  flex-wrap: nowrap;
}

.scroll-container::-webkit-scrollbar {
    background-color: #ffffff00;
    height: 5px;
}

.scroll-container::-webkit-scrollbar-thumb {
    background-color: #76ABAE;
    border-radius: 5px;
}

.category-name {
    width: 10%;
    text-align: center;
    border: 2px solid #76ABAE;
}
</style>