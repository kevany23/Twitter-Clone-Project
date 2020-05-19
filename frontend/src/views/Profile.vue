<template>
  <div>
    <NavBar></NavBar>
    <br>
    <h2>Following</h2>
    <br>
    <ul>
      <li v-for="user in followList" :key="user.username">
        {{ user.username }}
      </li>
    </ul>
  </div>
</template>

<script>
/* eslint-disable */
import { BACKEND_URL, url } from "../config/urls.js";
import axios from "axios";
import * as loginStorage from "../config/LoginStorage.js";
import NavBar from "../components/NavBar.vue";

export default {
  name: "Profile",
  components: {
    NavBar,
  },
  created() {
    axios.get(url('getFollowing'), {
      headers: loginStorage.authHeader(),
    })
    .then( (res) => {
      console.log("Success");
      console.log(res);
      this.followList = res.data.following;
    })
    .catch( (err) => {
      console.log("Error");
    });
  },
  data() {
    return {
      followList: [],
    };
  },
  methods: {
  },
};
</script>