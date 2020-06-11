<template>
  <div>
    <NavBar></NavBar>
    <div id="searchBar">
      <b-form>
        <b-form-input
        type="text"
        placeholder="Search username"
        v-model="query"
        >
        </b-form-input>
      </b-form>
    </div>
    <br>
    <div id ="cardDiv">
      <div
      v-for="user in userList"
      :key="user.id"
      >
      <b-card
      class = "userCard"
      v-bind:title="user.username"
      >
        <b-button
        v-on:click="followButtonClick(user)"
        >
          {{followButtonDisplay(user)}}
        </b-button>
      </b-card>
      </div>
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
  name: "SearchUser",
  components: {
    NavBar,
  },
  created() {
    this.findUsers();
  },
  data() {
    return {
      query: "",
      userList: [],
    };
  },
  methods: {
    findUsers() {
      axios.get(url("findUsers"), {
        headers: loginStorage.authHeader(),
        query: this.query,
      })
      .then( (res) => {
        console.log("Success");
        console.log(res);
        this.userList = res.data.users;
      })
      .catch( (err) => {
        console.log("Error");
      });
    },
    followButtonDisplay(user) {
      if (user.following) {
        return "Unfollow"
      } else {
        return "Follow"
      }
    },
    followButtonClick(user) {
      if (user.following) {
        this.unfollowUser(user);
      } else {
        this.followUser(user);
      }
    },
    followUser(user) {
      let username = user.username;
      console.log(user);
      axios.post(url("followUser"), {
        toFollow: username,
      },
      {
        headers: loginStorage.authHeader(),
      })
      .then( (res) => {
        console.log("Success");
        console.log(res);
        user.following = true;
      })
      .catch( (err) => {
        console.log("Error");
      });
    },
    unfollowUser(user) {
      let username = user.username;
      console.log(user);
      axios.post(url("unfollowUser"), {
        toUnfollow: username,
      },
      {
        headers: loginStorage.authHeader(),
      })
      .then( (res) => {
        console.log("Success");
        console.log(res);
        user.following = false;
      })
      .catch( (err) => {
        console.log("Error");
      });
    },
  }
};
</script>

<style>
#searchBar {
  width: 500px;
  justify-content: center;
}
#cardDiv {
  display: flex;
  flex-direction: row;
}
.userCard {
  width: 400px;
}
</style>