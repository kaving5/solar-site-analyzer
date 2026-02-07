import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SiteService } from '../../core/services/site.service';
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-site-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './site-list.component.html',
  styleUrls: ['./site-list.component.scss']
})
export class SiteListComponent implements OnInit {

  sites: any[] = [];
  loading = false;
  errorMessage = '';

  constructor(private siteService: SiteService) {}

  ngOnInit(): void {
    this.loadSites();
  }

  loadSites() {
    this.loading = true;
  
    this.siteService.getAllSites().subscribe({
      next: (sites) => {
        this.sites = sites;      
        this.loading = false;
      },
      error: () => {
        this.errorMessage = 'Failed to load sites';
        this.loading = false;
      }
    });
  }
}
