import { createWebHistory, createRouter } from "vue-router";

import Home from "./components/Home";
import Calendar from "./components/DiaryCalendar";
import Canvas from "./components/CanvasDrawing";
import Writing from "./components/DiaryWriting";
import Login from "./components/Login";
import SignUp from "./components/SignUp";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/calendar",
    component: Calendar,
  },
  {
    path: "/canvas",
    component: Canvas,
  },
  {
    path: "/writing",
    component: Writing,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/signup",
    component: SignUp,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
