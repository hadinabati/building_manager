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
}
