<template>
  <q-layout view="hHh lpR lfr" style="direction: rtl">

    <q-header elevated class="bg-purple-10">
      <q-toolbar>
        <q-btn flat @click="drawer = !drawer" round dense icon="menu"/>
        <q-toolbar-title style="text-align: center ; text-decoration: none; font-family:myvazir">
          <router-link  to="/" style ="text-decoration: none ;color: aliceblue ; font-family: myvazir">پنل مدیریت ساختمانی</router-link>
        </q-toolbar-title>

      </q-toolbar>
    </q-header>

    <q-drawer

      v-model="drawer"
      show-if-above
      side="right"
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      :width="300"
      :breakpoint="500"
      bordered
      class="bg-grey-3"
    >
      <q-scroll-area class="fit">
        <q-list bordered class="rounded-borders">
          <q-expansion-item
            expand-separator
            icon="dashboard"
            label="مدیریت ساختمان"
            class="text"
          >
            <q-item class="text">
              <router-link class="router" to="Dashboard"> پنل مدیریتی </router-link>
            </q-item>
          </q-expansion-item>
        </q-list>
        <q-list bordered class="rounded-borders">
          <q-expansion-item
            expand-separator
            icon="person"
            label="کاربران"
            class="text۲"
          >
            <q-item class="text">
              <router-link class="router" to="Dashboard"> پنل شخصی </router-link>
            </q-item>
          </q-expansion-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>

  </q-layout>
</template>

<script>
import {ref} from 'vue'

export default {

  data() {
    const rightDrawerOpen = ref(false)
    return {
      drawer: ref(false),
      miniState: ref(true),

    }
  }
}
</script>

<style>
.text{
  color: #ec2673;
  font-size: 12pt;
}
.text۲{
  font-family: myvazir;
  color: #0468a9;
  font-size: 12pt;
}
.router{
  text-decoration: none;
  font-family: myvazir;
  color: #000000;
}
</style>
