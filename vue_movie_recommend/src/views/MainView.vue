<template>
    <div>
        <Search class="searchBox"/>
        <div class="container">
            <MainPopularity/>
        </div>
    </div>
</template>

<script setup>
import Search from '@/component/Search.vue';
import MainPopularity from '@/component/MainPopularity.vue';
</script>

<style scoped>
.searchBox {
    margin : 50px;
}
</style>