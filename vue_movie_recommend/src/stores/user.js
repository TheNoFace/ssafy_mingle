import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import { defineStore } from "pinia"
import axios from "axios"

export const useUserStore = defineStore("user", () => {
    const AUTH_BASE_URL = "http://127.0.0.1:8000/api/auth"
    const router = useRouter()
    const sessionData = ref(null)
    const userData = ref(null)
    const followCount = ref(null)
    const followingCount = ref(null)

    const isLogin = computed(() => {
      if (sessionData.value) {
        return true
      } else {
        return false
      }
    })

    const userSignUp = function (payload) {
      axios({
        method: "post",
        url: `${AUTH_BASE_URL}/create/`,
        data: payload,
      })
        .then((response) => {
          payload.delete("nickname")
          axios({
            method: "post",
            url: `${AUTH_BASE_URL}/login/`,
            data: payload,
          })
            .then((response) => {
              sessionData.value = response.data
              router.push({ name: "MainView" })
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((error) => {
          console.log(error)
        })
    }

    const getProfile = function (userName) {
      axios({
        method: "get",
        url: `${AUTH_BASE_URL}/profile/${userName}/`,
      })
        .then((response) => {
          // console.log(response.data)
          userData.value = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    }

    const updateProfile = function (payload) {
      axios({
        method: "put",
        url: `${AUTH_BASE_URL}/update/`,
        headers: {
          Authorization: `Token ${sessionData.value.token}`,
        },
        data: payload,
      })
        .then((response) => {
          getProfile(response.data.username)
          router.push({
            name: "ProfileView",
            params: { username: response.data.username },
          })
        })
        .catch((error) => {
          console.log(error)
        })
    }

    const logOut = function () {
      axios({
        method: "post",
        url: `${AUTH_BASE_URL}/logout/`,
        headers: {
          Authorization: `Token ${sessionData.value.token}`,
        },
      })
        .then((response) => {
          sessionData.value = null
          userData.value = null
          localStorage.clear()
          router.push({ name: "MainView" })
        })
        .catch((error) => {
          console.log(error)
        })
    }

    const logOutAll = function () {
      axios({
        method: "post",
        url: `${AUTH_BASE_URL}/logoutall/`,
        headers: {
          Authorization: `Token ${sessionData.value.token}`,
        },
      })
        .then((response) => {
          sessionData.value = null
          userData.value = null
          localStorage.clear()
          router.push({ name: "MainView" })
        })
        .catch((error) => {
          console.log(error)
        })
    }

    return {
      AUTH_BASE_URL,
      sessionData,
      isLogin,
      userSignUp,
      getProfile,
      updateProfile,
      userData,
      logOut,
      logOutAll,
    }
  },
  { persist: true }
)

export const useUserTempStore = defineStore("userTemp", () => {
  const userStore = useUserStore()
  const hasPermission = ref(false)
  const tempData = ref(null)
  const isFollowing = ref(null)

  const checkPermission = function (username = null) {
    if (userStore.sessionData) {
      if (username) {
        axios({
          method: "post",
          url: `${userStore.AUTH_BASE_URL}/profile/${username}/check/`,
          headers: {
            Authorization: `Token ${userStore.sessionData.token}`,
          },
        })
          .then(() => {
            hasPermission.value = true
          })
          .catch((error) => {
            // console.log((error.response.status))
          })
      } else {
        axios({
          method: "get",
          url: `${userStore.AUTH_BASE_URL}/profile/undefined/check/`,
          headers: {
            Authorization: `Token ${userStore.sessionData.token}`,
          },
        })
          .then((response) => {
            tempData.value = response.data
          })
          .catch((error) => {
            // console.log((error.response.status))
          })
      }
    }
  }

  return {
    hasPermission,
    checkPermission,
    tempData
  }
})
