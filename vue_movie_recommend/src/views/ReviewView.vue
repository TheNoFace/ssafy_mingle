<template>
  <div class="text-color hidden-scrollbar">
    <v-infinite-scroll :items="items" :onLoad="load" :margin="200">
      <template v-for="(item, index) in items" :key="item">
        <AllReviewCard :review="item" class="m-3" />
      </template>
    </v-infinite-scroll>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useMovieStore } from "@/stores/movie"
import axios from 'axios'
import AllReviewCard from "@/component/Review/AllReviewCard.vue"

const store = useMovieStore()
const items = ref([])
const page = ref(1)


const getReviewList = function (page) {
  axios({
    method: "get",
    url: `${BASE_URL}/api/v1/movies/recommend/review/`,
    params: {
      'page': page
    }
  })
    .then((response) => {
      console.log(response.data)
      reviewList.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

async function api(page) {
  return new Promise(resolve => {
    resolve(
      axios({
        method: "get",
        url: `${store.BASE_URL}/api/v1/movies/recommend/review/`,
        params: {
          'page': page
        }
      })
        .then((response) => {
          return response.data
        })
        .catch((error) => {
          console.log(error)
        }))
  })
}

async function load({ done }) {
  const response = await api(page.value++)
  items.value = []
  items.value.push(...Object.values(response))
  done('ok')
}
</script>

<style scoped></style>
