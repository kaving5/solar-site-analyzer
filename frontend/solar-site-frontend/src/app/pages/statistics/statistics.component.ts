import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AnalysisService } from '../../core/services/analysis.service';

@Component({
  selector: 'app-statistics',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './statistics.component.html'
})
export class StatisticsComponent implements OnInit {

  stats: any = null;

  constructor(private analysisService: AnalysisService) {}

  ngOnInit(): void {
    this.analysisService.getStatistics().subscribe((res: any) => {
      this.stats = res.data;
    });
  }
}
