<template>
  <v-layout class="rounded rounded-md">
    <v-navigation-drawer permanent>
      <v-list-item title="Система отеля"></v-list-item>
      <v-divider></v-divider>
      <template v-if="!Token.token">
        <router-link to="/login" style="text-decoration: none; color: inherit"
          ><v-list-item link title="Войти"></v-list-item
        ></router-link>
        <router-link
          to="/register"
          style="text-decoration: none; color: inherit"
          ><v-list-item link title="Зарегистрироваться"></v-list-item
        ></router-link>
      </template>
      <v-list-item v-else class="text-red" @click="Token.deleteToken"
        >Выйти</v-list-item
      >

      <router-link
        to="/apartments"
        style="text-decoration: none; color: inherit"
        ><v-list-item link title="Номера"></v-list-item
      ></router-link>
      <router-link to="/guests" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Гости"></v-list-item
      ></router-link>
      <router-link to="/residents" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Постояльцы"></v-list-item
      ></router-link>
      <router-link to="/cleaners" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Уборщики"></v-list-item
      ></router-link>
      <router-link to="/schedules" style="text-decoration: none; color: inherit"
        ><v-list-item link title="График уборки"></v-list-item
      ></router-link>
      <router-link to="/report" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Отчет"></v-list-item
      ></router-link>
    </v-navigation-drawer>
    <v-main
      class="d-flex align-center justify-center"
      style="min-height: 300px"
    >
      <router-view />
    </v-main>
  </v-layout>
</template>

<script setup>
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
</script>

<style></style>
