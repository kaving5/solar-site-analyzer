import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { SiteService } from '../../core/services/site.service';

@Component({
  selector: 'app-site-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './site-detail.component.html'
})
export class SiteDetailComponent implements OnInit {

  site: any = null;
  loading = false;
  errorMessage = '';

  constructor(
    private route: ActivatedRoute,
    private siteService: SiteService
  ) {}

  ngOnInit(): void {
    const siteId = Number(this.route.snapshot.paramMap.get('id'));
    this.fetchSite(siteId);
  }

  fetchSite(siteId: number) {
    this.loading = true;
    this.siteService.getSiteById(siteId).subscribe({
      next: (res: any) => {
        this.site = res.data;
        this.loading = false;
      },
      error: () => {
        this.errorMessage = 'Failed to load site details';
        this.loading = false;
      }
    });
  }
}
