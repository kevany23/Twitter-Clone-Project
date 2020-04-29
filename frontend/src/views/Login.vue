<template>
  <div id="loginDiv">
    <div>
      <b-container fluid>
        <b-form>
          Login Here
          <b-row>
            <b-form-input
            class="loginField"
            placeholder="Username"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-form-input
            class="loginField"
            type="password"
            placeholder="Password"
            >
            </b-form-input>
          </b-row>
          <b-row>
            <b-button
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
      foo: 1,
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
    }
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