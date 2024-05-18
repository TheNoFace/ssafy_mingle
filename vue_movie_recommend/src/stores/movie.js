import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const popularMovieList = ref([])
  const BASE_URL = 'http://127.0.0.1:8000'

  const getMovieList = function (standard) {
    axios({
      method : 'get',
      url : `${BASE_URL}/api/v1/movies/${standard}/`,
    })
      .then(response => {
        if (standard === 'popularity') {
          popularMovieList.value = response.data
        }
      })
      .catch(error => {
        console.log(error)
      })
  }

  return { 
    popularMovieList,
    BASE_URL,
    getMovieList,
   }
}, { persist: true })
