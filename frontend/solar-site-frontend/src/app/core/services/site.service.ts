import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class SiteService {

  constructor(private api: ApiService) {}

  getAllSites() {
    return this.api.get('get_all_sites');
  }

  getSiteById(siteId: number) {
    return this.api.post('get_site_by_id', {
      site_id: siteId
    });
  }
}
