import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const popularityMovieList = ref([])
  const releaseMovieList = ref([])
  const categoryMovieList = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'

  const getMovieList = function (standard) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/${standard}/`,
    })
      .then(response => {
        if (standard === 'popularity') {
          popularityMovieList.value = response.data
          // console.log(popularityMovieList.value)
        } else if (standard === 'release_date') {
          releaseMovieList.value = response.data
        } else if (standard === 'category') {
          categoryMovieList.value = response.data
          // console.log(response.data)
        }
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { 
    popularityMovieList,
    releaseMovieList,
    categoryMovieList,
    BASE_URL,
    getMovieList,
   }
}, { persist: true })
