import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class AnalysisService {

  constructor(private api: ApiService) {}

  analyze(weights: any) {
    return this.api.post('analyze', {
      weights
    });
  }

  getStatistics() {
    return this.api.get('statistics');
  }
}
