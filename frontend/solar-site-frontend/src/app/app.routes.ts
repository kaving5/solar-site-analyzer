import { Routes } from '@angular/router';
import { SiteListComponent } from './pages/site-list/site-list.component';
import { SiteDetailComponent } from './pages/site-detail/site-detail.component';
import { StatisticsComponent } from './pages/statistics/statistics.component';
import { AnalyzeComponent } from './pages/analyze/analyze.component';

export const routes: Routes = [
  { path: 'sites', component: SiteListComponent },
  { path: 'sites/:id', component: SiteDetailComponent },
  { path: 'analyze', component: AnalyzeComponent },
  { path: 'statistics', component: StatisticsComponent },
  { path: '', redirectTo: 'sites', pathMatch: 'full' }
];
