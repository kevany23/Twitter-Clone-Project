<template>
  <div>
    <NavBar></NavBar>
    <b-form>
      <b-row>
        <b-button v-on:click="authenticationTest">
          Authentication Test
        </b-button>
      </b-row>
      <b-row>
        <b-button v-on:click="localStorageTest">
          Local Storage Test
        </b-button>
      </b-row>
    </b-form>
  </div>
</template>

<script>
/* eslint-disable */
import { BACKEND_URL, url } from "../config/urls.js";
import axios from "axios";
import * as loginStorage from "../config/LoginStorage.js";
import NavBar from "../components/NavBar.vue";

export default {
  name: "Home",
  components: {
    NavBar
  },
  created() {},
  data() {
    return {};
  },
  methods: {
    isAuthenticated() {
      return loginStorage.isLoggedIn();
    },
    authenticationTest() {
      axios.get(url('protected'), {
        headers: loginStorage.authHeader(),
        access_token: this.access_token,
      })
      .then( (res) => {
        console.log("Succeess");
        console.log(res);
      }

      )
      .catch( (err) => {
        console.log("Error");
        console.log(err);
        //this.$router.push('/about');
      }

      );
    },
    localStorageTest() {
      console.log(loginStorage.getLoginToken());
    },
  }
};
</script>