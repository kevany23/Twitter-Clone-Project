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
    <br>
    <div id=postStatus>
      <b-form>
        <b-row>
          <b-form-textarea
          v-model="postContent"
          style="height:150px"
          >
          </b-form-textarea>
        </b-row>
        <b-row>
          <b-button v-on:click="submitPost">
          Post Status
          </b-button>
        </b-row>
      </b-form>
    </div>
    <div id="newsFeed">
      <table>
        <tr>
        </tr>
      </table>
    </div>
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
  created() {
    this.loadPosts();
  },
  data() {
    return {
      postContent: "",
      posts: [],
    };
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
    submitPost() {
      axios.post(url('submitPost'), {
        content: this.postContent,
      },
      {
        headers: loginStorage.authHeader()
      })
      .then( (res) => {
        console.log("Success");
      })
      .catch( (err) => {
        console.log("Error");
      });
    },
    loadPosts() {
      axios.get(url('getPosts'), {
        headers: loginStorage.authHeader(),
      })
      .then( (res) => {
        console.log("Success");
      })
      .catch( (res) => {
        console.log("Error");
      })
    },
  }
};
</script>

<style>
#postStatus {
  position: absolute;
  width: 800px;
  left: 10%;
}
</style>