<template>
<div>
  <b-card>
    <h3>{{username}}</h3>
    <p>{{formatDate(timestamp)}}</p>
    <p>
    {{content}}
    </p>
  </b-card>
</div>
</template>

<script>
/* eslint-disable */
import formatPostDate from '../util/DateTime.js';
export default {
  name: "Post",
  props: ['content', 'username', 'timestamp'],
  methods: {
    formatDate(timestamp) {
      return formatPostDate(timestamp);
    }
  },
}
</script>

<style>
</style>