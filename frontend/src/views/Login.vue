<template>
  <div id="loginDiv">
    <div>
      <b-container fluid>
        <b-form>
          Login Here
          <b-alert show variant="danger">
          Login Failed
          </b-alert>
          <b-row>
            <b-form-input
            class="loginField"
            placeholder="Username"
            v-model="username"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-form-input
            class="loginField"
            type="password"
            placeholder="Password"
            v-model="password"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-button
            v-on:click="loginAuth"
            >
            Log In
            </b-button>
          </b-row>
        </b-form>
        <br>
        <b>OR</b>
        <br>
        <br>
        <b-form>
          Create Account
          <b-row>
            <b-form-input
            class="loginField"
            placeholder="Username"
            v-model="createUsername"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-form-input
            class="loginField"
            type="password"
            placeholder="Password"
            v-model="createPassword"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-form-input
            class="loginField"
            type="password"
            placeholder="Re-enter Password"
            v-model=verifyPassword
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-button
            v-on:click="createAccount"
            >
            Create Account
            </b-button>
          </b-row>
        </b-form>
      </b-container>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
// @ is an alias to /src
import BACKEND_URL from "../config/urls.js";
import axios from "axios";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      createUsername: "",
      createPassword: "",
      verifyPassword:"",
    };
  },
  methods: {
    createAccount() {
      const path = BACKEND_URL + 'createAccount';
      console.log(path);
      axios.post(path, {
        createUsername: this.createUsername,
        createPassword: this.createPassword,
        verifyPassword: this.verifyPassword,
      }).
      then(
        (res) => {
          console.log(res);
        })
      .catch(
        (err) => {
          console.log(err);
        }
      );
    },
    loginAuth() {
      const path = BACKEND_URL + 'loginAuth';
      axios.post(path, {
        username: this.username,
        password: this.password,
      })
      .then(
        (res) => {
          console.log(res);
        }
      )
      .catch(
        (err) => {
          console.log(err);
        }
      );
    },
  }
};
</script>

<style>
.loginField {
  height: 30px;
  width: 200px;
}
#loginDiv {
  position:absolute;
  top:20%;
  left: 40%;
}
</style>