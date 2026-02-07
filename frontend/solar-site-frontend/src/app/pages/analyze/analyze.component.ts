import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AnalysisService } from '../../core/services/analysis.service';


type WeightKey = 'solar' | 'area' | 'grid' | 'slope' | 'infrastructure';

@Component({
  selector: 'app-analyze',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './analyze.component.html'
})
export class AnalyzeComponent {


  weightKeys: WeightKey[] = [
    'solar',
    'area',
    'grid',
    'slope',
    'infrastructure'
  ];


  weights: Record<WeightKey, number> = {
    solar: 0.35,
    area: 0.25,
    grid: 0.20,
    slope: 0.15,
    infrastructure: 0.05
  };

  results: any[] = [];
  loading = false;
  errorMessage = '';

  constructor(private analysisService: AnalysisService) {}


  get totalWeight(): number {
    return Object.values(this.weights).reduce((a, b) => a + b, 0);
  }

  analyze(): void {
    this.errorMessage = '';
    this.results = [];
    this.loading = true;

    this.analysisService.analyze(this.weights).subscribe({
      next: (res: any) => {
        this.results = res.data.results;
        this.loading = false;
      },
      error: () => {
        this.errorMessage = 'Analysis failed. Please check weights.';
        this.loading = false;
      }
    });
  }
}
