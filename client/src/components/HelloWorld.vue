<script>
import ChatBox from './chat/ChatBox.vue'
import LessonCard from './chat/lessonCard.vue'

export default {
  data() {
    return {
      chat: [],
      message: null,
    }
  },
  methods: {
    sendMessage() {
      if(this.message != null) {
        this.axios.post(`http://127.0.0.1:5000/ask-me`, {input: this.message}).then((response) => {
          console.log(response)
          this.chat.push({
            isSender: false,
            text: response.data
          });
          setTimeout(() => {
            let messages = this.$el.querySelector('#messages')
            messages.scrollTop = messages.scrollHeight
          }, 100);
        })
        this.chat.push({
          isSender: true,
          text: this.message
        });
        this.message = null
  
        setTimeout(() => {
          let messages = this.$el.querySelector('#messages')
          messages.scrollTop = messages.scrollHeight
        }, 100);
      }
    }
  },
  components: {
    ChatBox,
    LessonCard
  }
}
</script>

<template>
  <div>
    <div class="bg-[#343541] h-screen w-full grid grid-cols-12">
      <div class="col-span-12 lg:col-span-9">
        <div>
          <div class="bg-[#343541] w-full h-[calc(100vh-174px)] overflow-y-scroll" ref="chatContainer" id="messages">
            <div class="grid grid-cols-12 gap-y-2">
              <chat-box v-for="(chatMessage, index) in chat" :key="index" :isSender="chatMessage.isSender" :something="{text: chatMessage.text}" />
            </div>
            
          </div>
          <div class="bg-[#343541] w-full h-40">
            <div class="flex px-4 pt-0">
              <div class="mx-1">
                <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M22 0h-20v6h1.999c0-1.174.397-3 2.001-3h4v16.874c0 1.174-.825 2.126-2 2.126h-1v2h9.999v-2h-.999c-1.174 0-2-.952-2-2.126v-16.874h4c1.649 0 2.02 1.826 2.02 3h1.98v-6z"/></svg>
                </button>
              </div>
              <div class="mx-1">
                <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                  <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M24 22h-24v-20h24v20zm-1-19h-22v18h22v-18zm-1 16h-19l4-7.492 3 3.048 5.013-7.556 6.987 12zm-11.848-2.865l-2.91-2.956-2.574 4.821h15.593l-5.303-9.108-4.806 7.243zm-4.652-11.135c1.38 0 2.5 1.12 2.5 2.5s-1.12 2.5-2.5 2.5-2.5-1.12-2.5-2.5 1.12-2.5 2.5-2.5zm0 1c.828 0 1.5.672 1.5 1.5s-.672 1.5-1.5 1.5-1.5-.672-1.5-1.5.672-1.5 1.5-1.5z"/></svg>
                </button>
              </div>
              <div class="mx-1">
                <button class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
                  <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M16 24h-8v-1h3.5v-3.018c-3.63-.256-6.5-3.287-6.5-6.982v-2h1v2.01c.005 3.307 2.692 5.99 6 5.99 3.311 0 6-2.689 6-6v-2h1v2c0 3.695-2.87 6.726-6.5 6.982v3.018h3.5v1zm-9-19c0-2.76 2.24-5 5-5s5 2.24 5 5v8c0 2.76-2.24 5-5 5s-5-2.24-5-5v-8zm9 0c0-2.208-1.792-4-4-4s-4 1.792-4 4v8c0 2.208 1.792 4 4 4s4-1.792 4-4v-8z"/></svg>
                </button>
              </div>
            </div>
            <div class="grid grid-cols-12 lg:grid-cols-11 md:grid-cols-10 sm:grid-cols-9 px-4 pt-2 gap-2">
              <div class="col-span-11 lg:col-span-10 md:col-span-9 sm:col-span-8">
                <textarea rows="4"  class=" p-2.5 w-full text-sm rounded-lg bg-[#40414F] placeholder-gray-400 text-white" placeholder="اسأل تيسير..." v-model="message">{{ message }}</textarea>
              </div>
              <div class="grid py-1">
                <button @click="sendMessage" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center h-full">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M0 12l11 3.1 7-8.1-8.156 5.672-4.312-1.202 15.362-7.68-3.974 14.57-3.75-3.339-2.17 2.925v-.769l-2-.56v7.383l4.473-6.031 4.527 4.031 6-22z"/></svg>
                </button>
              </div>
            </div>
          </div>

        </div>

      </div>
      <div class="h-screen bg-[#40414F] col-span-0 lg:col-span-3">
        <div class="w-full text-center mt-10">
          <span class="text-xl font-bold text-white">الدروس السابقة</span>
        </div>
        <div class="w-full pl-4 pr-2 my-5">
          <lesson-card subject="درس العلوم" />
          <lesson-card subject="درس الرياضيات" />
          <lesson-card subject="درس التاريخ" />
        </div>
        
      </div>
    </div>
  </div>
  
</template>

<style scoped>

</style>
