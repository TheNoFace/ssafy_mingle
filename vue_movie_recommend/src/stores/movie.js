import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const popularityMovieList = ref([])
  const releaseMovieList = ref([])
  const categoryMovieList = ref([])
  const detailMovie = ref(null)
  const MovieReviewList = ref([])
  const categoryList = ref([])
  const recommendCategoryMovieList = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'

  const getMovieList = function (standard) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/${standard}/`,
    })
      .then(response => {
        // console.log(response.data)
        if (standard === 'popularity') {
          popularityMovieList.value = response.data
          // console.log(popularityMovieList.value)
        } else if (standard === 'release_date') {
          releaseMovieList.value = response.data
        } else if (standard === 'category') {
          categoryMovieList.value = response.data
          // console.log(categoryMovieList.value)
        }
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getDetailMovie = function (tmdbId) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/detail/${tmdbId}/`,
    })
      .then(response => {
        // console.log(response.data)
        detailMovie.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getMovieReview = function (tmdbId) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/detail/${tmdbId}/review/`,
    })
      .then(response => {
        // console.log(response.data)
        MovieReviewList.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getCategoryList = function () {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/recommend/category/`,
    })
      .then(response => {
        // console.log(response.data)
        categoryList.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const recommendCategory = function (categoryId) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/recommend/category/${categoryId}/`,
    })
      .then(response => {
        // console.log(response.data)
        recommendCategoryMovieList.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { 
    popularityMovieList,
    releaseMovieList,
    categoryMovieList,
    detailMovie,
    MovieReviewList,
    categoryList,
    recommendCategoryMovieList,
    BASE_URL,
    getMovieList,
    getDetailMovie,
    getMovieReview,
    getCategoryList,
    recommendCategory,
   }
}, { persist: true })
