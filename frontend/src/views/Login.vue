<template>
  <div id="loginDiv">
    <div>
      <b-container fluid>
        <b-form>
          Login Here
          <b-alert
          show variant="danger"
          v-if="loginFail"
          >
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
          <b-row>
            <b-button
            v-on:click="authenticationTest"
            >
              Authentication Test
            </b-button>
          </b-row>
          <b-row>
            <b-button
            v-on:click="localStorageTest"
            >
              Local Storage Test
            </b-button>
          </b-row>
          <b-row>
            <b-button
            v-on:click="logout"
            >
              Logout
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
import * as loginStorage from "../config/LoginStorage.js"

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
      access_token: "abc",
      loginFail: false,
    };
  },
  created() {
    if (this.isAuthenticated()) {
      console.log("preMounted authenticated");
      this.$router.push('/home');
    } else {
      loginStorage.deleteLoginToken();
    }
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
        (response) => {
          this.access_token = response.data.access_token;
          loginStorage.setLoginToken(this.access_token);
          this.$router.push('/home');
        }
      )
      .catch(
        (err) => {
          console.log(err);
          this.loginFail = true;
        }
      );
    },
    isAuthenticated() {
      return loginStorage.isLoggedIn();
    },
    authenticationTest() {
      const path = BACKEND_URL + 'protected';
      axios.get(path, {
        headers: {
          Authorization: "Bearer " + this.access_token,
        },
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
    logout() {
      loginStorage.deleteLoginToken();
      const path = BACKEND_URL + 'logout';
      axios.get(path, { 
        headers: {
          Authorization: "Bearer " + this.access_token,
        }
      })
      .then( (res) => {
        console.log("Success");
        console.log(res);
      }

      )
      .catch( (err) => {
        console.log("Error");
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