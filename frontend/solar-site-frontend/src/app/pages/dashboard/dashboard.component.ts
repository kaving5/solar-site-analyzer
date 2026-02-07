import { Component, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { AnalysisService } from '../../core/services/analysis.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  stats: any;

  constructor(private statsService: AnalysisService) {}

  ngOnInit(): void {
    this.statsService.getStatistics().subscribe({
      next: (res: any) => {
        this.stats = res.data ?? res;
      },
      error: (err) => console.error(err)
    });
  }
}
