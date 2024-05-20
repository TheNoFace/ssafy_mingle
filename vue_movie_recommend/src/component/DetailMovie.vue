<template>
    <div class="top-detail col text-color">
        <!-- 이미지 -->
        <div class="col-4 detail-img">
            <img :src="`https://image.tmdb.org/t/p/original${props.movie.poster_path}`" :alt="movie.title" width="100%">
        </div>
        <div class="col-8">
            <!-- 제목, 평점 -->
            <div class="detail-title">
                <h1 style="font-size: 70px;">{{ movie.title }}</h1>
                <h3>
                    <i class="fa-solid fa-star" style="color: yellow;"></i>
                    {{ movie.vote_average }}
                </h3>
            </div>
            <!-- 줄거리 -->
            <div style="padding: 20px;">
                <p>{{ movie.overview }}</p>
            </div>
            <!-- 러닝타임, 국가, 장르 -->
            <div style="padding: 20px;">
                <p>러닝타임 :</p>
                <p>국가 : </p>
                <p class="d-flex">장르 : 
                    <p class="px-2" v-for="genre in movie.genres">{{ genre.name }}</p>
                </p>
            </div>
        </div>  
    </div>
</template>

<script setup>
const props = defineProps({
    movie : Object
})

</script>

<style scoped>
.top-detail {
    display: flex;
}

.detail-img {
    padding: 20px;
}

.detail-title {
    padding: 20px; 
    display: flex;
    justify-content: space-between;
}
</style>