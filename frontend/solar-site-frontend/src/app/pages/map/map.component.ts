import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import * as L from 'leaflet';

import { SiteService } from '../../core/services/site.service';

@Component({
  selector: 'app-map',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.scss']
})
export class MapComponent implements OnInit {
  private map!: L.Map;

  constructor(private siteService: SiteService) {}

  ngOnInit(): void {
    this.initMap();
    this.loadSites();
  }

  initMap() {
    this.map = L.map('map').setView([11.0, 77.0], 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap'
    }).addTo(this.map);
  }

  loadSites() {
    this.siteService.getAllSites().subscribe((sites: any[]) => {
      sites.forEach(site => {
        const marker = L.circleMarker(
          [site.latitude, site.longitude],
          {
            radius: 8,
            color: this.getColor(site.total_score),
            fillOpacity: 0.8
          }
        );

        marker.bindPopup(`
          <strong>${site.site_name}</strong><br/>
          Score: ${site.total_score}
        `);

        marker.addTo(this.map);
      });
    });
  }

  getColor(score: number): string {
    if (score >= 80) return 'green';
    if (score >= 60) return 'orange';
    return 'red';
  }
}
