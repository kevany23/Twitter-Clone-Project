<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    {{foobar}}
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
/* eslint-disable */
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import BACKEND_URL from '../config/urls.js';

export default {
  name: 'VueHome',
  components: {
    HelloWorld,
  },
  data() {
    return {
      foobar: process.env.foo,
    };
  },
  methods: {
    getEnv: function() {
      //console.log(process.env);
      console.log(BACKEND_URL);
    },
  },
};
</script>
