

const state = {
   token : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MmEyZmExYTMyYzMyNjRmMTRiODM5NjciLCJ1c2VybmFtZSI6ImFkbWluIiwic2NvcGUiOlsiYWRtaW4iLCJhdXRoZW50aWNhdGVkIl19.jPkjcLN_7Q78tCfjpBAMTtwGIA2Yepwz9f7NdG8HFVI'
}
const mutations = {}
const actions = {

}
const getters = {

  get_token:(state)=>{
    return state.token
  }

}

export  default {
  namespace :true,
  state ,
  getters,
  mutations,
  actions
}


