<template>
  <div class="container">
    <div class="search-box">
      <div class="input-group mb-3">
        <label class="input-group-text search-box-input" for="searchBox">
          <i class="fa-solid fa-magnifying-glass" style="color: white"></i>
        </label>
        <input type="text" class="form-control search-box-input" id="searchBox" :value="searchText"
          @input="(event) => (searchText = event.target.value)" v-debounce:500ms="search" autofocus />
      </div>
    </div>

    <div v-if="!searchText">
      <RouterView />
    </div>

    <div v-else>
      <p class="text-color">총 {{ store.searchMovieList.total_results }}개의 검색 결과가 있습니다.</p>
      <SearchMovie :movies="store.searchMovieList.results" />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { useUserStore, useUserTempStore } from "@/stores/user"
import { useMovieStore } from "@/stores/movie"
import SearchMovie from "@/component/Search/SearchMovie.vue"
import vueDebounce from 'vue-debounce'

const vDebounce = vueDebounce({ lock: true })
const userStore = useUserStore()
const userTempStore = useUserTempStore()
const store = useMovieStore()
const searchText = ref(null)
const router = useRouter()

const search = function () {
  store.searchMovie(searchText.value)
}
</script>

<style scoped>
.search-box-input {
  background-color: #ffffff00;
  color: white
}
</style>