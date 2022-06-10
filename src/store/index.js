import { store } from 'quasar/wrappers'
import { createStore } from 'vuex'
import StoreBase from "src/store/StoreBase";

export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      StoreBase
    },

    strict: process.env.DEBUGGING
  })
  return Store
})
