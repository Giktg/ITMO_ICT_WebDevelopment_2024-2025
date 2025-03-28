import { createRouter, createWebHistory } from "vue-router";
import Login from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import ApartamentsList from "@/components/Apartments/ApartamentsList.vue";
import ApartamentsPage from "@/components/Apartments/ApartamentsPage.vue";
import AddGuest from "@/components/Guests/addGuest.vue";
import GuestsList from "@/components/Guests/GuestsList.vue";
import GuestPage from "@/components/Guests/GuestPage.vue";
import findCity from "@/components/Guests/findCity.vue";
import AddResident from "@/components/Residents/AddResident.vue";
import ResidentsList from "@/components/Residents/ResidentsList.vue";
import ResidentsPage from "@/components/Residents/ResidentsPage.vue";
import FindOtherResident from "@/components/Residents/FindOtherResident.vue";
import FindCleaner from "@/components/Residents/FindCleaner.vue";
import AddCleaner from "@/components/Cleaners/AddCleaner.vue";
import CleanersList from "@/components/Cleaners/CleanersList.vue";

import ScheduleList from "@/components/Schedule/ScheduleList.vue";
import AddSchedule from "@/components/Schedule/AddSchedule.vue";
import SchedulePage from "@/components/Schedule/SchedulePage.vue";

import ReportPage from "@/components/Report/ReportPage.vue";

const routes = [
  { path: "/login", component: Login },
  { path: "/register", component: RegisterPage },
  { path: "/apartments", component: ApartamentsList },
  { path: "/apartments/:id", component: ApartamentsPage },
  { path: "/add-guest", component: AddGuest },
  { path: "/guests", component: GuestsList },
  { path: "/guests/:id", component: GuestPage },
  { path: "/guests/find", component: findCity },
  { path: "/add-residents", component: AddResident },
  { path: "/residents", component: ResidentsList },
  { path: "/residents/:id", component: ResidentsPage },
  { path: "/residents/:id/other_residents", component: FindOtherResident },
  { path: "/residents/find-cleaner", component: FindCleaner },
  { path: "/add-cleaner", component: AddCleaner },
  { path: "/cleaners", component: CleanersList },
  { path: "/add-schedule", component: AddSchedule },
  { path: "/schedules/:id", component: SchedulePage },
  { path: "/schedules/", component: ScheduleList },
  { path: "/report", component: ReportPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
