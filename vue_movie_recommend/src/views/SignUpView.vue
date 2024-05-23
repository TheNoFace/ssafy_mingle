<template>
  <div>
    <h1 style="color: white; text-align: center">회원 가입</h1>
    <div>
      <form ref="signUpForm" @submit.prevent="userSignUp" class="m-auto" style="width: 50%">
        <input class="form-control signup-form-inner my-3" type="text" placeholder="아이디를 입력하세요." name="username"
          required />
        <input class="form-control signup-form-inner my-3" type="text" placeholder="닉네임을 입력하세요." name="nickname"
          required />
        <input class="form-control signup-form-inner my-3" type="password" placeholder="비밀번호를 입력하세요." name="password"
          required />
        <v-card-text v-if="genres.length" class="text-color">
          <h2 class="text-h6 mb-2 text-center">Choose Cagegory</h2>

          <v-responsive class="overflow-y-auto" max-height="280">
            <v-chip-group multiple column v-model="genreSelection" selected-class="text-info">
              <v-chip v-for="genre in genres" :key="genre.tmdb_id" :text="genre.name" :value="genre.tmdb_id"
                @click="getSelection"></v-chip>
            </v-chip-group>
          </v-responsive>
        </v-card-text>
        <!-- </div> -->
        <input class="form-control signup-form-submit" type="submit" value="회원가입" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user"
import { useMovieStore } from "@/stores/movie"
import { ref, onMounted, computed } from "vue"

const userStore = useUserStore()
const store = useMovieStore()
const signUpForm = ref(null)
const genreSelection = ref([])

const userSignUp = function () {
  const payload = new FormData(signUpForm.value)
  payload.append('genres', genreSelection.value)
  userStore.userSignUp(payload)
}

const genres = computed(() => {
  return store.categoryList
})

const getSelection = function () {
  console.log(genreSelection.value)
}

onMounted(() => {
  store.getCategoryList()
})
</script>

<style scoped>
.signup-form-inner {
  background-color: #ffffff00;
  color: white;
}

.signup-form-inner::placeholder {
  color: white;
  /* text-align: center; */
}

.signup-form-submit {
  background-color: #76abae;
  border: 1px #76abae solid;
  color: black;
}

.signup-form-submit:hover {
  background-color: #ffffff00;
  color: white;
}
</style>