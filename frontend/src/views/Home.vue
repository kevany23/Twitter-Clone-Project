<template>
  <div>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      Etiam nec nibh nulla. Donec gravida tellus ut tellus rhoncus
      iaculis. Suspendisse volutpat dapibus mi, eget facilisis neque
      placerat non. Cras ac dapibus lectus, eget maximus metus. Aliquam
      sit amet nunc porttitor, pellentesque orci vel, viverra risus. Aenean
      laoreet est eu turpis porttitor eleifend. Cras gravida lacus in maximus ornare.
      Vestibulum tincidunt purus gravida, eleifend dolor nec, lacinia ipsum.
      Sed tellus purus, sagittis nec arcu non, scelerisque sollicitudin nisl.
      Fusce facilisis dapibus risus, in pharetra metus ultrices nec. Nulla in dapibus magna,
      ut pulvinar sapien.
    </p>
    <b-row>
      <b-button v-on:click="logOut">Log Out</b-button>
    </b-row>
  </div>
</template>

<script>
/* eslint-disable */
import { BACKEND_URL, url } from "../config/urls.js";
import axios from "axios";
import * as loginStorage from "../config/LoginStorage.js";

export default {
  name: "Home",
  components: {},
  created() {
  },
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
    }
  }
};
</script>