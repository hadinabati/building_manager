import Login from "../pages/Login/Login"
import DashBoard from "pages/AdminDashboard/DashBoard";
import building_info from "pages/AdminDashboard/building_info/building_info";
import out_money from "pages/AdminDashboard/out_money/out_money";
import incoming_page from "pages/AdminDashboard/incoming/incoming_page";
import sandbox from "pages/AdminDashboard/sandBox/sandbox";
import Dashboard from "pages/user_Dashboard/Dashboard";
import info from "../pages/AdminDashboard/info"

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        component: info
      },
      {
        path: 'Dashboard',
        component: DashBoard
      },
      {
        path: 'Dashboard/building_info',
        component: building_info
      },
      {
        path: 'Dashboard/money',
        component: out_money
      },
      {
        path: 'Dashboard/incoming',
        component: incoming_page
      },
      {
        path: 'Dashboard/cash_box',
        component: sandbox
      }
      , {
        path: 'Dashboard/user_Dashboard',
        component: Dashboard
      }
    ]
  },

  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
