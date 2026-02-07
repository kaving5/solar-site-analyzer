import { Injectable } from '@angular/core';
import { map, Observable } from 'rxjs';
import { ApiService } from './api.service';
import { Site } from '../models/site.model';

@Injectable({
  providedIn: 'root'
})
export class SiteService {

  constructor(private api: ApiService) {}

  getAllSites() {
    return this.api.get<any>('get_all_sites').pipe(
      map(res => res.data)  
    );
  }

  getSiteById(siteId: number): Observable<any> {
    return this.api.post<any>('get_site_by_id', {
      site_id: siteId
    });
  }
}

