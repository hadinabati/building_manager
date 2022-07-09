export default class URLS {
  constructor() {
    this.main = 'http://127.0.0.1:8000/'
  }
  create_building() {
    return this.main + 'create_building'
  }
  building_list() {
    return this.main + 'building/list'
  }
  apartements_list() {
    return this.main + 'apaterment/list'
  }
  create_apartements() {
    return this.main + 'ap'
  }
  create_money(){
    return this.main + 'create_money'
  }

  create_money_list(){
    return this.main + 'create_money/list'
  }

  check_name(){
    return this.main + 'check_name'
  }
  insert_factor_to_db(){
    return this.main + 'create_factor'
  }
  factor_list(){
    return this.main + 'get_factor_list'
  }
  factor_apartenet_month(){
    return this.main + 'show_apartement_factors'
  }
}



