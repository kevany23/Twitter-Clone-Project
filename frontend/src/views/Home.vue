<template>
  <div id="homeDiv">
    <NavBar></NavBar>
    <b-form>
      <b-row>
        <b-button
        style="display:none;"
        v-on:click="authenticationTest"
        >
          Authentication Test
        </b-button>
      </b-row>
      <b-row>
        <b-button
        style="display:none;"
        v-on:click="localStorageTest"
        >
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
          placeholder="Write a status..."
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
    <br>
    <div id="newsFeed">
      <div
      v-for="(post, idx) in posts"
      :key="idx"
      >
        <Post
        v-bind:content="post.content"
        v-bind:timestamp="post.timestamp"
        v-bind:username="post.username"
        v-bind:id="post.id"
        v-bind:liked="post.liked"
        v-bind:comments="post.comments"
        @post-liked="handleLike"
        @post-unliked="handleUnlike"
        @comment-submit="submitComment"
        ></Post>
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
import Post from "../components/Post.vue"

export default {
  name: "Home",
  components: {
    NavBar,
    Post
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
        this.posts = res.data.posts;
      })
      .catch( (res) => {
        console.log("Error");
      })
    },
    handleLike(postId) {
      axios.post(url('likePost'), {
        postId: postId
      },
      {
        headers: loginStorage.authHeader(),
      })
      .then( (res) => {
        console.log("Success");
      })
      .catch( (res) => {
        console.log("Error");
      });
    },
    handleUnlike(postId) {
      console.log("Unliked");
      console.log(postId);
      axios.post(url('unlikePost'), {
        postId: postId
      },
      {
        headers: loginStorage.authHeader(),
      })
      .then( (res) => {
        console.log("Success");
      })
      .catch( (res) => {
        console.log("Error");
      });
    },
    submitComment(postId, content) {
      axios.post(url('submitComment'), {
        postId: postId,
        content: content,
      },
      {
        headers: loginStorage.authHeader(),
      })
      .then ( (res) => {
        console.log("Success");
      })
      .catch( (res) => {
        console.log("Error");
      });
    },
  }
};
</script>

<style>
#postStatus {
  position: relative;
  width: 800px;
  left: 15%;
}
#newsFeed {
  position: relative;
  left: 10%;
  width: 70%;
}
</style>