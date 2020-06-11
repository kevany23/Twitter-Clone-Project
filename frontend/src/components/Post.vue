<template>
<div>
  <b-card>
    <h3>{{username}}</h3>
    <p>{{formatDate(timestamp)}}</p>
    <p>
    {{content}}
    </p>
    <b-button-toolbar
    style="justify-content: center"
    >
      <b-button-group>
        <b-button
        v-bind:style="likeButtonStyle"
        v-on:click="onLikeClick"
        >
          <b-icon-arrow-up class="h4 mb-0">
          </b-icon-arrow-up>
        </b-button>
        <b-button v-on:click="toggleComments">
          Comments
        </b-button>
      </b-button-group>
    </b-button-toolbar>
    <div>
      <b-collapse v-model="showComments">
        <table
        style="width:100%"
        >
          <tbody>
            <tr
            class="commentRow"
            style="width:100%"
            v-for="comment in comments"
            :key="comment.content"
            >
              <td class="commentUsername">
                <b>{{comment.username}}</b>
              </td>
              <td class="commentContent">
                {{comment.content}}
              </td>
            </tr>
          </tbody>
        </table>
        <b-form
        style="margin-top: 5px;"
        >
          <b-row>
            <b-form-textarea
            style="height:50px"
            placeholder="Add a comment..."
            v-model="commentContent"
            >
            </b-form-textarea>
          </b-row>
          <b-row>
            <b-button
            v-on:click="submitComment"
            >
              Comment
            </b-button>
          </b-row>
        </b-form>
      </b-collapse>
    </div>
  </b-card>
</div>
</template>

<script>
/* eslint-disable */
import formatPostDate from '../util/DateTime.js';
import { BootstrapVue, BIcon, BIconArrowUp } from 'bootstrap-vue';
export default {
  name: "Post",
  components: {
    BIconArrowUp,
  },
  props: ['id', 'content', 'username', 'timestamp', 'liked', 'comments'],
  mounted() {
      this.buttonMode = this.liked;
      if (this.liked) {
        this.likeButtonStyle.backgroundColor = 'Gray';
      } else {
        this.likeButtonStyle.backgroundColor = 'DodgerBlue';
      }
  },
  data() {
    return {
      likeButtonStyle: {
        backgroundColor: 'DodgerBlue',
        buttonMode: false,
      },
      showComments: false,
      commentContent: "",
    };
  },
  methods: {
    formatDate(timestamp) {
      return formatPostDate(timestamp);
    },
    onLikeClick() {
      this.buttonMode = ! this.buttonMode;
      if (this.buttonMode) {
        this.likeButtonStyle.backgroundColor = 'Gray';
        this.like();
      } else {
        this.likeButtonStyle.backgroundColor = 'DodgerBlue';
        this.unlike();
      }
    },
    like() {
      this.$emit('post-liked', this.id);
    },
    unlike() {
      this.$emit('post-unliked', this.id);
    },
    toggleComments() {
      this.showComments = ! this.showComments;
    },
    submitComment() {
      this.$emit('comment-submit', this.id, this.commentContent);
    },
  },
}
</script>

<style>
.commentRow {
  height: 50px;
  border-color: SkyBlue;
  border-style: none;
  margin-bottom: 1em;
  margin-top: 10px;
}
.commentUsername {
  width: 200px;
  text-align: left;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
  background-color: whitesmoke;
  padding-left: 8px;
}
.commentContent {
  width: 600px;
  text-align: left;
  border-top-right-radius: 15px;
  border-bottom-right-radius: 15px;
  padding-left: 8px;
  background-color: whitesmoke;
}
</style>