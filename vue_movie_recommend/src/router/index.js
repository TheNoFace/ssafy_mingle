import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import CategoryView from "@/views/CategoryView.vue";
import ReviewView from "@/views/ReviewView.vue";
import ProfileView from "@/views/ProfileView.vue";
import DetailView from "@/views/DetailView.vue";
import MovieReviewView from "@/views/MovieReviewView.vue";
import ProfileUpdateView from "@/views/ProfileUpdateView.vue";
import SignUpView from "@/views/SignUpView.vue";
import CategoryRecommendMovie from "@/component/Category/CategoryRecommendMovie.vue";
import CategoryMain from "@/component/Category/CategoryMain.vue";
import ReviewDetailView from "@/views/ReviewDetailView.vue";
import ProfileGenre from "@/component/Profile/ProfileGenre.vue";
import ProfileMovie from "@/component/Profile/ProfileMovie.vue";
import ProfileReview from "@/component/Profile/ProfileReview.vue";
import ProfileComment from "@/component/Profile/ProfileComment.vue";
import ReviewFormView from "@/views/ReviewFormView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "MainView",
      component: MainView,
    },
    {
      path: "/category",
      component: CategoryView,
      children: [
        {
          path: "",
          name: "CategoryView",
          component: CategoryMain,
        },
        {
          path: ":category_id",
          name: "CategoryRecommendMovie",
          component: CategoryRecommendMovie,
        },
      ],
    },
    {
      path: "/review",
      name: "ReviewView",
      component: ReviewView,
    },
    {
      path: "/detail/:tmdb_id",
      name: "DetailView",
      component: DetailView,
    },
    {
      path: "/detail/:tmdb_id/review",
      name: "MovieReviewView",
      component: MovieReviewView,
    },
    {
      path: "/profile/:username",
      name: "ProfileView",
      component: ProfileView,
      children: [
        {
          path: "genre",
          name: "ProfileGenre",
          component: ProfileGenre,
        },
        {
          path: "movie",
          name: "ProfileMovie",
          component: ProfileMovie,
        },
        {
          path: "review",
          name: "ProfileReview",
          component: ProfileReview,
        },
        {
          path: "comment",
          name: "ProfileComment",
          component: ProfileComment,
        },
      ],
    },
    {
      path: "/profile/update",
      name: "ProfileUpdateView",
      component: ProfileUpdateView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/review/:review_id",
      name: "ReviewDetailView",
      component: ReviewDetailView,
    },
    {
      path: '/:tmdb_id/review',
      name : "ReviewFormView",
      component : ReviewFormView
    }
  ],
});

export default router;
