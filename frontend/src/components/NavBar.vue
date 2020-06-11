<template>
  <b-navbar
  style="background-color:aqua;"
  >
    <b-navbar-nav>
    <b-nav-item>
      <router-link to="/home">
      Home
      </router-link>
    </b-nav-item>
    <b-nav-item>
      <router-link to="/profile">
      Profile
      </router-link>
    </b-nav-item>
    <b-nav-item>
      <router-link to="/searchUser">
      Search User
      </router-link>
    </b-nav-item>
    </b-navbar-nav>
    <b-navbar-nav class="ml-auto">
      <b-nav-item>
        <router-link to="/about">
        About
        </router-link>
      </b-nav-item>
      <b-nav-item
      v-on:click="logOut"
      >
        Logout
      </b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
/* eslint-disable */
import { BACKEND_URL, url } from "../config/urls.js";
import axios from "axios";
import * as loginStorage from "../config/LoginStorage.js";

export default {
  name: "NavBar",
  components: {},
  data() {
    return {};
  },
  methods: {
    logOut() {
      const tokenHeader = loginStorage.authHeader();
      loginStorage.deleteLoginToken();
      axios.get(url("logout"), {
          headers: tokenHeader,
        })
        .then((res) => {
          console.log("Success");
          console.log(res);
          this.$router.push('/login');
        })
        .catch((err) => {
          console.log("Error");
        });
    },
  },
};
</script>